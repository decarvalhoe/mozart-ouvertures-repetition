import music21 as m21, verovio, pathlib
def clean(part):
    for n in part.recurse().notes:
        for p in (n.pitches if n.isChord else [n.pitch]):
            if p.accidental is not None: p.accidental.displayStatus = None
    ts = part.getElementsByClass(m21.meter.TimeSignature).first() or m21.meter.TimeSignature('2/2')
    for i, mm in enumerate(part.getElementsByClass(m21.stream.Measure)):
        for n in mm.notesAndRests: n.beams = m21.beam.Beams()
        added = False
        if mm.timeSignature is None: mm.timeSignature = ts.__deepcopy__(); added = True
        m21.stream.makeNotation.makeBeams(mm, inPlace=True)
        if added and i > 0: mm.remove(mm.timeSignature)
    return part
def add_dyn(part, dyn):
    for bar, d in dyn:
        for mm in part.getElementsByClass(m21.stream.Measure):
            if mm.number == bar: mm.insert(0, m21.dynamics.Dynamic(d))
def render(score, out_dir, stem, scale=40, extra=None):
    out = pathlib.Path(out_dir); out.mkdir(parents=True, exist_ok=True)
    for p in score.parts: clean(p)
    xml = out / f"{stem}.musicxml"; score.write('musicxml', fp=str(xml))
    tk = verovio.toolkit()
    opts = {"pageWidth": 2200, "pageHeight": 60000, "scale": scale, "adjustPageHeight": True, "breaks": "auto",
            "footer": "none", "header": "none", "mnumInterval": 1, "svgViewBox": True, "spacingStaff": 6, "spacingSystem": 7}
    if extra: opts.update(extra)
    tk.setOptions(opts); tk.loadData(xml.read_text(encoding="utf-8")); svg = tk.renderToSVG(1)
    (out / f"{stem}.svg").write_text(svg, encoding="utf-8"); print(stem, len(svg), "bytes")
