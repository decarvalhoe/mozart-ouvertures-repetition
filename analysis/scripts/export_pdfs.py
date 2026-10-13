"""Export the built site to PDF with headless Edge, then merge the handouts into one dossier.

Usage: python -I export_pdfs.py <site_dir> <pdf_dir>
"""
import subprocess, sys, pathlib, time, json
import fitz  # pymupdf

SITE = pathlib.Path(sys.argv[1]).resolve()
PDF = pathlib.Path(sys.argv[2]).resolve(); PDF.mkdir(parents=True, exist_ok=True)
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

def to_pdf(html_path: pathlib.Path, out: pathlib.Path):
    url = "file:///" + str(html_path).replace("\\", "/")
    subprocess.run([EDGE, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    "--run-all-compositor-stages-before-draw", "--virtual-time-budget=8000",
                    f"--print-to-pdf={out}", url], check=False, timeout=120,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for _ in range(40):
        if out.exists() and out.stat().st_size > 1000: return True
        time.sleep(0.5)
    return False

# the index is published without a doctype wrapper; wrap a copy for printing
idx = (SITE / "index.html").read_text(encoding="utf-8")
wrapped = SITE / "_print_index.html"
wrapped.write_text('<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
                   '<style>@page{size:A4;margin:14mm 15mm}</style></head><body>' + idx + '</body></html>', encoding="utf-8")
ok = to_pdf(wrapped, PDF / "Guide de repetition - Nina Ramousse.pdf")
print("guide pdf:", ok)
wrapped.unlink(missing_ok=True)

if (SITE / "programmes.html").exists():
    print("programmes pdf:", to_pdf(SITE / "programmes.html", PDF / "Programmes de concert - combinaisons.pdf"))

order = json.loads((SITE / "fiches_order.json").read_text(encoding="utf-8")) if (SITE / "fiches_order.json").exists() else None
fiches = sorted((SITE / "fiches").glob("*.html"))
if order:
    fiches = [SITE / "fiches" / f"{i}.html" for i in order if (SITE / "fiches" / f"{i}.html").exists()]
made = []
for f in fiches:
    out = PDF / f"Fiche - {f.stem}.pdf"
    if to_pdf(f, out): made.append(out); print("fiche pdf:", f.stem)
    else: print("FAILED:", f.stem)

if made:
    doc = fitz.open()
    for p in made:
        with fitz.open(p) as src: doc.insert_pdf(src)
    doc.save(PDF / "Dossier musiciens - toutes les fiches.pdf"); doc.close()
    print("dossier pages:", sum(len(fitz.open(p)) for p in made))
