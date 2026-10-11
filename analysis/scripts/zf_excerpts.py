import sys, music21 as m21, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent)); from engrave_common import render, add_dyn
MIDS = sys.argv[1]; OUT = sys.argv[2]
def load(name): return m21.converter.parse(f"{MIDS}/{name}.mid", quantizePost=True)
def part_of(score, key):
    for p in score.parts:
        if p.partName.startswith(key): return p
    raise KeyError(key)
def slice_part(p, m0, m1, base, label, abbrev, clef, ts='cut', dyn=None):
    new = m21.stream.Part(); new.partName = label; new.partAbbreviation = abbrev
    new.insert(0, clef); new.insert(0, m21.key.KeySignature(-3)); new.insert(0, m21.meter.TimeSignature(ts))
    for m in p.getElementsByClass(m21.stream.Measure):
        if m0 <= m.number <= m1:
            mm = m21.stream.Measure(number=m.number + base - 1)
            for e in m.notesAndRests:
                e2 = e.__deepcopy__()
                if e2.isNote or e2.isChord: e2.stemDirection = 'unspecified'
                mm.insert(e.offset, e2)
            new.append(mm)
    if dyn: add_dyn(new, dyn)
    return new
# Z2 fugato 16-27
alg = load("allegroIscore")
vl1 = slice_part(part_of(alg, "violino1"), 1, 12, 16, "Violon I", "Vl. I", m21.clef.TrebleClef(), dyn=[(20, 'p')])
vl2 = slice_part(part_of(alg, "violino2"), 1, 12, 16, "Violon II", "Vl. II", m21.clef.TrebleClef(), dyn=[(16, 'p')])
va = slice_part(part_of(alg, "viola"), 1, 12, 16, "Alto", "Va.", m21.clef.AltoClef(), dyn=[(27, 'p')])
vc = slice_part(part_of(alg, "violoncello"), 1, 12, 16, "Violoncelle", "Vc.", m21.clef.BassClef(), dyn=[(27, 'p')])
sc = m21.stream.Score(); [sc.insert(0, p) for p in (vl1, vl2, va, vc)]
render(sc, OUT, "fugato_16_27", 34)
# Z1 Adagio 1-3 (strings) with bar 3 of Vl I rebuilt (quarter rest with fermata, dotted-eighth rest, 32nd triplet)
ada = load("adagioIscore")
parts = []
for key, lab, ab, cl in [("violino1","Violon I","Vl. I",m21.clef.TrebleClef()),("violino2","Violon II","Vl. II",m21.clef.TrebleClef()),("viola","Alto","Va.",m21.clef.AltoClef()),("violoncello","Violoncelle et contrebasse","Vc. Cb.",m21.clef.BassClef())]:
    parts.append(slice_part(part_of(ada, key), 1, 3, 1, lab, ab, cl, ts='common', dyn=[(1,'f')]))
m3 = [m for m in parts[0].getElementsByClass(m21.stream.Measure) if m.number == 3][0]
for e in list(m3.notesAndRests): m3.remove(e)
ch = m21.chord.Chord(["B-4", "B-5"], quarterLength=2.0); m3.insert(0, ch)
r1 = m21.note.Rest(quarterLength=1.0); r1.expressions.append(m21.expressions.Fermata()); m3.insert(2.0, r1)
m3.insert(3.0, m21.note.Rest(quarterLength=0.75))
trip = []
for i, pn in enumerate(["B-5", "A-5", "G5"]):
    n = m21.note.Note(pn, quarterLength=0.125); n.duration.appendTuplet(m21.duration.Tuplet(3, 2, '32nd')); m3.insert(3.75 + i * (0.25/3), n); trip.append(n)
m3.insert(3.75, m21.dynamics.Dynamic('p')); parts[0].insert(0, m21.spanner.Slur(trip[0], trip[-1]))
for p in parts[1:]:
    mm = [m for m in p.getElementsByClass(m21.stream.Measure) if m.number == 3][0]
    for e in list(mm.notesAndRests):
        if e.isRest and e.offset >= 2.0: mm.remove(e)
    r = m21.note.Rest(quarterLength=1.0); r.expressions.append(m21.expressions.Fermata()); mm.insert(2.0, r); mm.insert(3.0, m21.note.Rest(quarterLength=1.0))
for p in parts:
    for mm in p.getElementsByClass(m21.stream.Measure):
        for e in list(mm.notesAndRests):
            if e.isRest and e.quarterLength == 1.75:
                off = e.offset; mm.remove(e); mm.insert(off, m21.note.Rest(quarterLength=1.0)); mm.insert(off + 1.0, m21.note.Rest(quarterLength=0.75))
sc = m21.stream.Score(); [sc.insert(0, p) for p in parts]
render(sc, OUT, "adagio_1_3", 38)
# Z3 the threefold chord 97-102: oboes, trombones, bassoons (from the Adagio II file)
ad2 = load("adagioIIscore")
ob = slice_part(part_of(ad2, "oboi"), 1, 6, 97, "Hautbois", "Ob.", m21.clef.TrebleClef(), ts='common', dyn=[(97,'f')])
tb = slice_part(part_of(ad2, "trombone"), 1, 6, 97, "Trombones", "Trb.", m21.clef.BassClef(), ts='common')
fg = slice_part(part_of(ad2, "fagotti"), 1, 6, 97, "Bassons", "Fag.", m21.clef.BassClef(), ts='common')
for p in (ob, tb, fg):
    for mm in p.getElementsByClass(m21.stream.Measure):
        for e in list(mm.notesAndRests):
            if e.isRest and e.quarterLength == 1.75:
                off = e.offset; mm.remove(e); mm.insert(off, m21.note.Rest(quarterLength=1.0)); mm.insert(off + 1.0, m21.note.Rest(quarterLength=0.75))
sc = m21.stream.Score(); [sc.insert(0, p) for p in (ob, tb, fg)]
render(sc, OUT, "trois_accords_97_102", 38)
print("== adagio II rhythm (oboi):")
for m in ob.getElementsByClass(m21.stream.Measure): print(m.number, " ".join((f"{e.pitches[0].nameWithOctave if e.isChord else e.nameWithOctave}{e.quarterLength:g}" if not e.isRest else f"r{e.quarterLength:g}") for e in m.notesAndRests))
