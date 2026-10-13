# Figaro & La Flûte enchantée — guide de répétition

Guide de répétition préparé pour Nina Ramousse, qui dirige depuis le premier violon une répétition d’orchestre d’étudiants (9h00–13h00, Lyon) consacrée à deux ouvertures de Mozart : *Les Noces de Figaro* (K. 492) et *La Flûte enchantée* (K. 620).

**Lire le guide en ligne :** https://decarvalhoe.github.io/mozart-ouvertures-repetition/

## Contenu

- `docs/` — le site publié (GitHub Pages) : le guide complet et les sept fiches à distribuer aux musiciens (plan de la répétition, cordes *Figaro*, cordes *Flûte*, vents–cuivres–timbales, style classique, justesse, écoutes), plus la page « Programmes de concert » (cinq combinaisons d’une demi-heure pour orchestre réduit autour de la Pavane de Ravel et de Tico-Tico) et les versions PDF A4 dans `docs/pdf/`.
- `analysis/` — ce qui a servi à produire le guide : le contenu structuré (`final.json`), les extraits gravés (`excerpts/`, SVG et MusicXML, rendus avec Verovio) et les scripts Python (music21, Verovio, export PDF).

## Méthode

Les numéros de mesure de *Figaro* ont été relevés page par page sur la partition de la Neue Mozart-Ausgabe (NMA II/5/16, Sinfonia) ; les hauteurs de l’extrait initial ont été contrôlées sur deux encodages indépendants. Pour *La Flûte enchantée*, la structure (Adagio 1–15, Allegro 16–96, Adagio 97–102, Allegro 103–226) et les entrées du sujet ont été extraites par analyse automatique (music21) de l’édition encodée du Mutopia Project (d’après C. F. Peters), cohérente avec le compte de la NMA ; ces numéros sont à confirmer sur le matériel de l’orchestre.

## Reproduire

```bash
python -m venv av && av/Scripts/python -m pip install music21 verovio markdown pymupdf
av/Scripts/python analysis/scripts/content.py out/final.json
av/Scripts/python analysis/scripts/build_site.py out/final.json site --pdf-links
av/Scripts/python analysis/scripts/export_pdfs.py site out/pdf   # Microsoft Edge en mode headless
```

Les scripts de gravure (`fig_excerpts.py`, `zf_excerpts.py`) attendent les encodages sources (MIDI) qui ne sont pas redistribués ici.

## Licence

Textes et fiches : CC BY 4.0. Scripts : MIT. Les œuvres de Mozart sont dans le domaine public ; les extraits ont été gravés pour ce guide.
