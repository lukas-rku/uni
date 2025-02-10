---
title: Kombinatorische Logik
description: Lernzettel - Digitaltechnik
draft: false
date: 2025-02-10
tags:
---
## Abstrakte Eigenschaften logischer Schaltungen
- Eingänge
- Ausgänge
- Spezifikation des Funktionalen Verhaltens = realisierte (boole'sche Funktion)
- Spezifikation des Zeitverhaltens
![[Screenshot 2025-02-10 162540_inverted.png]]
## Komponenten einer logischen Schaltung
- Verbindungsknoten
	- Eingangs-Terminale: $A,B,C$
	- Ausgangs-Terminale: $Y,Z$
	- Interne Knoten: $n_1$
- Schaltungselemente
	- $E_1,E_2,E_3$
	- jedes selbst eine Schaltung $\rightarrow$ Hierarchie
	- Ein Modul, bspw. $E_1$, kann wieder ein Submodul sein.
![[Screenshot 2025-02-10 162833_inverted.png]]
## Arten von logischen Schaltungen
- kombinatorische Logik ("Schaltnetz")
	- Ausgänge hängen nur von aktuellen Eingangswerten ab
- sequentielle Logik ("Schaltwerk"%%Link Schaltwerk%%)
	- Ausgängen von aktuellen Eingangswerten und internen Zustand ab
	- Ausgänge indirekt abhängig von vorherigen Eingangswerten

## Eigenschaften kombinatorischer Logik
- jedes Schaltungselement ist selbst kombinatorisch
- jeder Verbindungsknoten ist
	- Eingang in die Schaltung, oder
	- and genau ein Ausgangsterminal ("Treiber") eines Schaltungselements angeschlossen
- jeder Pfad durch die Schaltung besucht jeden Verbindungsknoten maximal einmal (zyklenfrei)
![[Screenshot 2025-02-10 163139_inverted.png]]
