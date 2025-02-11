---
title: Logik-Realisierung mit Basis-Gattern
description: Lernzettel - Digitaltechnik
draft: false
date: 2025-02-11
tags:
---
## Zweistufige Logik
![[../../assets/Pasted image 20250211150829.png]]
- direkte (konstruktive) Umsetzung der disjunktiven Normalform (DNF)
	- Eingangsliterale: ein Inverter pro Variable (falls benötigt)
	- Minterme: je ein "breites"[[Logikgatter#AND|AND]] Gatter and passende Literale anschließen
	- Summe: alle Minterme an ein "breites" [[Logikgatter#OR|OR]] Gatter anschließen
- Gatter mit vielen Inputs als Bäume, kleinerer Gatter
	- jede boole'sche Funktion realisierbar mit Basisgattern 
		- [[Logikgatter#AND|AND2]]
		- [[Logikgatter#OR|OR2]]
		- [[Logikgatter#NOT|NOT]]
![[../../assets/Pasted image 20250211150934.png]]
## Konventionen für lesbare Schaltpläne
- Eingänge links (oder oben)
- Ausgänge rechts (oder unten)
- Gatter von links nach rechts (oben nach unten) angeordnet
- gerade (oder rechtswinklige) Verbindungen
	- keine Schrägen oder Kurven
- 3-armige Kreuzungen gelten implizit als verbunden
- 4-armige Kreuzungen gelten nur bei Markierung (Punkt) als verbunden
![[../../assets/Pasted image 20250211151313.png]]
## Weitere kombinatorische Grundelemente
- zweistufige Logik
	- sehr mächtig
	- aufwändige Darstellung und Realisierung
	- realisiertes Verhalten nicht intuitiv ersichtlich
- weitere Basisgatter neben AND, OR, NOT:
	- [[Logikgatter#XOR|XOR]]: Parität
	- Multiplexer (MUX): $n$ zu $1$ %%Link Multiplexer MUX%%
	- Dekodierer (DEC): $n$ zu $n^2$ %%Link Dekodierer DEC%%
