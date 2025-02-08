---
title: Funktionale Abstraktion
description: Lernzettel - funktionale und objektorientierte Programmierung
draft: false
date: 2025-02-08
tags:
---
## Übersicht
- Diverse Konzepte von Java gehören zu den funktionales Programmierkonzepten.
- Diese Konzepte sind grundlegend für funktionale Programmiersprachen.
- Betrachtet wird hier die beispielhaft gewählte Programmiersprache `HtDP-TL`, als Variante von `Racket` und `Scheme`

- Im Gegensatz zu Referenztypen und ihren Objekten bei der [[Objektorientierte Abstraktion|objektorientierten Abstraktion]], sind Funktionen hier die zentralen Bausteine:
	- $f: D_1 \times D_2 \times \text{...} \times D_n \rightarrow R$
- Programmdesign:
	- Zerlegung der zu erstellenden Funktionalitäten in Funktionen.
	- Funktionen rufen andere, grundlegendere Funktionen auf.
- Funktionen werden variiert durch Parameter, die ihrerseits Funktionen sind.