"""Build the rehearsal guide site (index + A4 handouts) from out/final.json.

Usage: python -I build_site.py <final.json> <site_dir>
final.json keys: guide_markdown, handouts[{id,title,audience,markdown}], sources_used[],
                 excerpts{"work/id": {title,start_bar,end_bar,parts,svg_path}}, method_note (md)
"""
import json, re, sys, html, pathlib
import markdown

FINAL = pathlib.Path(sys.argv[1])
SITE = pathlib.Path(sys.argv[2])
(SITE / "fiches").mkdir(parents=True, exist_ok=True)
data = json.loads(FINAL.read_text(encoding="utf-8"))
EXC = data.get("excerpts", {})

FONTS = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&family=IBM+Plex+Mono:wght@400;500&display=swap">'

# ---------- design tokens / base css ----------
BASE_CSS = """
/* Layout: a conductor's-score margin — rehearsal-letter rail on the left, 68ch reading column, bar numbers as mono chips. */
:root{
  --bg:#F5F6F8; --surface:#FFFFFF; --ink:#16181D; --muted:#5B6270; --line:#D9DDE3;
  --accent:#1E4D7B; --accent-soft:#E4EDF6; --mark:#A3302A; --mark-soft:#F6E6E4; --ok:#2E6B3F; --ok-soft:#E3EFE6;
  --display:"Cormorant Garamond",Garamond,"Times New Roman",serif;
  --body:"Source Serif 4",Georgia,"Times New Roman",serif;
  --mono:"IBM Plex Mono",Consolas,"Courier New",monospace;
}
@media (prefers-color-scheme: dark){ :root:not([data-theme="light"]){
  --bg:#15181D; --surface:#1C2027; --ink:#E8EAEE; --muted:#9AA3B0; --line:#2F353E;
  --accent:#8FBCEB; --accent-soft:#1F2E40; --mark:#E8857A; --mark-soft:#3A2321; --ok:#8CCB9B; --ok-soft:#1F3326; color-scheme:dark } }
:root[data-theme="dark"]{
  --bg:#15181D; --surface:#1C2027; --ink:#E8EAEE; --muted:#9AA3B0; --line:#2F353E;
  --accent:#8FBCEB; --accent-soft:#1F2E40; --mark:#E8857A; --mark-soft:#3A2321; --ok:#8CCB9B; --ok-soft:#1F3326; color-scheme:dark }
*{box-sizing:border-box}
body{background:var(--bg);color:var(--ink);font-family:var(--body);font-size:17px;line-height:1.55;margin:0}
a{color:var(--accent)} a:focus-visible,button:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
h1,h2,h3,h4{font-family:var(--display);line-height:1.15;text-wrap:balance;margin:0}
h1{font-size:clamp(2.1rem,5vw,3.4rem);font-weight:600}
h2{font-size:clamp(1.65rem,3.2vw,2.3rem);font-weight:600;margin-block:2.6rem .9rem;padding-top:1.2rem;border-top:1px solid var(--line)}
h3{font-size:1.4rem;font-weight:600;margin-block:1.8rem .5rem}
h4{font-size:1.12rem;font-weight:700;font-family:var(--body);margin-block:1.3rem .35rem}
p{margin-block:0 .9rem} ul,ol{margin-block:0 .9rem;padding-inline-start:1.4rem} li{margin-block:.22rem}
li>p{margin-block:0 .3rem}
strong{font-weight:600}
blockquote{margin:1rem 0;padding:.6rem 1rem;border-inline-start:3px solid var(--accent);background:var(--accent-soft);border-radius:0 6px 6px 0}
blockquote p:last-child{margin:0}
code{font-family:var(--mono);font-size:.88em;background:var(--accent-soft);padding:.05em .35em;border-radius:4px}
hr{border:0;border-top:1px solid var(--line);margin:2rem 0}
.eyebrow{font-family:var(--mono);font-size:.74rem;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
.bar{font-family:var(--mono);font-size:.82em;white-space:nowrap;background:var(--accent-soft);color:var(--accent);padding:.08em .4em;border-radius:4px;font-variant-numeric:tabular-nums}
.tbl{overflow-x:auto;margin-block:.6rem 1.2rem;border:1px solid var(--line);border-radius:8px;background:var(--surface)}
table{border-collapse:collapse;width:100%;font-size:.95rem;min-width:520px}
th,td{padding:.55rem .7rem;border-bottom:1px solid var(--line);vertical-align:top;text-align:left}
th{font-family:var(--mono);font-size:.74rem;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:500;background:var(--bg)}
tr:last-child td{border-bottom:0}
td:first-child{font-variant-numeric:tabular-nums}
figure.excerpt{margin:1.2rem 0 1.6rem;background:#fff;border:1px solid var(--line);border-radius:8px;padding:.6rem .6rem .2rem;overflow-x:auto}
figure.excerpt svg{width:100%;height:auto;display:block;min-width:min(100%,520px)}
figure.excerpt figcaption{font-family:var(--mono);font-size:.78rem;color:#4b5563;padding:.45rem .3rem .4rem;border-top:1px solid #e5e7eb;margin-top:.4rem}
figure.excerpt figcaption b{font-weight:500;color:#1E4D7B}
.callout{border:1px solid var(--line);border-radius:8px;padding:.9rem 1.1rem;background:var(--surface);margin:1rem 0}
.callout.mark{border-color:var(--mark);background:var(--mark-soft)}
.callout.ok{border-color:var(--ok);background:var(--ok-soft)}
.timeline{margin:1rem 0 1.4rem}
.timeline .ruler{position:relative;height:1.3rem;font-family:var(--mono);font-size:.72rem;color:var(--muted)}
.timeline .ruler span{position:absolute;transform:translateX(-50%)}
.timeline .track{display:flex;height:2.6rem;border-radius:6px;overflow:hidden;border:1px solid var(--line)}
.timeline .blk{display:flex;align-items:center;justify-content:center;font-family:var(--mono);font-size:.72rem;padding:0 .3rem;overflow:hidden;white-space:nowrap;text-overflow:ellipsis;background:var(--accent-soft);color:var(--ink);border-inline-end:1px solid var(--surface)}
.timeline .blk.pause{background:var(--bg);color:var(--muted)} .timeline .blk.figaro{background:var(--accent-soft)} .timeline .blk.flute{background:var(--ok-soft)} .timeline .blk.filage{background:var(--mark-soft)}
"""

INDEX_CSS = BASE_CSS + """
.wrap{max-width:1180px;margin:0 auto;padding-inline:16px;padding-block:0 4rem}
header.hero{padding-block:2.4rem 1.6rem;border-bottom:1px solid var(--line);margin-bottom:1rem}
header.hero .meta{display:flex;flex-wrap:wrap;gap:.5rem 1.4rem;margin-top:1rem;font-family:var(--mono);font-size:.8rem;color:var(--muted)}
header.hero p.lede{font-size:1.15rem;max-width:62ch;margin-top:1rem;color:var(--muted)}
.grid{display:grid;grid-template-columns:1fr;gap:2rem}
@media (min-width:1000px){.grid{grid-template-columns:200px minmax(0,1fr)}}
nav.rail{position:sticky;top:env(safe-area-inset-top,0px);align-self:start;max-height:100vh;overflow:auto;padding-block:1rem;display:none}
@media (min-width:1000px){nav.rail{display:block}}
nav.rail a{display:flex;gap:.6rem;align-items:baseline;text-decoration:none;color:var(--muted);padding:.3rem .2rem;font-size:.9rem;border-inline-start:2px solid transparent}
nav.rail a:hover{color:var(--ink)} nav.rail a b{font-family:var(--mono);font-weight:500;color:var(--accent);min-width:1.2em}
nav.top{display:flex;gap:.4rem;overflow-x:auto;padding-block:.6rem;margin-bottom:.5rem;font-family:var(--mono);font-size:.74rem}
@media (min-width:1000px){nav.top{display:none}}
nav.top a{white-space:nowrap;text-decoration:none;color:var(--accent);background:var(--accent-soft);padding:.25rem .55rem;border-radius:999px}
main{min-width:0;max-width:74ch}
main h2 .letter{font-family:var(--mono);font-size:.95rem;font-weight:500;color:var(--accent);margin-inline-end:.7rem;vertical-align:.35em;letter-spacing:.05em}
.fiches{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:.9rem;margin-block:1rem 1.6rem}
.fiches a{display:block;text-decoration:none;color:var(--ink);background:var(--surface);border:1px solid var(--line);border-radius:8px;padding:.9rem 1rem}
.fiches a:hover{border-color:var(--accent)}
.fiches a .t{font-family:var(--display);font-size:1.25rem;font-weight:600;line-height:1.15}
.fiches a .a{font-family:var(--mono);font-size:.72rem;color:var(--muted);margin-top:.4rem;letter-spacing:.06em;text-transform:uppercase}
footer{margin-top:3rem;padding-top:1rem;border-top:1px solid var(--line);font-size:.85rem;color:var(--muted)}
@media print{ nav.rail,nav.top,.fiches{display:none!important} body{background:#fff;color:#000;font-size:11.5pt} .wrap{max-width:none;padding:0} h2{break-before:page;border:0} h2:first-of-type{break-before:auto} figure.excerpt{break-inside:avoid} .tbl{break-inside:avoid;border:0} table{min-width:0} }
"""

FICHE_CSS = BASE_CSS + """
@page{size:A4;margin:14mm 15mm}
.sheet{max-width:820px;margin:0 auto;padding-inline:16px;padding-block:1.6rem 3rem}
.head{display:flex;flex-wrap:wrap;justify-content:space-between;gap:.4rem 1rem;align-items:baseline;border-bottom:2px solid var(--ink);padding-bottom:.6rem;margin-bottom:1rem}
.head .prog{font-family:var(--mono);font-size:.74rem;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
h1{font-size:clamp(1.8rem,4vw,2.5rem)}
.aud{font-family:var(--mono);font-size:.78rem;color:var(--muted);margin-bottom:1.2rem}
.sheet h2{font-size:1.45rem;margin-block:1.5rem .5rem;padding-top:.6rem}
.sheet h3{font-size:1.15rem}
.back{font-family:var(--mono);font-size:.76rem;margin-bottom:1rem;display:inline-block}
.sheet .legend{font-family:var(--mono);font-size:.76rem;color:var(--muted);border:1px dashed var(--line);padding:.5rem .7rem;border-radius:6px;margin:.6rem 0 1rem}
footer{margin-top:2rem;font-family:var(--mono);font-size:.72rem;color:var(--muted);border-top:1px solid var(--line);padding-top:.5rem}
@media print{ body{background:#fff;color:#000;font-size:10.5pt;line-height:1.4} .sheet{max-width:none;padding:0} .back{display:none} figure.excerpt{break-inside:avoid;border-color:#bbb} .tbl{border:0;break-inside:avoid} table{min-width:0;font-size:9.5pt} th{background:#f2f2f2;color:#333} .bar{background:#eee;color:#000} blockquote{background:#f4f4f4;border-color:#333} .callout.mark{background:#f7eceb} h2{break-after:avoid} h3{break-after:avoid} ul,ol{break-inside:auto} li{break-inside:avoid} }
"""

# ---------- helpers ----------
def typo(md: str) -> str:
    """French typography: narrow no-break spaces before ; ? ! and no-break before : and inside « »."""
    out = []
    in_code = False
    for line in md.split("\n"):
        if line.strip().startswith("```"):
            in_code = not in_code; out.append(line); continue
        if in_code or line.strip().startswith("|"):
            # tables: only fix guillemets, keep pipes/colons intact
            line = re.sub(r"«\s", "« ", line); line = re.sub(r"\s»", " »", line)
            out.append(line); continue
        line = re.sub(r"(?<=\S) ([;?!])", " \\1", line)
        line = re.sub(r"(?<=[^\s:|]) :(?=\s|$)", " :", line)
        line = re.sub(r"«\s", "« ", line); line = re.sub(r"\s»", " »", line)
        out.append(line)
    return "\n".join(out)

BAR_RE = re.compile(r"\b(?:mes\.|mesures?|m\.)\s?(\d{1,3})(?:\s?[–-]\s?(\d{1,3}))?(?![\d-])")
def bars(md: str) -> str:
    def rep(m):
        a, b = m.group(1), m.group(2)
        label = f"mes. {a}" + (f"–{b}" if b else "")
        return f'<span class="bar">{label}</span>'
    out, in_code = [], False
    for line in md.split("\n"):
        if line.strip().startswith("```"): in_code = not in_code
        if in_code or line.startswith("#"): out.append(line); continue
        out.append(BAR_RE.sub(rep, line))
    return "\n".join(out)

def svg_inline(path: str) -> str:
    s = pathlib.Path(path).read_text(encoding="utf-8")
    s = s[s.index("<svg"):]
    # drop fixed px size on root, keep viewBox
    s = re.sub(r'^<svg([^>]*?)\swidth="[^"]*"', r'<svg\1', s, count=1)
    s = re.sub(r'^<svg([^>]*?)\sheight="[^"]*"', r'<svg\1', s, count=1)
    s = re.sub(r'<\?xml[^>]*\?>', '', s)
    return s

EXC_RE = re.compile(r"^\s*\[\[excerpt:([\w-]+)/([\w-]+)\]\]\s*$", re.M)
def excerpts(md: str) -> str:
    def rep(m):
        key = f"{m.group(1)}/{m.group(2)}"
        meta = EXC.get(key)
        if not meta or not pathlib.Path(meta["svg_path"]).exists():
            return ""
        cap = f'<b>{html.escape(meta["title"])}</b> · mes. {meta["start_bar"]}–{meta["end_bar"]} · {html.escape(meta.get("parts",""))}'
        return f'\n<figure class="excerpt">{svg_inline(meta["svg_path"])}<figcaption>{cap}</figcaption></figure>\n'
    return EXC_RE.sub(rep, md)

def convert(md: str) -> str:
    md = excerpts(bars(typo(md)))
    h = markdown.markdown(md, extensions=["tables", "sane_lists", "attr_list", "md_in_html"], output_format="html5")
    h = re.sub(r"<table>", '<div class="tbl"><table>', h); h = re.sub(r"</table>", "</table></div>", h)
    return h

TIME_RE = re.compile(r"(\d{1,2})\s?h\s?(\d{2})?")
def timeline_from(md: str) -> str:
    """Build a to-scale 9h–13h timeline from the first table whose first column holds time ranges."""
    rows = []
    for line in md.split("\n"):
        if not line.strip().startswith("|"): continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2: continue
        ts = TIME_RE.findall(cells[0])
        if len(ts) >= 2:
            t0 = int(ts[0][0]) * 60 + int(ts[0][1] or 0); t1 = int(ts[1][0]) * 60 + int(ts[1][1] or 0)
            if 8 * 60 <= t0 < t1 <= 14 * 60:
                rows.append((t0, t1, re.sub(r"\*+|`", "", cells[1])))
    if len(rows) < 3: return ""
    start, end = min(r[0] for r in rows), max(r[1] for r in rows)
    total = end - start
    blocks = []
    for t0, t1, label in rows:
        w = (t1 - t0) / total * 100
        low = label.lower()
        cls = "pause" if "pause" in low else "figaro" if "figaro" in low else "flute" if ("flûte" in low or "flute" in low) else "filage" if ("filage" in low or "reprise" in low) else ""
        short = re.sub(r"[.:(].*$", "", label).strip()
        blocks.append(f'<div class="blk {cls}" style="width:{w:.2f}%" title="{html.escape(label)}">{html.escape(short)}</div>')
    ticks = "".join(f'<span style="left:{(t-start)/total*100:.1f}%">{t//60}h{"%02d"%(t%60) if t%60 else ""}</span>' for t in range(start, end + 1, 60))
    return f'<div class="timeline" aria-label="Déroulé à l’échelle"><div class="ruler">{ticks}</div><div class="track">{"".join(blocks)}</div></div>'

def add_letters(h: str):
    """Give each h2 a rehearsal letter + id; return (html, toc)."""
    toc = []
    letters = "ABCDEFGHJKLMNPQRSTUVWXYZ"  # orchestral convention skips I and O
    i = 0
    def rep(m):
        nonlocal i
        title = re.sub(r"<[^>]+>", "", m.group(1))
        slug = re.sub(r"[^a-z0-9]+", "-", title.lower().translate(str.maketrans("àâäéèêëîïôöùûüç’'", "aaaeeeeiioouuuc  "))).strip("-")[:40]
        L = letters[i]; i += 1
        toc.append((L, slug, title))
        return f'<h2 id="{slug}"><span class="letter">{L}</span>{m.group(1)}</h2>'
    h = re.sub(r"<h2>(.*?)</h2>", rep, h, flags=re.S)
    return h, toc

# ---------- handouts ----------
PROG = "Mozart — Ouvertures des Noces de Figaro (K. 492) et de La Flûte enchantée (K. 620)"
fiches_index = []
for hd in data["handouts"]:
    body = convert(hd["markdown"])
    body = re.sub(r"^<h1>.*?</h1>\s*", "", body, count=1, flags=re.S)
    page = f"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{html.escape(hd['title'])}</title>{FONTS}<style>{FICHE_CSS}</style></head>
<body><div class="sheet">
<a class="back" href="../index.html">← Retour au guide</a>
<div class="head"><h1>{html.escape(hd['title'])}</h1><div class="prog">{html.escape(PROG)}</div></div>
<div class="aud">Destinataires : {html.escape(hd['audience'])}</div>
{body}
<footer>Répétition du matin, 9h00–13h00 · Direction depuis le premier violon : Nina Ramousse · Numéros de mesure conformes à la partition (NMA / éditions de référence).</footer>
</div></body></html>"""
    (SITE / "fiches" / f"{hd['id']}.html").write_text(page, encoding="utf-8")
    fiches_index.append(hd)

# ---------- index ----------
guide_html = convert(data["guide_markdown"])
guide_html = re.sub(r"^<h1>.*?</h1>\s*", "", guide_html, count=1, flags=re.S)
guide_html, toc = add_letters(guide_html)
tl = timeline_from(data["guide_markdown"])
if tl:
    # place the timeline right after the "Déroulé" heading
    guide_html = re.sub(r'(<h2 id="[^"]*deroule[^"]*">.*?</h2>)', r"\1" + tl.replace("\\", "\\\\"), guide_html, count=1, flags=re.S)

PDF_LINKS = ""
if "--pdf-links" in sys.argv:
    PDF_LINKS = ('<div class="callout" style="margin-top:1rem"><div class="eyebrow">Versions imprimables (PDF, A4)</div>'
                 '<p style="margin:.4rem 0 0"><a href="pdf/Guide%20de%20repetition%20-%20Nina%20Ramousse.pdf">Le guide complet</a> · '
                 '<a href="pdf/Dossier%20musiciens%20-%20toutes%20les%20fiches.pdf">Les sept fiches en un seul dossier</a></p></div>')
fiches_cards = "".join(
    f'<a href="fiches/{hd["id"]}.html"><div class="t">{html.escape(hd["title"])}</div><div class="a">{html.escape(hd["audience"])}</div></a>'
    for hd in fiches_index)
rail = "".join(f'<a href="#{slug}"><b>{L}</b><span>{html.escape(t)}</span></a>' for L, slug, t in toc)
top = "".join(f'<a href="#{slug}">{L} · {html.escape(t[:22])}</a>' for L, slug, t in toc)
method = convert(data.get("method_note", ""))

index = f"""<title>Guide de répétition Mozart</title>
{FONTS}
<style>{INDEX_CSS}</style>
<div class="wrap">
<header class="hero">
  <div class="eyebrow">Répétition d’orchestre · 9h00–13h00 · direction depuis le premier violon</div>
  <h1>Figaro &amp; La Flûte enchantée</h1>
  <p class="lede">Guide de répétition préparé pour Nina Ramousse : plan des quatre heures, passages prioritaires mesure par mesure, méthode de justesse, esthétique classique, et les fiches à distribuer aux musiciens.</p>
  <div class="meta"><span>W. A. Mozart</span><span>Ouverture des Noces de Figaro, K. 492 — ré majeur, Presto</span><span>Ouverture de La Flûte enchantée, K. 620 — mi♭ majeur, Adagio–Allegro</span></div>
</header>
<nav class="top" aria-label="Sections">{top}<a href="#fiches">Fiches</a></nav>
<div class="grid">
<nav class="rail" aria-label="Sections"><div class="eyebrow" style="margin-bottom:.5rem">Repères</div>{rail}<a href="#fiches"><b>✦</b><span>Fiches musiciens</span></a></nav>
<main>
<section id="fiches">
<div class="eyebrow">Documents à distribuer</div>
<div class="fiches">{fiches_cards}</div>
{PDF_LINKS}
</section>
{guide_html}
<h2 id="methode"><span class="letter">∞</span>Méthode et vérification</h2>
{method}
<footer>Préparé le 11 octobre 2026. Extraits gravés avec Verovio à partir d’encodages vérifiés sur la partition imprimée ; analyse structurelle music21. Les numéros de mesure marqués « à vérifier » n’ont pas pu être confirmés sur la partition et doivent être contrôlés sur le matériel de l’orchestre.</footer>
</main>
</div>
</div>
"""
(SITE / "index.html").write_text(index, encoding="utf-8")
print("built", SITE / "index.html", "+", len(fiches_index), "fiches;", "timeline:", bool(tl), "; toc:", [t[0] + " " + t[2] for t in toc])
