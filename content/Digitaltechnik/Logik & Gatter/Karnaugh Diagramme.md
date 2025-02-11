---
title: Karnaugh Diagramme
description: Lernzettel - Digitaltechnik
draft: false
date: 2025-02-11
tags:
---
## Graycode
![[Pasted image 20250211154733.png]]
- Aufzählung von Binärzahlen einer festen Breite $k$, wobei sich (zyklisch) benachbarte Zahlen nur um ein Bit unterscheiden
![[Pasted image 20250211154822.png]]
- Konstruktion: Graycode für $k+1$ aus Graycode für $k$ mit Prefix $0$, dann umgekehrt Graycode für $k$ mit Prefix $1$.
![[Pasted image 20250211154916.png]]
## Karnaugh Diagramme
- [[Boole'sche Algebra|boole'sche Ausdrücke]] können durch Zusammenfassen von [[Boole'sche Gleichungen#Minterm|Mintermen]] minimiert werden
	- $Y=AB+A\overline B=A=A\cdot(B+\overline B)=A\cdot 1=A$
- Karnaugh Diagramme stellen Zusammenhänge graphisch dar
	- Anordnung der Wahrheitswertetabelle via Graycode
		$\Rightarrow$ zusammenhängende Minterme besser erkennbar
![[Screenshot 2025-02-11 155224_inverted.png]]
## Karnaugh Diagramm für drei Eingänge
![[Pasted image 20250211155441.png]]
*Man versucht die "Blasen" möglichst groß zu machen, allerdings dürfen die Blasen nur viereckig sein. Ein Kästchen kann mehrfach markiert werden.*
## Abdeckung von Mintermen durch Implikanten
- $n$ Eingangsvariablen
- Implikant aus $k\le n$ Literalen deckt $2^{n-k}$ Minterme ab
- Primimplikant
	- nicht vergrößerbare zusammenhängende viereckige Fläche im Karnaugh Diagramm
	- Achtung: Umbruch an Rändern beachten
**Achtung:**  Rechteckige Flächen sind nur dann erlaubt, wenn die Anzahl ihrer Kästchen gerade ist!
## Karnaugh Diagramm mit für Eingängen
![[Pasted image 20250211161519.png]]
*Ein einer Block hat vier Literale, ein zweier Block hat drei Literale, ein vierer Block hat drei Literale und ein achter Block hat ein Literal.*
## Karnaugh Diagramm mit "Don't Cares"
![[Pasted image 20250211161831.png]]
## Minimierungsregeln für Karnaugh Diagramme
- Eintragen von Mintermen
	- Einsen aus Wahrtstabelle
	- "Don't Cares" (`*`) für ungültige Eingangskombinationen
- Markieren von Implikanten
	- markierte Bereiche dürfen nur `1` und `*` enthalten, aber keine `0`
	- nur Rechtecke mit $2^k$ Einträgen erlaubt (keine L- oder Z-Formen)
	- Bereiche dürfen sich überschneiden
	- Bereiche dürfen um die Ränder des Diagrammes herum reichen (Torus)
	- Bereiche müssen so groß wie möglich sein (Primimplikanten)
- Ziel: Überdeckung aller Einsen mit möglichst wenigen Primimplikanten