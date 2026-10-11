import sys, music21 as m21
base = sys.argv[1]
for name in ["adagioIscore","allegroIscore","adagioIIscore","allegroIIscore","MFO-Score"]:
    try:
        s = m21.converter.parse(f"{base}/{name}.mid", quantizePost=True)
    except Exception as e:
        print(name, "ERR", e); continue
    parts = s.parts
    p0 = parts[0]
    ms = p0.getElementsByClass(m21.stream.Measure)
    ts = [(m.number, m.timeSignature.ratioString) for m in ms if m.timeSignature is not None]
    mm = [(e.offset, e.number) for e in s.flatten().getElementsByClass(m21.tempo.MetronomeMark)]
    print(f"{name}: parts={len(parts)} measures={len(ms)} first={ms[0].number if ms else None} last={ms[-1].number if ms else None} ts={ts[:6]} tempi={mm[:6]}")
    print("   part names:", [p.partName for p in parts][:20])
