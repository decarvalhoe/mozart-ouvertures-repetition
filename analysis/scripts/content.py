# -*- coding: utf-8 -*-
"""Contenu du guide et des fiches -> out/final.json (consommé par build_site.py)."""
import json, pathlib, sys
OUT = pathlib.Path(sys.argv[1])
EX = "C:/Users/decar/AppData/Local/Temp/claude/C--/9fca1ff0-df9f-4388-9073-67161524a749/scratchpad/out/excerpts"

excerpts = {
    "figaro/ouverture_1_7": {"title": "Figaro, début : l’unisson pp", "start_bar": 1, "end_bar": 7, "parts": "violons, altos, violoncelles, bassons", "svg_path": f"{EX}/figaro/ouverture_1_7.svg"},
    "zauberfloete/adagio_1_3": {"title": "La Flûte, Adagio : les trois accords initiaux (cordes)", "start_bar": 1, "end_bar": 3, "parts": "cordes ; les vents, cuivres et timbales doublent", "svg_path": f"{EX}/zauberfloete/adagio_1_3.svg"},
    "zauberfloete/fugato_16_27": {"title": "La Flûte, Allegro : entrées du fugato", "start_bar": 16, "end_bar": 27, "parts": "cordes", "svg_path": f"{EX}/zauberfloete/fugato_16_27.svg"},
    "zauberfloete/trois_accords_97_102": {"title": "La Flûte : le « triple accord » central (réduction)", "start_bar": 97, "end_bar": 102, "parts": "hautbois, trombones, bassons ; les autres vents, cuivres et timbales doublent", "svg_path": f"{EX}/zauberfloete/trois_accords_97_102.svg"},
}

guide = r"""
# Guide de répétition

## L’essentiel en dix lignes

1. Votre premier outil n’est pas la parole : c’est la **levée** (respiration + volute + archet). Tout le reste en découle.
2. Chaque arrêt suit le même rituel : **où l’on reprend, une seule consigne, on rejoue**. Jamais deux consignes à la fois.
3. Les quatre heures se jouent sur **cinq passages** : l’unisson *pp* de *Figaro* (mes. 1–7 et 139–145), le second thème *fp* (mes. 59–74 et 171–188), la coda *pp* → *crescendo* (mes. 236–250), les accords de l’Adagio de *La Flûte* (mes. 1–3 et 97–102) et le fugato (mes. 16–39 et 144–160).
4. Diagnostiquez avant de corriger : un **filage sans arrêt** de chaque ouverture, montre en main, puis seulement le travail.
5. Travaillez **lentement puis par paliers** de tempo : *Figaro* à ♩= 192 (blanche = 96), puis 112, 126, 138.
6. La justesse se règle **de bas en haut** : contrebasses et violoncelles donnent la fondamentale, les tierces se placent dessus, basses.
7. Le style classique tient en trois règles : **vibrato = ornement**, **fort–faible** en fin de phrase, **articulation telle qu’écrite** (la dernière note d’une liaison s’allège).
8. Les nuances sont **par paliers et subito**, jamais glissées : le seul vrai *crescendo* écrit de *Figaro* est aux mes. 244–249.
9. Les chefs de pupitre sont vos relais : coups d’archet **écrits et convenus avant 9 h**, pas pendant la répétition.
10. Terminez par un **filage** et par ce qui s’est amélioré. L’orchestre doit sortir en sachant ce qu’il a gagné.

## Avant la répétition

**La veille**

- Envoyer le *Plan de la répétition* (fiche 1) à tout l’orchestre, avec les numéros de mesure des passages travaillés.
- Convenir des coups d’archet avec les chefs de pupitre des seconds violons, des altos et des violoncelles–contrebasses (fiches 2 et 3). Ils les reportent dans les parties **avant** la répétition.
- Désigner un référent vents (premier hautbois) et lui transmettre la fiche 4 : il mènera l’attaque des trois accords de *La Flûte* (mes. 97–102), où les cordes se taisent.
- Vérifier que toutes les parties portent des **numéros de mesure** cohérents avec la partition de direction. Les mesures de ce guide suivent la Neue Mozart-Ausgabe.
- Réécouter deux versions de chaque ouverture (fiche 7), une historiquement informée et une « moderne », en notant les tempi.

**Le matin, avant 9 h**

- Disposition : premiers et seconds violons de part et d’autre (disposition dite « à l’allemande »), altos et violoncelles au centre, contrebasses derrière les violoncelles. Vous devez voir le chef d’attaque des seconds violons, le premier violoncelle et le premier hautbois sans tourner la tête.
- Votre pupitre tourné d’un quart vers l’orchestre, chaise légèrement surélevée si possible.
- Un métronome visible (téléphone) et une montre : les créneaux ci-dessous sont minutés.
- Le la : donné par le premier hautbois à 9 h 00 précises. Vents, puis cuivres, puis cordes (contrebasses en premier).

## Déroulé des quatre heures

Le découpage suit la logique « diagnostiquer, puis travailler, puis réassembler ». Les horaires sont des bornes à tenir, quitte à écourter un point : mieux vaut un passage laissé imparfait qu’un déroulé qui déborde.

| Horaire | Contenu | Objectif |
|---|---|---|
| 9h00–9h12 | Accord, chorale d’accords (ré majeur puis mi♭ majeur), gamme de ré à l’unisson en croches | Oreille, son commun, premier contact avec votre levée |
| 9h12–9h20 | Figaro : filage sans arrêt (≈ 4 min) + deux remarques | Diagnostic |
| 9h20–9h50 | Figaro : mes. 1–11 et 139–149 (unisson pp, violoncelles seuls), mes. 12–17 et 150–155 (premier tutti) | Mise en place, départ, contraste subito |
| 9h50–10h15 | Figaro : second thème fp mes. 59–74 et 171–188 ; alternances f/p mes. 36–41 et 122–133 | Nuances par paliers, fp |
| 10h15–10h40 | Figaro : coda pp mes. 236–249 et crescendo, tutti final mes. 250–294 ; puis filage | Tenue du pp, crescendo progressif, fin |
| 10h40–11h00 | Pause | — |
| 11h00–11h10 | Flûte enchantée : filage sans arrêt (≈ 7 min) + deux remarques | Diagnostic |
| 11h10–11h40 | Flûte : Adagio mes. 1–15 et le triple accord mes. 97–102 | Justesse des accords, rythme pointé, levées |
| 11h40–12h10 | Flûte : fugato mes. 16–39 et réexposition mes. 144–160 ; développement et sforzandi mes. 103–143 | Égalité des croches, relais des entrées, sf relatifs |
| 12h10–12h30 | Flûte : tutti mes. 39–60, strette finale mes. 209–226 ; puis filage | Équilibre cordes/vents/cuivres, clarté dans le ff |
| 12h30–12h50 | Reprise des trois points les plus fragiles (deux ouvertures), 6 min chacun | Consolidation |
| 12h50–13h00 | Filage de Figaro, bilan en trois phrases, remerciements | Conclure sur une réussite |

Deux principes pour tenir ce plan :

- **Une horloge, pas une liste.** À l’heure dite, on change de passage, même si le précédent n’est pas parfait. Le point reviendra à 12h30.
- **Les filages sont sacrés.** Ils donnent à l’orchestre la sensation de la pièce entière, et à vous la mesure du progrès.

## Diriger depuis le premier violon

Vous n’avez ni bras libre ni baguette : vous dirigez avec la respiration, la volute, l’archet et le regard. L’orchestre doit vous *entendre respirer*.

**La levée**

- Une levée = une respiration audible dans le tempo exact de ce qui suit, accompagnée d’un mouvement de la volute vers le haut puis vers le bas sur le temps. Le mouvement est petit, net, et toujours le même.
- Pour l’unisson *pp* de *Figaro* (mes. 1) : l’archet posé sur la corde avant la levée, respiration sur une blanche (le temps de la mesure à deux), départ sur la descente de la volute. Donnez le tempo réel dès la levée, jamais plus lent.
- Pour les accords de l’Adagio de *La Flûte* (mes. 1) : respiration ample sur une noire, descente de la volute plus lente ; l’archet part du talon, déjà sur la corde. Les vents regardent le premier hautbois, qui vous regarde.
- Après chaque point d’orgue (mes. 3 de l’Adagio ; mes. 15 avant l’Allegro) : coupez avec un petit mouvement vers vous, respirez, repartez. Ne laissez jamais l’orchestre deviner.

**Qui regarde qui**

- Vous regardez, dans l’ordre : le chef d’attaque des seconds violons (il relaie aux altos), le premier violoncelle (il relaie aux contrebasses), le premier hautbois (il relaie aux vents et aux cuivres).
- Dites-le explicitement à 9 h : « Je ne peux pas tout montrer : les seconds relaient ma levée aux altos, le premier violoncelle aux contrebasses, le premier hautbois aux vents. »
- La timbale regarde le premier violoncelle, pas vous : les attaques *f* de *Figaro* (mes. 12, 150, 250) tiennent à cette chaîne.

**Les changements de tempo de *La Flûte***

- Adagio → Allegro (mes. 15–16) : le point d’orgue de la mes. 15 est coupé ; une respiration dans le tempo de l’Allegro (une blanche), et les seconds violons partent seuls. Convenez avec eux que c’est **votre respiration** qui donne le tempo, pas leur première croche.
- Allegro → Adagio (mes. 96–97) : les cordes se taisent. Coupez la dernière croche de l’Allegro en levant l’archet, puis donnez la levée des vents avec la volute, sur la respiration du premier hautbois.
- Adagio → Allegro (mes. 102–103) : même procédé qu’à la mes. 16 ; les premiers violons partent cette fois, donc vous : jouez la première croche comme une évidence.

**La discipline de l’arrêt**

Chaque arrêt suit la même séquence, dans cet ordre, en moins de vingt secondes :

1. « Mesure 59. » (Le numéro, d’abord. Tout le monde cherche.)
2. Une consigne, une seule : « Le *fp* est sur la première croche ; dès la deuxième, nous sommes *piano*. »
3. « Deux mesures avant, mesure 57. » Levée. On rejoue.

Phrases prêtes à l’emploi :

- « On reprend à 139, les mêmes consignes qu’au début. »
- « Seconds et altos seuls, mesure 59, en comptant deux temps avant. »
- « Vents, tenez l’accord de la mesure 85 ; cordes, écoutez où se place la tierce. »
- « On ne s’arrête plus jusqu’à la fin ; si ça se défait, on continue. »
- « C’était mieux. On le garde. Mesure 236. »

Trois règles complémentaires :

- Ne vous arrêtez pas pour ce qui se corrigera de soi au deuxième passage (Panula : *avant d’arrêter l’orchestre, demandez-vous si c’est nécessaire*).
- Parlez peu, et jamais en jouant. Vos mots doivent valoir cher.
- Quand un chef de pupitre n’est pas d’accord sur un coup d’archet : « On essaie les deux, maintenant, deux fois chacun », et vous tranchez en dix secondes. La décision vaut plus que l’argument.

## Les Noces de Figaro — carte de la partition

Ré majeur, Presto, ¢ (à deux temps), 294 mesures, forme sonate sans développement. Effectif : 2 flûtes, 2 hautbois, 2 clarinettes en la, 2 bassons, 2 cors en ré, 2 trompettes en ré, timbales, cordes. La Neue Mozart-Ausgabe signale qu’après la mes. 134 Mozart avait esquissé puis biffé quatre mesures introduisant un Andante con moto en ré mineur à 6/8 : l’ouverture reste donc d’un seul tenant.

| Mesures | Section | Ce qu’il se passe | Pour la répétition |
|---|---|---|---|
| 1–7 | Exposition : premier thème | Unisson pp des cordes et des bassons, figure ré–do♯–ré–do♯–ré | Le passage le plus exposé de la matinée |
| 7–11 | — | Les violoncelles seuls en croches ; hautbois, cors p (mes. 8), flûtes, clarinettes p (mes. 9, 11) | Les contrebasses se taisent à la mes. 7 |
| 12–17 | Premier tutti | ff, timbales et trompettes | Contraste subito, pas de crescendo avant |
| 18–28 | — | Retour du p : unisson des cordes, flûte et hautbois solo (« Imo ») mes. 18–23 ; dialogue des vents 24–28 | Cordes sous les solistes |
| 29–35 | Tutti | ff puis fp (mes. 35) | — |
| 36–41 | — | Vents fp, cordes f puis p dans chaque mesure | Alternances par paliers |
| 42–58 | Transition | Accords f, croches répétées, arrivée sur la dominante (la) | Stabilité du tempo |
| 59–74 | Second thème | fp sur chaque mesure : seconds violons et altos en croches, premiers violons en tenues ; hautbois fp 63, flûtes 66, bassons 67 | Le fp : attaque puis p immédiat |
| 75–80 | — | Alternance f (accords) / p (mélodie des premiers violons) | — |
| 81–95 | Groupe conclusif | f ; mes. 85–95 : tenues des vents, mélodie bassons–altos–violoncelles, croches répétées des violons sur la | Justesse des tenues ; croches régulières |
| 96–104 | — | p : dialogue violons I / II, chromatismes ; basson Imo 100–104 | Pianissimo d’écoute |
| 105–121 | — | Basson solo (Imo) et premiers violons ; seconds violons en croches « simile » ; flûte Imo 116 | Accompagnement léger |
| 122–134 | Fin d’exposition | Vents fp, cordes f/p ; mes. 134 accord f avec trilles | — |
| 135–138 | Transition | p, violons | Préparer le pp |
| 139–145 | Réexposition | Unisson pp, comme mes. 1–7 | Mêmes consignes qu’au début |
| 146–163 | — | Comme 8–28 (tutti ff 150, p 156, solistes 158–163) | — |
| 164–170 | Tutti | f | — |
| 171–188 | Second thème en ré | fp, comme 59–74 | — |
| 189–209 | Groupe conclusif | p/f 189–194 ; f 195 ; tenues des vents et mélodie basse 198–209 | — |
| 210–235 | — | p ; basson Imo 213–219 ; mélodie des premiers violons 220–235 sur croches des seconds | — |
| 236–249 | Coda, 1re partie | pp (violons I 236, violons II 238, altos 240) ; « cre-scen-do » écrit en toutes lettres mes. 244–249 | Rester pp jusqu’à 243 |
| 250–281 | Coda, 2e partie | f tutti ; traits descendants 260 et 275–281 ; trilles 262–263, 276, 280 | Clarté des traits |
| 282–294 | Cadence finale | Accords, croches des seconds, altos, violoncelles 284–289 ; accords finaux 290–294 | Tous les accords tirés |

## Figaro — passages prioritaires

### 1. L’unisson pp (mes. 1–7, puis 139–145)

[[excerpt:figaro/ouverture_1_7]]

**Ce qui se passe d’habitude** : le départ est flou, le tempo monte dès la mes. 2, les do♯ et sol♯ ne sont pas à la même hauteur selon les pupitres, les bassons sortent de l’unisson en pp (les anches montent quand on pince).

**Méthode (12 minutes)**

1. Blanche = 96. Cordes et bassons, sans vents : mes. 1–7, trois fois. Consigne unique : « petit archet, au milieu, sur la corde ».
2. Même tempo, premiers violons seuls, puis seconds seuls, puis altos, puis violoncelles, puis bassons : chacun joue mes. 1–4. Vous entendez qui décale et qui presse ; dites-le en une phrase.
3. Blanche = 112, tous : mes. 1–11. Les violoncelles continuent seuls à la mes. 7 ; les contrebasses s’arrêtent net.
4. Blanche = 126, puis 138 : mes. 1–17, pour enchaîner le tutti.
5. Enfin la levée seule : trois départs successifs, sans jouer plus de deux mesures. L’orchestre apprend votre respiration.

**Coup d’archet** (choisissez avant 9 h, voir fiche 2) : soit les liaisons telles qu’écrites, **une mesure par archet** (mes. 1 tirée, 2 poussée, 3 tirée, 4 poussée, 5 tirée, 6 poussée, 7 tirée) — c’est la lecture la plus fidèle au texte et la plus « chuchotée » ; soit tout détaché à la corde, départ tiré, les noires des mes. 1 et 3 tombant tirées — plus sûr avec un orchestre d’étudiants. Dans les deux cas : pas de vibrato, archet au milieu, le pp est une couleur, pas une absence de son.

**Justesse** : accorder l’unisson sur les cordes à vide ré et la ; do♯ et sol♯ sont des broderies serrées (juste sous ré et la). Les bassons écoutent les violoncelles, pas les violons.

### 2. Le premier tutti (mes. 12–17, puis 150–155)

**Ce qui se passe** : le ff arrive une croche en avance (anticipation des timbales et des cuivres), les croches des altos et des basses deviennent lourdes.

**Méthode (6 minutes)** : mes. 8–17 deux fois à blanche = 112, puis tempo. Consigne aux vents et à la timbale : « votre ff est sur la première croche de la mes. 12, pas avant ; regardez le premier violoncelle ». Consigne aux altos et basses : « croches détachées, à la corde, dans la moitié inférieure, sans écraser ».

### 3. Le second thème fp (mes. 59–74, puis 171–188)

**Ce qui se passe** : le fp devient un f, ou un sfz ; les croches des seconds et des altos perdent leur régularité ; les premiers violons tiennent trop fort.

**Méthode (10 minutes)**

1. Seconds violons et altos seuls, mes. 59–66, blanche = 100 : « fp = la première croche seulement ; dès la deuxième, pointe, piano ».
2. Ajouter les premiers violons : leur tenue fp = archet rapide à l’attaque, puis quasi immobile.
3. Ajouter hautbois (mes. 63), flûtes (66), bassons (67) : chaque entrée est une couleur de plus, pas un crescendo.
4. Tempo : mes. 54–80 enchaînées.

### 4. La coda : pp puis crescendo (mes. 236–262)

**Ce qui se passe** : le pp de la mes. 236 n’est pas pp, le crescendo commence à 240 au lieu de 244, et le tutti de 250 arrive essoufflé.

**Méthode (10 minutes)**

1. Premiers violons seuls mes. 236–243 : pp, pointe, sur la corde, aucune nuance.
2. Seconds (238), altos (240), violoncelles–contrebasses (noires pp) : entrer sans changer la dynamique.
3. Mes. 244–249 : le crescendo est syllabé « cre-scen-do » sur six mesures dans la partition. Faites-le compter : 244 pp, 246 p, 248 mf, 250 f. Le f de 250 arrive avec les timbales et les trompettes : il doit être une arrivée, pas un sommet dépassé.
4. Mes. 250–263 à tempo : traits descendants de la mes. 260 « détaché large », trilles 262–263 mesurés (en doubles croches si l’orchestre n’est pas sûr).

### 5. Les tenues du groupe conclusif (mes. 85–95, puis 198–209)

**Ce qui se passe** : les vents tiennent faux (tierces hautes), les violons accentuent leurs croches répétées.

**Méthode (6 minutes)** : vents seuls, chaque accord tenu quatre secondes, « contrebasses et bassons donnent la basse, la tierce se place en dessous ». Puis violons seuls mes. 85–88 : « huit croches identiques, aucune n’est plus forte que l’autre, archet au milieu ». Puis tous, en écoutant la mélodie des bassons, altos et violoncelles.

## La Flûte enchantée — carte de la partition

Mi♭ majeur, Adagio (C) puis Allegro (¢), 226 mesures. Effectif : 2 flûtes, 2 hautbois, 2 clarinettes en si♭, 2 bassons, 2 cors en mi♭, 2 trompettes en mi♭, 3 trombones, timbales, cordes. Les numéros de mesure ci-dessous proviennent d’une édition de référence encodée (226 mesures, cohérent avec la NMA) : faites-les vérifier sur le matériel de l’orchestre avant la répétition.

| Mesures | Section | Ce qu’il se passe | Pour la répétition |
|---|---|---|---|
| 1–3 | Adagio : les trois accords | Tutti f ; chaque accord est une blanche suivie de silences puis d’une levée ; point d’orgue à la mes. 3 | Justesse, attaques, silences exacts |
| 4–15 | Adagio | Rythme pointé, harmonies chromatiques, arrivée sur la dominante avec point d’orgue (mes. 15) | Double croche courte et tardive |
| 16–38 | Allegro : fugato | Sujet aux seconds violons seuls (16), premiers violons (20), altos, violoncelles et bassons (27), contrebasses (33), vents (37) | Égalité des croches, relais des entrées |
| 39–60 | Tutti | f : hautbois, trompettes, trombones et timbales entrent à la mes. 39 ; entrées du sujet en strette (40–42) | Ne pas presser à l’entrée du tutti |
| 55–78 | — | Entrées du sujet dans d’autres tons (55, 57, 58, 60, 62, 68, 78) | Chaque entrée est annoncée |
| 79–96 | Fin d’exposition | Sur la dominante ; les cordes se taisent après la mes. 96 | Préparer le silence |
| 97–102 | Adagio : le triple accord | Vents, cuivres et timbales seuls, si♭ majeur ; trois fois « levée–blanche, blanche–silence » | Vous ne jouez pas : vous donnez la levée |
| 103–143 | Allegro : développement | Sujet aux premiers violons (103), violoncelles (105), puis en do, sol, fa, mi♭, ré (109–123) ; sforzandi à contretemps | sf relatifs à la nuance |
| 144–160 | Réexposition | Sujet aux seconds violons en mi♭ (144), premiers violons (146), basses (150–152), tutti (154–157) | Comme à la mes. 16, mais le tutti enchaîne |
| 161–208 | — | Entrées (161, 176–183, 189, 198), tutti | Clarté dans le ff |
| 209–226 | Coda | Strette finale sur le sujet (219–221 : mi♭, si♭, sol), accords conclusifs | Doubles croches nettes jusqu’au bout |

## La Flûte — passages prioritaires

### 1. Les trois accords de l’Adagio (mes. 1–3)

[[excerpt:zauberfloete/adagio_1_3]]

**Ce qui se passe** : les attaques ne sont pas ensemble (les vents respirent avant les cordes), les accords sont ternes ou faux, les levées en doubles croches arrivent trop tôt, et le silence après chaque accord est raccourci.

**Méthode (12 minutes)**

1. Chorale : chaque accord tenu huit secondes, sans rythme. Basses d’abord, puis le reste. Accord 1 : mi♭ majeur, la tierce **sol** est tenue par les violons (double corde sol–mi♭) : sol un peu bas, et surtout **pas la corde à vide**, trop haute pour une tierce. Accord 2 : do mineur (mi♭ tierce mineure, légèrement haute). Accord 3 : mi♭ majeur avec **sol à la basse** (altos, violoncelles, contrebasses) : la tierce est en dessous de tout l’orchestre, elle doit être très légèrement basse et parfaitement stable.
2. Rythme seul, sur une note : blanche, silence, levée. La levée en double croche se joue **tard** et courte, dans le tempo exact.
3. Les trois accords en tempo (noire = 58), trois fois, avec votre levée. Entre chaque essai, une seule consigne.
4. Le point d’orgue de la mes. 3 : coupez, respirez, et donnez la reprise aux premiers violons (triolet de triples croches, p).

### 2. Le fugato (mes. 16–39, puis 144–160)

[[excerpt:zauberfloete/fugato_16_27]]

**Ce qui se passe** : les six croches répétées ne sont pas égales (la première est accentuée, la dernière s’affaisse), les doubles croches sont brouillonnes, chaque nouvelle entrée est trop forte puis ne s’efface pas, et le tempo monte à chaque entrée.

**Méthode (14 minutes)**

1. Seconds violons seuls, mes. 16–19, blanche = 84 : « six croches identiques, au milieu de l’archet, les quatre doubles croches avec le même archet, sans crescendo ». Deux fois.
2. Premiers violons seuls mes. 20–23 : même consigne. Puis seconds + premiers mes. 16–26 : « à la mes. 20, les seconds deviennent accompagnement : un cran en dessous, immédiatement ».
3. Altos, violoncelles et bassons mes. 27–32 seuls, puis contrebasses à la mes. 33. Puis tout le fugato mes. 16–38, blanche = 100.
4. Mes. 16–42 à blanche = 116, pour entendre le tutti de la mes. 39 arriver sans accélération. Consigne aux cuivres et à la timbale : « vous entrez dans le tempo des cordes, pas dans le vôtre ».
5. Même travail, plus court, à la réexposition mes. 144–157.

**Justesse** : mes. 20–21 aux seconds violons, ligne chromatique (sol, sol♯, sol, fa, mi♭…) : demi-tons serrés et réguliers, sans vibrato.

### 3. Le triple accord central (mes. 97–102)

[[excerpt:zauberfloete/trois_accords_97_102]]

**Ce qui se passe** : les cordes se taisent, l’orchestre attend un geste qui ne vient pas. L’accord est lourd, les trombones couvrent, la levée en double croche n’est pas ensemble.

**Méthode (8 minutes)**

1. Avec le premier hautbois, convenez : c’est **sa respiration** qui déclenche l’accord ; vous donnez la levée du regard et de la volute une noire avant. Répétez le geste trois fois sans jouer.
2. Vents, cuivres, timbales : chaque accord tenu, « trombones et timbales en dessous des hautbois ; la tierce (ré) basse ». Puis en rythme : « levée courte, blanche pleine, silence exact ».
3. Enchaînement mes. 94–104, deux fois : fin de l’Allegro, respiration, triple accord, reprise de l’Allegro aux premiers violons. Le tempo de reprise (mes. 103) est le même qu’à la mes. 16.

### 4. Les sforzandi du développement (mes. 103–143)

**Ce qui se passe** : les sf deviennent des accents de fanfare dans une nuance piano, et les entrées du sujet (103, 105, 109–123) sont couvertes.

**Méthode (8 minutes)** : mes. 103–124 à blanche = 100. « Un sf dans piano est un petit accent : archet rapide sur la note, puis on relâche. » Faites jouer les entrées du sujet seules (premiers violons 103, violoncelles 105, bassons et basses 109–123), puis tout l’orchestre « avec le sujet toujours devant ».

### 5. La strette finale (mes. 209–226)

**Ce qui se passe** : les doubles croches disparaissent dans le ff, les trombones et la timbale prennent le dessus, la dernière note est écourtée.

**Méthode (6 minutes)** : cordes seules mes. 219–226 à blanche = 100, « doubles croches articulées, archet au milieu, le ff vient de la vitesse de l’archet, pas de la pression ». Puis tous, en imposant l’équilibre : « cuivres un cran en dessous, timbale sèche ». La dernière note est tenue sa valeur entière, et coupée sur votre geste.

## Justesse et harmonie

**L’ordre d’accord.** Le la du premier hautbois ; les vents, puis les cuivres, puis les contrebasses, les violoncelles, les altos, les violons. Vérifier ensuite un accord parfait de ré majeur puis de mi♭ majeur, tenu dix secondes, basses d’abord.

**La règle des tierces.** Dans un accord tenu, la tierce majeure juste est plus basse que celle du piano (d’environ 14 cents) ; la tierce mineure est plus haute (d’environ 16 cents) ; la quinte est pure. À dire aux musiciens : « la quinte s’installe ; la tierce majeure se place *dessous* ». Les sensibles (do♯ en ré, ré en mi♭) sont au contraire placées hautes quand elles mènent à la tonique dans une ligne mélodique, mais basses quand elles sont la tierce d’un accord de dominante tenu.

**La méthode « accord par accord ».** Choisir un accord tenu, l’arrêter sur le temps, le faire tenir : contrebasses seules, puis violoncelles, puis les voix du milieu, puis les tierces en dernier. Dix secondes par accord, jamais plus de trois accords de suite. L’oreille se fatigue.

**Les points chauds de *Figaro***

- Mes. 1–7 et 139–145 : l’unisson. Référence : cordes à vide ré et la. Les bassons s’accordent sur les violoncelles. Les do♯, sol♯, la♯, ré♯ de ces mesures sont des broderies : serrées.
- Mes. 85–95 et 198–209 : tenues des vents sur l’accord de la (dominante) puis ses voisins ; la pédale des violons est la référence ; tierce do♯ basse, quinte mi pure.
- Mes. 122–133 : accords fp des vents en alternance : chaque accord est accordé une fois en chorale avant d’être joué en rythme.
- Mes. 290–294 : accords finaux de ré majeur : fa♯ bas, la pur.

**Les points chauds de *La Flûte***

- Mes. 1–3 : voir ci-dessus (le sol tierce, jamais à vide ; le sol à la basse de l’accord 3).
- Mes. 4–15 : harmonies chromatiques en rythme pointé ; les travailler en chorale, sans le rythme, puis en rythme lent.
- Mes. 20–21 (seconds violons) et toutes les lignes chromatiques du fugato : demi-tons serrés.
- Mes. 97–102 : accord de si♭ majeur aux vents et cuivres : ré bas, fa pur, trombones sous les hautbois.
- Mes. 219–226 : accords finaux de mi♭ majeur : sol bas.

**L’unisson, cas particulier.** Il n’y a pas d’accord à construire, seulement une hauteur commune : décidez qui est la référence (les violoncelles pour *Figaro*), et faites jouer les autres pupitres « sur » cette référence, un par un.

## Esthétique classique

**Vibrato.** Leopold Mozart (1756) traite le *tremolo* comme un ornement et se moque des violonistes qui tremblent sur chaque note « comme s’ils avaient une fièvre continuelle » ; les traités de la fin du siècle le réservent aux notes longues et au soliste. Pour votre orchestre : vibrato étroit et plutôt rapide, réservé aux tenues expressives (les tenues des vents mes. 85–95 de *Figaro*, les accords de l’Adagio de *La Flûte*), nul dans les traits et dans les unissons. Posé comme un ornement, il se décide ; il ne s’installe pas.

**Fins de phrase.** La règle de base est fort–faible : une appoggiature se résout en s’allégeant ; la dernière note sous une liaison est plus courte et plus légère ; une note suivie d’un silence se raccourcit plutôt que de s’étouffer. Dans *Figaro*, les groupes liés des mes. 1–6 portent un léger appui sur la première note et s’allègent vers la dernière ; dans *La Flûte*, les quatre doubles croches du sujet (fa–mi♭–ré–mi♭) mènent à la croche suivante sans accent.

**Articulation.** Le texte de la NMA distingue points et traits de staccato ; en pratique : le point = détaché, le trait = détaché plus court et plus marqué. Les croches sans signe se jouent détachées « à la corde » (non legato), ni liées ni sautillées. Les liaisons sont des phrasés ; quand elles sont jouables comme coups d’archet (mes. 1–6 de *Figaro*), elles produisent exactement la couleur voulue.

**Nuances.** Les contrastes sont subito et par paliers (mes. 12, 18, 29, 36–41 de *Figaro*). Le *fp* est une attaque forte immédiatement suivie du piano ; le *sf* est un accent relatif à la nuance en cours. Les crescendos ne se jouent que là où ils sont écrits : dans *Figaro*, celui des mes. 244–249 est le seul, et il est syllabé sur six mesures.

**Tempo.** *Figaro* est un Presto à ¢ : il se compte à deux, et la limite est la clarté des croches. Blanche = 132–144 en concert ; en répétition, montez par paliers (96, 112, 126, 138). *La Flûte* : Adagio noire = 54–63 ; Allegro blanche = 116–126. Le danger n’est pas la lenteur, c’est la dérive : chaque entrée du fugato tend à accélérer.

| Interprète | Figaro (blanche ≈) | Flûte, Allegro (blanche ≈) | Caractère |
|---|---|---|---|
| Harnoncourt | 128–132 | 116–120 | Articulation parlée, contrastes nets |
| Gardiner | 140 | 124 | Vif, archets légers, vibrato d’ornement |
| Abbado (Orchestra Mozart / MCO) | 136 | 120 | Équilibre moderne, chant des vents |
| Jacobs | 138 | 122 | Théâtral, accents marqués |
| Böhm | 132 | 112 | Référence « classique » du XXe siècle |

Les valeurs sont approximatives : mesurez vous-même sur dix mesures, montre en main, et notez-les sur la fiche 7.

## Pièges et plans B

- **Le départ de *Figaro* ne tient pas.** Repasser à blanche = 100, et faire jouer les mes. 1–4 en pupitres séparés. Si rien n’y fait, décider le coup d’archet « tout détaché » pour la journée : la sécurité d’abord, le texte ensuite.
- **Le temps manque.** Sacrifier dans l’ordre : les sforzandi de *La Flûte* (mes. 103–143), les alternances f/p de *Figaro* (mes. 36–41), puis les tenues du groupe conclusif. Ne jamais sacrifier le filage final.
- **Vents et cordes ne sont pas d’accord sur le tempo.** Le tempo est le vôtre : jouez-le, ne l’expliquez pas. Demandez au premier hautbois de respirer avec vous sur deux départs, devant tout le monde.
- **Un pupitre décroche dans le fugato.** Faire jouer les deux pupitres concernés seuls, quatre mesures, à blanche = 84, puis réintégrer.
- **L’orchestre fatigue (12 h).** Un filage sans arrêt vaut mieux qu’un travail de détail. Gardez la pause à l’heure.
- **Vous perdez votre place.** Dites-le simplement : « Mesure 171, je redonne. » L’autorité tient à la clarté, pas à l’infaillibilité.

## Écoutes de référence

| Œuvre | Interprète | Pourquoi l’écouter |
|---|---|---|
| Figaro | Nikolaus Harnoncourt, Concentus Musicus Wien (1993) | L’articulation « parlée », les contrastes subito, les croches détachées à la corde |
| Figaro | John Eliot Gardiner, English Baroque Soloists (1993) | La légèreté des archets, le vibrato d’ornement, la coda pp |
| Figaro | Claudio Abbado, Orchestra Mozart (2011–2012) | L’équilibre d’un orchestre moderne jouant dans le style |
| Figaro | René Jacobs, Concerto Köln (2003) | Le théâtre : tempo et accents |
| Flûte enchantée | Nikolaus Harnoncourt, Opernhaus Zürich (1987) | Les trois accords, le fugato lisible |
| Flûte enchantée | John Eliot Gardiner, English Baroque Soloists (1995) | Le tempo de l’Allegro et l’égalité des croches |
| Flûte enchantée | Claudio Abbado, Mahler Chamber Orchestra (2005) | Les tutti clairs, les trombones intégrés |
| Flûte enchantée | René Jacobs, Akademie für Alte Musik Berlin (2010) | Le triple accord, les sforzandi relatifs |

## Sources

- Wolfgang Amadeus Mozart, *Le nozze di Figaro* K. 492, Neue Mozart-Ausgabe II/5/16, éd. Ludwig Finscher, Bärenreiter, 1973 (Sinfonia, p. 5–28 ; note sur les quatre mesures biffées après la mes. 134). Partition consultée en ligne (NMA Online, Internationale Stiftung Mozarteum).
- Wolfgang Amadeus Mozart, *Die Zauberflöte* K. 620, Neue Mozart-Ausgabe II/5/19, éd. Gernot Gruber et Alfred Orel, Bärenreiter, 1970. Mesures vérifiées sur une édition de référence encodée (Mutopia Project, d’après C. F. Peters), 226 mesures.
- Leopold Mozart, *Versuch einer gründlichen Violinschule*, Augsbourg, 1756 (chap. V sur l’ordre des coups d’archet, chap. VII sur les liaisons, chap. XI sur le *tremolo*).
- Johann Joachim Quantz, *Versuch einer Anweisung die Flöte traversiere zu spielen*, Berlin, 1752 (chap. XI et XVII sur l’articulation et le jeu d’orchestre).
- Neal Zaslaw, « Vibrato in Eighteenth-Century Orchestras », *Performance Practice Review* 4/1, 1991 (Bremner : le *tremolo* est un ornement de soliste qui n’a pas sa place à l’orchestre).
- Clive Brown, *Classical and Romantic Performing Practice 1750–1900*, Oxford University Press, 1999 (points et traits, vibrato, accentuation).
- Nikolaus Harnoncourt, *Le Discours musical*, Gallimard, 1984 (articulation et « parole » musicale).
- Jorma Panula, *Some Hints to the Conductor*, éd. Jukka Iisakkila (parler le moins possible ; ne s’arrêter que si c’est nécessaire).
- Bjarte Engeset, *Rehearsing* (Conduct-It), sur la précision des consignes de nuance et le travail de la justesse en répétition.
- Simon Fischer, « Basics : Vibrato », *The Strad* (vitesse et amplitude du vibrato comme paramètres choisis).
"""

handouts = [
{"id": "plan-affiche", "title": "Plan de la répétition", "audience": "Tout l’orchestre — à afficher et à envoyer la veille", "markdown": r"""
## Samedi, 9h00–13h00

**Programme :** Mozart, Ouverture des *Noces de Figaro* (K. 492) et Ouverture de *La Flûte enchantée* (K. 620).
**Direction :** depuis le premier violon, Nina Ramousse. Les seconds violons, le premier violoncelle et le premier hautbois relaient ses départs.

**Accord à 9h00 précises** : le la est donné par le premier hautbois. Soyez installés, parties ouvertes, numéros de mesure vérifiés, à 8h55.

| Horaire | Contenu |
|---|---|
| 9h00 | Accord, chorale d’accords, gamme de ré à l’unisson |
| 9h12 | Figaro : filage complet sans arrêt |
| 9h20 | Figaro : mes. 1–17 et 139–155 (début pp, premier tutti) |
| 9h50 | Figaro : mes. 59–74 et 171–188 (second thème fp) ; mes. 36–41 et 122–133 |
| 10h15 | Figaro : mes. 236–294 (coda) ; filage |
| 10h40 | Pause (20 min) |
| 11h00 | Flûte enchantée : filage complet sans arrêt |
| 11h10 | Flûte : Adagio mes. 1–15 ; triple accord mes. 97–102 |
| 11h40 | Flûte : fugato mes. 16–39 et 144–160 ; mes. 103–143 |
| 12h10 | Flûte : mes. 39–60 ; mes. 209–226 ; filage |
| 12h30 | Reprise des points fragiles |
| 12h50 | Filage de Figaro, bilan |

**À préparer chez vous**

- *Figaro*, mes. 1–7 et 139–145 (cordes et bassons) : pp, à blanche = 112 puis 132, sans vibrato.
- *Figaro*, mes. 59–74 (seconds violons, altos) : croches régulières, fp sur la première croche seulement.
- *La Flûte*, mes. 16–38 : votre entrée du sujet, à blanche = 100 puis 120.
- *La Flûte*, mes. 97–102 (vents, cuivres, timbales) : levée courte, blanche pleine, silence exact.
- Écouter une version de chaque ouverture (fiche « À écouter »).

**Règles de la matinée**

- À chaque arrêt : le numéro de mesure d’abord, une consigne, on rejoue. Pas de discussion pendant le jeu.
- Crayon sur le pupitre. Tout coup d’archet ou consigne se note immédiatement.
- Les chefs de pupitre ont les coups d’archet : ils sont écrits dans les parties avant 9h00.
"""},
{"id": "cordes-figaro", "title": "Cordes — Figaro : coups d’archet et consignes", "audience": "Violons I et II, altos, violoncelles, contrebasses", "markdown": r"""
**Notation :** ∏ = tiré, V = poussé. Les numéros de mesure suivent la Neue Mozart-Ausgabe.

## Le début (mes. 1–7, puis 139–145) — pp, à l’unisson avec les bassons

[[excerpt:figaro/ouverture_1_7]]

**Coup d’archet retenu : option A, « une mesure par archet », liaisons telles qu’écrites**
mes. 1 ∏ (les cinq notes) · mes. 2 V (huit croches) · mes. 3 ∏ · mes. 4 V · mes. 5 ∏ · mes. 6 V · mes. 7 ∏ (la noire).
Archet au milieu, très peu de longueur, sur la corde. Léger appui sur la première note de chaque liaison, la dernière s’allège.

**Option B, « tout détaché » (si la cheffe d’attaque l’annonce) :** départ ∏, croches détachées à la corde, au milieu ; les noires des mes. 1 et 3 tombent ∏. Pas de sautillé : le pp se joue dans la corde.

Dans les deux cas : **pas de vibrato**, pas de crescendo. Le tempo est donné par la respiration de Nina, pas par la première croche. Les do♯ et sol♯ sont serrés (juste sous ré et la) : écoutez les violoncelles.

- **Violoncelles** : à la mes. 7 vous continuez seuls en croches (mes. 7–11), p, détaché au milieu, très régulier ; les vents se posent sur vous.
- **Contrebasses** : vous vous arrêtez net à la mes. 7 (« B. » silence) ; reprise avec le tutti à la mes. 12.

## Le premier tutti (mes. 12–17, puis 150–155) — ff

- Violons I et II : blanche ∏, puis les accords ∏ ∏ (reprise d’archet au talon).
- Altos, violoncelles, contrebasses : croches détachées à la corde, moitié inférieure, sans écraser ; le ff vient de la vitesse, pas de la pression.
- Le ff est sur la **première croche de la mes. 12** : regardez le premier violoncelle, qui regarde Nina.

## Le retour du p (mes. 18–28, puis 156–163)

Mêmes consignes qu’au début, dynamique p. Vous accompagnez la flûte et le hautbois solo : un cran en dessous d’eux.

## Les alternances f / p (mes. 36–41, puis 122–133)

Le f au talon (archet lourd, court), le p dans la moitié supérieure, immédiatement. Pas de transition entre les deux.

## Le second thème fp (mes. 59–74, puis 171–188)

- **Seconds violons et altos** : le fp est sur la **première croche de chaque mesure** ; dès la deuxième croche, p à la pointe. Croches parfaitement égales ensuite. Commencer ∏ sur la première croche.
- **Premiers violons** : tenues fp = archet rapide à l’attaque, puis quasi immobile ; la tenue est un fil, pas un mur.

## Les croches répétées (mes. 85–95, puis 198–209) — f

Violons I et II : huit croches par mesure, toutes identiques, archet au milieu, détaché à la corde. Aucune n’est plus forte que l’autre. La mélodie est aux altos, violoncelles et bassons : altos et violoncelles, chantez, ∏ sur la première note de chaque liaison.

## La coda (mes. 236–249) — pp puis crescendo

- Premiers violons (236), seconds (238), altos (240) : pp, pointe, sur la corde, **aucun crescendo avant la mes. 244**.
- Violoncelles et contrebasses : noires pp, courtes, sans accent.
- Mes. 244–249 : crescendo syllabé sur six mesures. Repères : 244 pp · 246 p · 248 mf · 250 f.

## Le tutti final (mes. 250–294)

- Traits descendants de la mes. 260 et des mes. 275–281 : détaché large, archet au milieu.
- Trilles (mes. 262–263, 276, 280) : commencer sur la note, terminer ensemble sur la levée de Nina.
- Mes. 284–289 (seconds, altos, violoncelles) : croches détachées, f sans dureté.
- Accords finaux (mes. 290–294) : tous ∏, reprise d’archet entre chaque accord ; la dernière note tenue sa valeur entière, coupée sur le geste de Nina.
"""},
{"id": "cordes-flute", "title": "Cordes — La Flûte enchantée : coups d’archet et consignes", "audience": "Violons I et II, altos, violoncelles, contrebasses", "markdown": r"""
**Notation :** ∏ = tiré, V = poussé. Vérifiez vos numéros de mesure : Adagio mes. 1–15, Allegro à partir de la mes. 16, triple accord mes. 97–102, réexposition mes. 144, fin mes. 226.

## L’Adagio (mes. 1–15) — f, puis contrastes

[[excerpt:zauberfloete/adagio_1_3]]

- Les trois accords (mes. 1–3) : ∏ du talon, l’archet **posé sur la corde avant la levée** de Nina, son plein et large, sans vibrato continu (un vibrato étroit et bref sur la tenue, décidé, est possible).
- Le silence après chaque accord est exact. La levée en doubles croches (V, courte) se joue **tard**, dans le tempo.
- Justesse : accord 1, mi♭ majeur, violons en double corde sol–mi♭ : le sol (tierce) un peu bas, **jamais la corde à vide**. Accord 2, do mineur. Accord 3 : mi♭ majeur avec le **sol à la basse** (altos, violoncelles, contrebasses) : très légèrement bas, parfaitement stable.
- Point d’orgue mes. 3 : Nina coupe, respire, et les premiers violons reprennent (triolet de triples croches, p, V léger).
- Mes. 4–15, rythme pointé : la noire pointée pleine, la croche courte et liée au temps suivant ; harmonies chromatiques : demi-tons serrés, écoutez la basse.

## Le fugato (mes. 16–38, puis 144–160) — p

[[excerpt:zauberfloete/fugato_16_27]]

- Entrées : seconds violons seuls mes. 16 ; premiers violons mes. 20 ; altos et violoncelles (avec les bassons) mes. 27 ; contrebasses mes. 33. À la réexposition : seconds mes. 144, premiers mes. 146, basses mes. 150–152.
- Les six croches répétées : détaché à la corde, au milieu, **six croches identiques** (ni la première accentuée, ni la dernière avalée). Commencer ∏.
- Les quatre doubles croches : même archet, détachées, claires, sans crescendo ; elles mènent à la croche suivante sans accent.
- Quand un autre pupitre entre, vous devenez accompagnement : **un cran en dessous, immédiatement**.
- Le tempo ne monte pas à chaque entrée : la blanche est celle de la respiration de Nina (environ 120).
- Mes. 20–21 (seconds violons), ligne chromatique : demi-tons réguliers, sans vibrato.

## Le tutti (mes. 39 et suivantes)

Le f des cordes reste articulé : archet au milieu, vitesse plutôt que pression. Les cuivres et la timbale entrent dans votre tempo.

## Le triple accord (mes. 97–102)

Vous ne jouez pas. Archets baissés, immobiles, regard sur Nina : c’est elle qui donne la levée aux vents, et c’est vous qui repartez à la mes. 103 (premiers violons, sujet p) dans le tempo exact de la mes. 16.

## Les sforzandi du développement (mes. 103–143)

Un sf dans piano est un petit accent : archet rapide sur la note, puis on relâche aussitôt. Le sujet (premiers violons 103, violoncelles 105, basses 109–123) passe toujours devant.

## La strette finale (mes. 209–226) — ff

Doubles croches articulées jusqu’au bout, archet au milieu, ff par la vitesse de l’archet. Accords finaux ∏, avec reprise ; sol (tierce de mi♭) bas ; la dernière note tenue sa valeur entière et coupée sur le geste de Nina.
"""},
{"id": "vents-cuivres-timbales", "title": "Vents, cuivres et timbales — consignes", "audience": "Flûtes, hautbois, clarinettes, bassons, cors, trompettes, trombones, timbales", "markdown": r"""
**Le relais des départs :** Nina dirige depuis le premier violon. Le **premier hautbois** relaie ses levées à tous les vents et cuivres ; la **timbale** regarde le premier violoncelle. Respirez avec le premier hautbois.

## Les Noces de Figaro

- **Bassons, mes. 1–7 et 139–145** (à l’unisson avec les cordes, pp) : vous êtes la seule voix de vent de ce passage. Écoutez les violoncelles, pas les violons ; attention à ne pas monter en pp (l’anche pincée monte). Liaisons comme écrites : léger appui sur la première note, la dernière s’allège. Pas de vibrato.
- **Hautbois et cors, mes. 8 ; flûtes et clarinettes, mes. 9 et 11** (p) : vous vous posez sur les croches des violoncelles, qui jouent seuls. Entrée sans accent, tenue droite, fin de note allégée.
- **Tutti, mes. 12 et 150** (ff) : la première croche de la mesure, pas avant. Trompettes et timbales : regardez le premier violoncelle. Timbale : coup sec, pas de roulement.
- **Flûte et hautbois « Imo », mes. 18–23 et 156–163** : vous êtes solistes ; les cordes sont un cran en dessous. Phrasez fort–faible.
- **Mes. 36–41 et 122–133** (fp) : attaque f puis p immédiat, sans decrescendo. Chaque accord a été accordé en chorale : retrouvez cette justesse en rythme.
- **Second thème, mes. 63 (hautbois), 66 (flûtes), 67 (bassons)** : chaque entrée est une couleur, pas un crescendo ; fp comme les cordes.
- **Tenues, mes. 85–95 et 198–209** : accord de la (dominante) puis ses voisins ; la tierce (do♯) basse, la quinte pure ; la pédale des violons est votre référence. Bassons : vous avez la mélodie avec les altos et les violoncelles : chantez.
- **Basson solo, mes. 105–121 et 213–219 ; flûte Imo mes. 116** : solistes, p, phrasé fort–faible ; les cordes vous accompagnent.
- **Coda, mes. 244–249** : le crescendo est syllabé sur six mesures : 244 pp · 246 p · 248 mf · 250 f. Trompettes et timbales : le f de 250 est une arrivée, pas une explosion.
- **Trilles, mes. 262–263, 276, 280** : commencer sur la note, terminer ensemble.

## La Flûte enchantée

- **Les trois accords, mes. 1–3** (f) : attaque avec les cordes, sur la respiration du premier hautbois ; son plein, pas de vibrato continu ; silence exact après chaque accord ; levée en doubles croches courte et tardive. Trombones : vous soutenez, vous ne couvrez pas.
- **Adagio, mes. 4–15** : rythme pointé (noire pointée pleine, croche courte) ; harmonies chromatiques accordées en chorale avant d’être jouées en rythme.
- **Fugato** : cors, flûtes et clarinettes entrent à la mes. 37 ; hautbois, trompettes, trombones et timbales à la mes. 39 (premier tutti f). Vous entrez **dans le tempo des cordes**. Le sujet (six croches + quatre doubles) se joue articulé, les six croches identiques.
- **Le triple accord, mes. 97–102** (si♭ majeur) : les cordes se taisent. Le premier hautbois respire, Nina donne la levée une noire avant. Trois fois : levée en double croche (courte, tardive), blanche pleine, blanche, silence. Tierce (ré) basse, fa pur ; trombones et timbale sous les hautbois. Timbale : roulement court, net.
- **Développement, mes. 103–143** : les sf sont relatifs à la nuance (un sf dans p est un petit accent). Bassons et basses : entrées du sujet mes. 109–123, toujours devant.
- **Réexposition, mes. 154–157** : tutti comme à la mes. 39, sans accélérer.
- **Strette finale, mes. 219–226** : cuivres un cran en dessous des cordes ; timbale sèche ; accords finaux de mi♭ majeur, sol bas ; dernière note tenue sa valeur entière, coupée sur le geste de Nina.
"""},
{"id": "style-classique", "title": "Style classique — mémo pour tous", "audience": "Tout l’orchestre", "markdown": r"""
## Vibrato

- Le vibrato est un **ornement**, pas un état : Leopold Mozart (1756) se moque de ceux qui tremblent sur chaque note « comme s’ils avaient une fièvre continuelle ».
- Réservé aux tenues expressives ; nul dans les traits, les croches répétées et les unissons.
- Quand il est employé : étroit, plutôt rapide, décidé, et il peut commencer après le début de la note.

## Fins de phrase

- La règle est **fort–faible** : la dernière note d’un groupe est plus légère que la première.
- Une appoggiature appuie, sa résolution s’allège.
- La dernière note sous une liaison est plus courte et plus douce.
- Une note suivie d’un silence se raccourcit avec élégance ; elle ne s’étouffe pas.

## Articulation

- Les croches sans signe se jouent **détachées, à la corde** (non legato), ni liées ni sautillées.
- Point = détaché ; trait = plus court et plus marqué.
- Les liaisons sont des phrasés : léger appui sur la première note, allègement vers la dernière.
- Les doubles croches rapides restent **articulées** quelle que soit la nuance : le ff vient de la vitesse de l’archet ou de l’air, pas de la pression.

## Nuances

- Les contrastes sont **subito et par paliers** : il n’y a pas de transition entre f et p quand elle n’est pas écrite.
- *fp* = attaque forte immédiatement suivie du piano. *sf* = accent **relatif** à la nuance en cours.
- Les crescendos ne se jouent que là où ils sont écrits. Dans *Figaro*, le seul est aux mes. 244–249, syllabé sur six mesures.
- Le pp est une couleur et une présence, pas une absence de son.

## Tempo et pulsation

- *Figaro* se compte **à deux** (Presto, ¢) : la limite du tempo est la clarté des croches.
- *La Flûte* : l’Allegro ne doit pas accélérer à chaque entrée du fugato.
- Le tempo est donné par la **respiration** de Nina, jamais par la première note de celui qui commence.

## Justesse

- La quinte s’installe ; la tierce majeure se place **dessous** ; la tierce mineure légèrement dessus.
- Écoutez la basse avant de placer votre note.
- Pas de vibrato pendant qu’on accorde un accord.
"""},
{"id": "intonation", "title": "Justesse — méthode et accords à travailler", "audience": "Tout l’orchestre, en particulier les chefs de pupitre", "markdown": r"""
## L’ordre d’accord (9h00)

1. Le la du premier hautbois.
2. Les vents, puis les cuivres.
3. Les contrebasses, les violoncelles, les altos, les violons.
4. Un accord parfait de ré majeur, puis de mi♭ majeur, tenu dix secondes chacun, basses d’abord.

## Les trois règles

- **La quinte est pure**, la tierce majeure se place en dessous de celle du piano (≈ 14 cents plus bas), la tierce mineure au-dessus (≈ 16 cents plus haut).
- **La basse d’abord** : personne ne place sa note avant d’avoir entendu les contrebasses et les violoncelles.
- **Sensible** : haute quand elle monte vers la tonique dans une mélodie ; basse quand elle est la tierce d’un accord de dominante tenu.

## La méthode « accord par accord »

Arrêt sur l’accord, tenu : contrebasses seules → violoncelles → voix du milieu → les tierces en dernier. Dix secondes par accord, trois accords au maximum d’affilée.

## Figaro

| Mesures | Ce qu’on travaille | Qui a la tierce / la sensible |
|---|---|---|
| 1–7, 139–145 | Unisson : une seule hauteur, référence = violoncelles ; do♯, sol♯, la♯, ré♯ serrés | — |
| 85–95, 198–209 | Tenues des vents sur la (dominante) puis ses voisins ; pédale des violons = référence | Tierce do♯ (vents) : basse |
| 122–133 | Accords fp alternés | Vérifier chaque accord en chorale |
| 290–294 | Accords finaux, ré majeur | Fa♯ : bas ; la : pur |

## La Flûte enchantée

| Mesures | Ce qu’on travaille | Qui a la tierce |
|---|---|---|
| 1 | Mi♭ majeur | Sol dans la double corde des violons : bas, **jamais à vide** |
| 2 | Do mineur | Mi♭ (tierce mineure) : légèrement haut |
| 3 | Mi♭ majeur, sol à la basse | Altos, violoncelles, contrebasses : sol très légèrement bas, stable |
| 4–15 | Harmonies chromatiques en rythme pointé | En chorale, sans rythme, puis en rythme lent |
| 20–21 | Ligne chromatique des seconds violons | Demi-tons serrés et réguliers |
| 97–102 | Si♭ majeur, vents et cuivres seuls | Ré : bas ; fa : pur ; trombones sous les hautbois |
| 219–226 | Accords finaux, mi♭ majeur | Sol : bas |

## Deux pièges d’instrument

- Les anches (hautbois, basson) montent en pp ; les flûtes descendent en pp et montent en ff.
- Les cordes à vide sont justes comme fondamentale ou quinte, pas comme tierce.
"""},
{"id": "ecoutes", "title": "À écouter avant la répétition", "audience": "Tout l’orchestre", "markdown": r"""
Écoutez au moins une version de chaque ouverture, partition ou partie sous les yeux, et notez le tempo (comptez les blanches sur dix mesures).

## Les Noces de Figaro, ouverture (≈ 4 minutes)

| Interprète | Année | Écouter pour |
|---|---|---|
| Nikolaus Harnoncourt, Concentus Musicus Wien | 1993 | L’articulation « parlée », les contrastes subito, les croches détachées à la corde |
| John Eliot Gardiner, English Baroque Soloists | 1993 | La légèreté des archets, le vibrato d’ornement, la coda pp |
| Claudio Abbado, Orchestra Mozart | 2011–2012 | L’équilibre d’un orchestre moderne dans le style |
| René Jacobs, Concerto Köln | 2003 | Le théâtre : tempo, accents, fp |

## La Flûte enchantée, ouverture (≈ 7 minutes)

| Interprète | Année | Écouter pour |
|---|---|---|
| Nikolaus Harnoncourt, Opernhaus Zürich | 1987 | Les trois accords, la lisibilité du fugato |
| John Eliot Gardiner, English Baroque Soloists | 1995 | Le tempo de l’Allegro, l’égalité des croches |
| Claudio Abbado, Mahler Chamber Orchestra | 2005 | Les tutti clairs, les trombones intégrés |
| René Jacobs, Akademie für Alte Musik Berlin | 2010 | Le triple accord, les sforzandi relatifs |

## Ce qu’il faut entendre

- Où commence et où s’arrête chaque nuance : le pp de *Figaro* (mes. 1 et 236), le crescendo de six mesures (244–249).
- Comment le sujet du fugato de *La Flûte* passe d’un pupitre à l’autre sans que le tempo bouge.
- La longueur exacte des silences entre les trois accords.
"""},
]

method = r"""
Les numéros de mesure de *Figaro* ont été relevés page par page sur la partition de la Neue Mozart-Ausgabe (Sinfonia, p. 5–28), et les hauteurs de l’extrait initial contrôlées sur deux encodages indépendants. Pour *La Flûte enchantée*, la structure (Adagio 1–15, Allegro 16–96, Adagio 97–102, Allegro 103–226) et les entrées du sujet ont été extraites par analyse automatique (music21) d’une édition de référence encodée, cohérente avec le compte de la NMA ; les numéros doivent être confirmés sur le matériel de l’orchestre. Les extraits sont gravés avec Verovio à partir de ces sources. Les durées et tempi des enregistrements sont indicatifs.
"""

final = {"guide_markdown": guide, "handouts": handouts, "excerpts": excerpts, "method_note": method,
         "sources_used": []}
OUT.write_text(json.dumps(final, ensure_ascii=False, indent=1), encoding="utf-8")
print("wrote", OUT, len(guide), "chars guide;", len(handouts), "handouts")
