"""Figaro excerpts: pitches from the full-orchestra MIDI (bitmidi 30279, 294 bars), rhythm/articulation per NMA reading."""
import sys, music21 as m21, verovio, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent)); from engrave_common import render as _render
MID = sys.argv[1]; OUT = pathlib.Path(sys.argv[2]); OUT.mkdir(parents=True, exist_ok=True)
s = m21.converter.parse(MID, quantizePost=True)
fag = [p for p in s.parts if 'Fagotti' in str(p.partName)][0]

def dump(m0, m1):
    for m in fag.getElementsByClass(m21.stream.Measure):
        if m0 <= m.number <= m1:
            print(m.number, " ".join((f"{e.nameWithOctave}{e.quarterLength:g}" if e.isNote else f"r{e.quarterLength:g}") for e in m.notesAndRests))

print("== bassoon bars 1-7"); dump(1, 7)
print("== bassoon bars 85-92"); dump(85, 92)
print("== bassoon bars 105-112"); dump(105, 112)

def line_part(m0, m1, label, abbrev, clef, transpose=0, dyn=None, fix=None):
    new = m21.stream.Part(); new.partName = label; new.partAbbreviation = abbrev
    new.insert(0, clef); new.insert(0, m21.key.KeySignature(2)); new.insert(0, m21.meter.TimeSignature('cut'))
    for m in fag.getElementsByClass(m21.stream.Measure):
        if m0 <= m.number <= m1:
            mm = m21.stream.Measure(number=m.number)
            for e in m.notesAndRests:
                e2 = e.__deepcopy__()
                if e2.isNote:
                    e2 = e2.transpose(transpose) if transpose else e2
                    e2.stemDirection = 'unspecified'
                    if e2.pitch.accidental and e2.pitch.accidental.name == 'flat':
                        e2.pitch.getEnharmonic(inPlace=True)
                mm.insert(e.offset, e2)
            if fix: fix(mm)
            new.append(mm)
    if dyn:
        for bar, d in dyn:
            for mm in new.getElementsByClass(m21.stream.Measure):
                if mm.number == bar: mm.insert(0, m21.dynamics.Dynamic(d))
    return new

def fix_open(mm):
    """NMA: bars 1 and 3 end with a quarter note + quarter rest (MIDI has dotted quarter + eighth rest)."""
    els = list(mm.notesAndRests)
    if mm.number == 7 and els:
        n = els[0]; n.quarterLength = 1.0
        for e in els[1:]: mm.remove(e)
        mm.insert(1.0, m21.note.Rest(quarterLength=1.0)); mm.insert(2.0, m21.note.Rest(quarterLength=2.0))
    if mm.number in (1, 3, 5) and els and els[-1].isRest:
        n = els[-2]
        if n.isNote and n.quarterLength == 1.5:
            n.quarterLength = 1.0; mm.remove(els[-1]); mm.insert(3.0, m21.note.Rest(quarterLength=1.0))

def add_slurs(part, spans):
    for (b0, i0, b1, i1) in spans:
        ms = {m.number: m for m in part.getElementsByClass(m21.stream.Measure)}
        a = list(ms[b0].notes)[i0]; b = list(ms[b1].notes)[i1]
        sl = m21.spanner.Slur(a, b); part.insert(0, sl)

def render(score, stem, scale=40):
    xml = OUT / f"{stem}.musicxml"; score.write('musicxml', fp=str(xml))
    tk = verovio.toolkit()
    tk.setOptions({"pageWidth": 2200, "pageHeight": 60000, "scale": scale, "adjustPageHeight": True, "breaks": "auto",
                   "footer": "none", "header": "none", "mnumInterval": 1, "svgViewBox": True, "spacingStaff": 6})
    tk.loadData(xml.read_text(encoding="utf-8")); svg = tk.renderToSVG(1)
    (OUT / f"{stem}.svg").write_text(svg, encoding="utf-8"); print(stem, len(svg), "bytes")

# F1: opening unison, violin I register (one octave above bassoon), pp, slurs per NMA
vl = line_part(1, 7, "Violons, altos, violoncelles et bassons à l’unisson", "Tutti", m21.clef.TrebleClef(), transpose=12, dyn=[(1, 'pp')], fix=fix_open)
# NMA slurs: bar1 notes 0-4, bar2 all (0-7), bar3 0-4, bar4 0-7, bar5 0-4?, bar6 0-7
try: add_slurs(vl, [(1,0,1,4),(2,0,2,7),(3,0,3,4),(4,0,4,7),(5,0,5,7),(6,0,6,7)])
except Exception as e: print("slur warn", e)
sc = m21.stream.Score(); sc.insert(0, vl); _render(sc, OUT, "ouverture_1_7", 42)
