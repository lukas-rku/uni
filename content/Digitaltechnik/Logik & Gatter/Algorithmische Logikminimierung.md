---
title: Algorithmische Logikminimierung
description: Lernzettel - Digitaltechnik
draft: false
date: 2025-02-11
tags:
---
## Beispiele für Verfahren zur Logikminimierung
- [[Boole'sche Algebra|Algebraisch]]
	- Umformen nach [[Boole'sche Algebra#Axiome der boole'schen Algebra|Axiome]]/[[Boole'sche Algebra#Theoreme der boole'schen Algebra|Theoremen]]
- Grafisch
	- [[Karnaugh Diagramme|Karnaugh Diagramme]]
- Algorithmisch
	- exakt: Quine-McCluskey
	- heuristisch: Espresso
	$\Rightarrow$ Minimiere Anzahl der zur Darstellung einer Funktion notwendigen Implikanten
## Verwendbarkeit der Verfahren
- Grafische Verfahren
	- für viel (> 6) Eingänge nicht mehr praktikabel
	- keine Optimierung zwischen Ausdrücken für mehrere Ausdrücke
- Quine-McCluskey-Methode
	- berechnet zunächst alle möglichen Implikanten
	- ermittelt danach minimale Teilmenge für vollständige Überdeckung
	$\Rightarrow$ Rechenzeit steigt exponentiell in der Anzahl der Einträge
$\Rightarrow$ für wirklich große Probleme (> Variablen) Heuristiken sinnvoll
- geringere Laufzeitkomplexität
- geringere Lösungsqualität
## Espresso-Heuristik
- in 1980er Jahren von IBM und UC Berkeley entwickelt
- unterstützt auch mehrere (zusammen optimierte) Ausgänge
- Details des Algorithmus hier nicht relevant
- hier nur Anwendung einer konkreten Implementieruing
	- [https://embedded.eecs.berkeley.edu/pubs/downloads/espresso](https://embedded.eecs.berkeley.edu/pubs/downloads/espresso)
	- spezielles Dateiformat für boole'sche Funktionen
	- erlaubt auch exakte Minimierung (als Referenz für Heuristik):
		- `espresso -D exact    input.esp > output.esp`
		- `espresso -D ESPRESSO input.esp > output.esp`

## Espresso Minimalbeispiel
```python
.i 2    # Anzahl Eingänge
.o 1    # Anzahl Ausgänge

00 0    # Ausgang 0 optional  
01 1
10 1
11 0    # Ausgang 0 optional
```
## Espresso Dateiformat
- jede Zeile beschreibt einen Implikanten mit $n_i$ Zeichen...
	- `0` Eingang negiert im Implikanten
	- `1` Eingang nicht-negiert im Implikanten
	- `-` Eingang nicht im Implikanten (kein Minterm)
- ... und $n_0$ Ausgangsfunktionen mit je einem Zeichen
	- `0` Implikant im off set des Ausgangs (optional)
	- `1` Implikant im on set des Ausgangs
	- `-` Implikant im on set oder off set des Ausgangs (Don't Cares)
## Anwendungsbeispiel: 7-Segment Anzeige
$\mathbb{B}^4\rightarrow\mathbb{B}^7$
- (Typischerweise) vier Eingänge für dargestellte Ziffer
- Sieben unabhängig schaltbare Segmente $S_0,\dots,S_6$
	$\Rightarrow$ jedes Segment nur für bestimmte Zeichen aktiv

![[Screenshot 2025-02-11 164056_inverted.png]]
## 7-Segment Anzeige
Wahrheitstabelle
![[Pasted image 20250211164157.png]]
## 7-Segment Anzeige in Espresso
Eingabedateien
```python
.i 4
.o 7
0000 1111110
0001 0110000
0010 1101101
0011 1111001
0100 0110011
0101 1011011
0110 1011111
0111 1110000
1000 1111111
1001 1111011
1010 -------
1011 -------
1100 -------
1101 -------
1110 -------
1111 -------
```
## Espresso Dezimale 7-Segment Anzeige
Ausgabedateien
```python
.i 4
.o 7
.p 9
-0-0 1001100
-0-1 0110000
--10 1001100
-01- 0101001
-1-0 0010011
--11 1110000
--00 110010
-101 1011011
1--- 1001011
.e
```
