---
title: Kombinatorische Logik in SystemVerilog
description: Lernzettel - Digitaltechnik
draft: false
date: 2025-02-10
tags:
---
## Module
- Ein Modul beschreibt wie eine Aufgabe (Berechnung) durchgeführt wird
	- Ähnlich einer Funktion in Programmiersprachen
- Schnittstellenbeschreibung:
	- Eingänge
	- Ausgänge
	- (Parameter)
- zwei Arten von Modul-Beschreibungen:
	- Strukturbeschreibung: Wie ist die Schaltung aus (Sub-)Modulen aufgebaut?
	- Verhaltensbeschreibung: Was tut die Schaltung
- strukturelle Modul-Hierarchie mit Verhaltensbeschreibung auf unterster Ebene
![[Screenshot 2025-02-10 164334_inverted.png]]
## Beispiel für Verhaltensbeschreibung
```verilog
module example(input logic a, b, c, output logic y);

	assign y = ~a & ~b & ~c | a & ~b & ~c | a & ~b & ~c;

endmodule
```

^452699

| Bezeichnung       | Beschreibung                                                                                                                                                                                                                                   |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `module`          | Beginn der Schnittstellenbeschreibung                                                                                                                                                                                                          |
| `example`         | Modulname                                                                                                                                                                                                                                      |
| `input`, `output` | Port-Richtung                                                                                                                                                                                                                                  |
| `logic`           | Port-Datentyp                                                                                                                                                                                                                                  |
| `a, b, c, y`      | Port-Namen                                                                                                                                                                                                                                     |
| `assign`          | ([[Kombinatorische Logik\|kombinatorische]]) Signalzuweisung                                                                                                                                                                                   |
| `~`, `&`, \|      | ([[Kombinatorische Logik\|kombinatorische]]) Operatoren ([[Logikgatter#NOT $ mathbb{B} rightarrow mathbb{B}$\|NOT]], [[Logikgatter#AND $ mathbb{B} 2 rightarrow mathbb{B}$\|AND]], [[Logikgatter#OR $ mathbb{B} 2 rightarrow mathbb{B}$\|OR]]) |
| `endmodule`       | Ende der Schnittstellenbeschreibung                                                                                                                                                                                                            |
*Man kann eine beliebige [[Kombinatorische Logik|kombinatorische Logik]] eins zu eins abtippen.*
## Simulation von Verhaltensbeschreibungen
Plot mit Opensource Tools `Icarus Verilog` + `GTKWave`
![[Screenshot 2025-02-10 165555_inverted.png]]
Man kann sehen, dass die [[Boole'sche Gleichungen#Minterm|Minterme]] von [[Kombinatorische Logik in SystemVerilog#^452699|example]] bei der ersten, fünften und sechsten Zeiteinheit bei `y = 1` sind.
## Synthese von Verhaltensbeschreibung
Plot mit Open-Source Tools `YoSyS` + `GraphViz`
![[Screenshot 2025-02-10 170304_inverted.png]]