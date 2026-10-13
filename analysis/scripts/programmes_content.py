# -*- coding: utf-8 -*-
"""Ajoute la page « Programmes de concert » à out/final.json."""
import json, pathlib, sys
OUT = pathlib.Path(sys.argv[1])
data = json.loads(OUT.read_text(encoding="utf-8"))

md = r"""
## Le cahier des charges

- **Durée** : 30 minutes de musique (28 à 32 min), en quatre ou cinq œuvres courtes.
- **Effectif de base** (« orchestre Mozart ») : 2 flûtes, 2 hautbois, 2 clarinettes, 2 bassons, 2 cors, harpe (ou piano), cordes. Tout ce qui suit tient dans cet effectif ; les rares ajouts (trompettes, timbales, percussion) sont signalés et ne concernent que des pièces optionnelles.
- **Niveau** : accessible à un orchestre d’étudiants, sans chef, dirigé depuis le premier violon. Les niveaux indiqués vont de ● (facile) à ●●● (exigeant). Aucune œuvre ●●● n’est retenue.
- **Matériel** : toutes les œuvres sont dans le domaine public dans l’Union européenne et leur conducteur et leurs parties sont téléchargeables sur IMSLP (vérifier qu’il s’agit bien de l’édition d’orchestre, et non d’une réduction pour piano).
- **Pas de baroque** : ni Bach, ni Haendel, ni Vivaldi, et pas non plus de suites « dans le style ancien » (la *Suite Holberg* de Grieg, les *Antiche danze* de Respighi sont écartées des programmes pour cette raison).
- **Deux pièces demandées** : Ravel, *Pavane pour une infante défunte* (version d’orchestre de 1910) et Zequinha de Abreu, *Tico-Tico no Fubá* (version orchestre).

## La Pavane de Ravel, pièce fixe

| | |
|---|---|
| Durée | ≈ 6 min 30 |
| Effectif | 2 flûtes, 1 hautbois, 2 clarinettes, 2 bassons, 2 cors, harpe, cordes |
| Niveau | ●● : lent (noire ≈ 54), mais exposé ; le thème initial est au **cor solo** (douze mesures seul avec les cordes en pizzicato), puis repris par les bois |
| Direction depuis le violon | Oui. Le cor solo donne le ton ; convenir que Nina donne la levée et que le corniste respire avec elle. Les cordes ne doivent pas vibrer en continu : son droit, archet lent |
| Harpe | Indispensable à la couleur, mais la partie se joue au piano sans dommage (c’est courant) |
| Matériel | IMSLP, édition Eschig (1910), domaine public |
| Pièges | La justesse des bois dans les enchaînements chromatiques ; les pizzicati des cordes (ensemble et sonorité) ; ne pas ralentir davantage que l’écrit |

## Tico-Tico no Fubá, la pièce qui ferme le concert

| | |
|---|---|
| Œuvre | Zequinha de Abreu (1880–1935), *Tico-Tico no Fubá*, choro, 1917. Domaine public dans l’Union européenne depuis 2006 (l’original pour piano est sur IMSLP) |
| Durée | ≈ 3 min (2 min 30 à 3 min 30 selon les reprises) |
| Niveau | ●● : tempo vif (noire ≈ 120–130 à 2/4), doubles croches continues à la mélodie ; on la répartit entre bois et violons pour que personne ne la tienne trois minutes |
| Direction depuis le violon | Oui, à condition d’un tempo fixé d’avance et tenu par les basses et la percussion ; pas de rubato |
| Effectif | Effectif de base + percussion légère (maracas ou pandeiro, caisse claire avec balais) ; piano bienvenu |
| **Matériel, trois options** | **1.** Arrangement pour orchestre à cordes de James Kazik (Hal Leonard, 2023, niveau intermédiaire, avec piano et percussion facultatifs) : le plus simple à obtenir, les vents doublent ou se taisent. **2.** Arrangement pour orchestre symphonique de Francesco Traversi (Sheet Music Direct / ArrangeMe) : à examiner avant achat, effectif plus large. **3.** Arrangement maison pour l’effectif de base, réalisé à partir de la partition de piano libre de droits : mélodie aux bois puis aux violons, accompagnement de choro aux cordes graves et à la percussion. Sur IMSLP, les arrangements existants (trios d’anches, duos de cuivres, violon et piano) sont sous licence Creative Commons, mais aucun n’est pour orchestre |
| Place dans le concert | En finale ou en bis : après elle, on ne peut plus rien jouer |

## Catalogue des œuvres compatibles

### Cordes seules (toute la section joue, les vents se reposent)

| Œuvre | Durée | Niveau | Remarques |
|---|---|---|---|
| Bizet, *L’Arlésienne*, Adagietto | 3 min | ● | Sourdines, pp, phrasé long. Idéal en ouverture douce ou avant Ravel |
| Massenet, *Le dernier sommeil de la Vierge* | 4 min | ● | Même famille que l’Adagietto ; très simple, très beau |
| Grieg, *Deux mélodies élégiaques* op. 34 : *Le dernier printemps* | 5 min | ● | La pièce de cordes la plus sûre du répertoire |
| Grieg, *Deux mélodies élégiaques* op. 34 : *Blessure du cœur* | 4 min | ● | Fait la paire avec la précédente (9 min à deux) |
| Grieg, *Suite Holberg* op. 40 | 20 min, ou par mouvements | ●● | Mentionnée pour mémoire : écrite « dans le style ancien » (prélude, sarabande, gavotte, air, rigaudon), elle sonne baroque et n’entre dans aucun des programmes ci-dessous |
| Holst, *St Paul’s Suite* | 12 min | ●● | Écrite pour un orchestre d’école ; Jig, Ostinato, Intermezzo (solo de violon), Finale sur *Greensleeves* |
| Holst, *Brook Green Suite* | 7 min | ● | Prelude, Air, Dance ; encore plus simple que la précédente |
| Elgar, *Serenade pour cordes* op. 20 | 12 min | ●● | Trois mouvements ; le Larghetto (6 min) peut être donné seul |
| Mozart, Divertimento K. 136 | 13 min | ●● | Allegro 6 min, Andante 4 min 30, Presto 3 min ; tempo vif à tenir |
| Schubert, *Cinq danses allemandes* D. 90 | 8 min, ou une sélection | ● | Charmant, sans difficulté ; bon « respiration » entre deux pièces lentes |
| Tchaïkovski, *Sérénade pour cordes* op. 48 : Valse | 4 min | ●● | Le tube ; demande une section de violons homogène |
| Tchaïkovski, *Andante cantabile* (version pour cordes) | 7 min | ●● | Sourdines, longues phrases |
| Grieg, *Peer Gynt* : *La mort d’Åse* | 4 min 30 | ● | Cordes seules ; crescendo-decrescendo à construire |

### Petit orchestre (bois par deux, deux cors, cordes, harpe ou piano)

| Œuvre | Durée | Niveau | Effectif exact | Remarques |
|---|---|---|---|---|
| Fauré, *Pavane* op. 50 | 6 min | ●● | 2.2.2.2 – 2 cors – cordes (chœur ad lib., à omettre) | Le pendant naturel de Ravel : deux pavanes, deux générations |
| Fauré, *Sicilienne* (*Pelléas et Mélisande*) | 4 min | ●● | Flûte solo, harpe, cordes, quelques bois | Solo de flûte exposé |
| Fauré, *Masques et bergamasques* : Menuet, Gavotte, Pastorale | 3 + 3 + 3 min 30 | ●● | 2.2.2.2 – 2 cors – harpe – cordes (l’Ouverture ajoute 2 trompettes et timbales) | Sans l’Ouverture, tout tient dans l’effectif de base |
| Massenet, *Méditation* de *Thaïs* | 5 min 30 | ●● (solo ●●●) | Petit orchestre, harpe, cordes | **Nina en soliste**, debout, en dirigeant ; l’accompagnement est simple |
| Fauré, *Berceuse* op. 16 (violon et orchestre) | 4 min | ●● | Petit orchestre, cordes | Même idée, plus intime |
| Elgar, *Chanson de matin* / *Chanson de nuit* | 3 + 4 min | ● | 2 flûtes, hautbois, 2 clarinettes, basson, 2 cors, harpe, cordes | Faciles, parfaits en bis ou en ouverture |
| Elgar, *Salut d’amour* | 3 min | ● | Petit orchestre, cordes | Bis tout trouvé |
| Delius, *Au premier coucou du printemps* | 6 min 30 | ●● | 2 flûtes, hautbois, 2 clarinettes, 2 bassons, 2 cors, cordes | Couleur proche de Ravel ; tempo très lent à tenir |
| Bartók, *Danses populaires roumaines* (version pour petit orchestre, 1917) | 6 min | ●● | 2 flûtes (piccolo), 2 clarinettes, 2 bassons, 2 cors, cordes | Domaine public dans l’UE depuis 2016 ; six danses, changements de tempo nets : excellent pour un orchestre dirigé du violon |
| Bizet, *Jeux d’enfants* : Berceuse, Duo | 3 + 3 min | ● | Petit orchestre | Marche et Galop ajoutent trompettes, timbales et percussion (●●) |
| Grieg, *Peer Gynt* : *La danse d’Anitra* | 3 min 30 | ●● | Cordes et triangle | Pizzicati, légèreté |
| Abreu, *Tico-Tico no Fubá* | 3 min | ●● | Effectif de base, percussion légère, piano | Voir ci-dessus ; en finale ou en bis |

### Vents seuls (les cordes se reposent, les vents ont leur moment)

| Œuvre | Durée | Niveau | Effectif | Remarques |
|---|---|---|---|---|
| Gounod, *Petite symphonie* : Andante cantabile, Scherzo | 5 + 4 min | ●● | Flûte, 2 hautbois, 2 clarinettes, 2 cors, 2 bassons | Neuf vents ; se dirige depuis la flûte ou le premier hautbois |
| Mozart, Divertimento K. 270 (un mouvement) | 3 à 4 min | ●● | 2 hautbois, 2 cors, 2 bassons | Six vents |

## Cinq programmes prêts à l’emploi

Chaque programme dure 28 à 32 minutes, alterne les formations (pour que chacun joue et se repose), place la Pavane de Ravel là où elle porte le mieux, et finit sur une pièce qui « ferme » le concert : *Tico-Tico* dans quatre programmes sur cinq.

### Programme 1 — « Deux pavanes » (musique française, 1872–1910)

| Ordre | Œuvre | Formation | Durée |
|---|---|---|---|
| 1 | Fauré, *Pavane* op. 50 | Petit orchestre | 6 min |
| 2 | Bizet, *L’Arlésienne*, Adagietto | Cordes | 3 min |
| 3 | Massenet, *Méditation* de *Thaïs* — Nina en soliste | Petit orchestre | 5 min 30 |
| 4 | Fauré, *Masques et bergamasques* : Menuet, Gavotte | Petit orchestre | 6 min |
| 5 | Ravel, *Pavane pour une infante défunte* | Petit orchestre | 6 min 30 |
| 6 | Abreu, *Tico-Tico no Fubá* | Petit orchestre et percussion | 3 min |
| | **Total** | | **≈ 30 min** |

Un seul effectif pour tout le concert, harpe ou piano pour Fauré, Massenet et Ravel. Le plus cohérent et le plus simple à organiser ; *Tico-Tico* fait sortir du rêve français en trois minutes.

### Programme 2 — « Suites pour cordes » (le choix le plus sûr)

| Ordre | Œuvre | Formation | Durée |
|---|---|---|---|
| 1 | Holst, *St Paul’s Suite* | Cordes | 12 min |
| 2 | Ravel, *Pavane pour une infante défunte* | Petit orchestre | 6 min 30 |
| 3 | Elgar, *Serenade pour cordes* op. 20 | Cordes | 12 min |
| 4 | Bis : Abreu, *Tico-Tico no Fubá* | Petit orchestre et percussion | 3 min |
| | **Total** | | **≈ 33 min 30, dont 3 min de bis** |

Les vents ne jouent que la Pavane, placée au centre, et le bis. Si les vents doivent jouer davantage, remplacer la *Serenade* d’Elgar par Fauré, *Pavane* + Delius, *Au premier coucou du printemps* (12 min 30).

### Programme 3 — « Nord et lumière » (Grieg, Delius, Ravel)

| Ordre | Œuvre | Formation | Durée |
|---|---|---|---|
| 1 | Grieg, *Deux mélodies élégiaques* op. 34 : *Blessure du cœur*, *Le dernier printemps* | Cordes | 9 min |
| 2 | Delius, *Au premier coucou du printemps* | Petit orchestre | 6 min 30 |
| 3 | Grieg, *Peer Gynt* : *La mort d’Åse* | Cordes | 4 min 30 |
| 4 | Ravel, *Pavane pour une infante défunte* | Petit orchestre | 6 min 30 |
| 5 | Grieg, *Peer Gynt* : *La danse d’Anitra* | Cordes et triangle | 3 min 30 |
| | **Total** | | **≈ 30 min** |

Programme de couleur : printemps, lumière du Nord, pavane. Le seul des cinq sans *Tico-Tico*, pour garder l’unité de ton ; la *Danse d’Anitra* fait une fin légère. Si Nina tient à *Tico-Tico*, le donner en bis : le contraste fonctionne.

### Programme 4 — « Danses et jeux » (jeune public, familles)

| Ordre | Œuvre | Formation | Durée |
|---|---|---|---|
| 1 | Bizet, *Jeux d’enfants* : Berceuse, Duo | Petit orchestre | 6 min |
| 2 | Tchaïkovski, *Sérénade pour cordes* : Valse | Cordes | 4 min |
| 3 | Ravel, *Pavane pour une infante défunte* | Petit orchestre | 6 min 30 |
| 4 | Grieg, *La danse d’Anitra* | Cordes et triangle | 3 min 30 |
| 5 | Bartók, *Danses populaires roumaines* | Petit orchestre | 6 min |
| 6 | Abreu, *Tico-Tico no Fubá* | Petit orchestre et percussion | 3 min |
| | **Total** | | **≈ 29 min** |

Six pièces courtes, rythme de concert vif ; tout tient dans l’effectif de base, plus un triangle et une percussion légère. Si l’orchestre dispose de trompettes et de timbales, ouvrir par la Marche de *Jeux d’enfants* (2 min). Les danses de Bartók puis *Tico-Tico* enchaînées font une fin irrésistible pour un jeune public.

### Programme 5 — « Nina soliste, et chacun son tour »

| Ordre | Œuvre | Formation | Durée |
|---|---|---|---|
| 1 | Mozart, Divertimento K. 136 : Allegro | Cordes | 6 min |
| 2 | Gounod, *Petite symphonie* : Andante cantabile, Scherzo | Neuf vents | 9 min |
| 3 | Massenet, *Méditation* de *Thaïs* — Nina en soliste | Petit orchestre | 5 min 30 |
| 4 | Ravel, *Pavane pour une infante défunte* | Petit orchestre | 6 min 30 |
| 5 | Abreu, *Tico-Tico no Fubá* | Petit orchestre et percussion | 3 min |
| | **Total** | | **≈ 30 min** |

Chaque groupe a sa pièce : les cordes seules, les vents seuls, puis tout le monde avec la soliste, et *Tico-Tico* pour finir ensemble. Le plus valorisant pour l’orchestre, le plus exigeant pour Nina (un solo et la direction). Pour un second solo, ajouter Fauré, *Berceuse* op. 16 (4 min) avant la *Méditation*.

## Comment choisir

- **Première expérience, peu de temps de répétition** : programme 2 (trois œuvres, deux formations) ou programme 1 (un seul effectif).
- **Orchestre à vents solide** : programme 1 ou 5.
- **Vents fragiles ou incomplets** : programme 2 ; la Pavane de Ravel reste jouable avec hautbois, clarinette, basson et cor à un (prévoir alors le piano pour la harpe et vérifier les doublures).
- **Public familial, concert scolaire** : programme 4.
- **Thème « couleurs », concert du soir** : programme 3.

Dans tous les cas, l’ordre suit la même logique : ouvrir par une pièce sûre, placer la Pavane de Ravel au centre ou en avant-dernière position, finir par une pièce qui tient toute seule (*Tico-Tico*, Bartók, la Valse, la *Danse d’Anitra*), et garder un bis court de deux ou trois minutes (Elgar, *Salut d’amour* ; Bizet, Adagietto ; Schubert, une danse ; ou *Tico-Tico* repris).

## Matériel et pratique

- **IMSLP** : télécharger conducteur et parties d’orchestre, puis vérifier le nombre de parties de cordes (en général 4-4-3-3-2 à l’achat ; en téléchargement, imprimer selon l’effectif).
- ***Tico-Tico*** : décider tôt entre l’arrangement Kazik (cordes, à commander), l’arrangement Traversi (orchestre, à examiner) et l’arrangement maison ; prévoir la percussion (maracas ou pandeiro, caisse claire) et un pianiste.
- **Harpe** : Ravel, Fauré (*Pavane* : pas de harpe ; *Sicilienne* et *Masques* : harpe), Massenet, Elgar. Un piano remplace la harpe partout ; prévoir le pianiste aux répétitions.
- **Numéros de mesure et lettres** : vérifier qu’ils sont imprimés dans les parties avant la première répétition (certaines éditions anciennes n’en ont pas : les ajouter au crayon avant de distribuer).
- **Temps de répétition** : compter une répétition de trois heures par tranche de dix minutes de musique nouvelle pour un orchestre d’étudiants, soit trois répétitions pour un programme de trente minutes, plus une générale.
- **Direction** : pour les pièces où Nina est soliste, confier la levée au deuxième chef d’attaque (premier violon, deuxième pupitre), convenu à l’avance ; Nina reprend la direction dès qu’elle rejoint le tutti.
"""

rep = pathlib.Path(__file__).resolve().parent.parent / "atelier" / "docs" / "medleys-testes.md"
if rep.exists():
    md += "\n" + rep.read_text(encoding="utf-8")
data["programmes"] = {"title": "Programmes de concert", "subtitle": "Une demi-heure, orchestre réduit, sans baroque : cinq programmes et sept medleys testés autour de la Pavane de Ravel et de Tico-Tico", "markdown": md}
OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
print("programmes added", len(md), "chars")
