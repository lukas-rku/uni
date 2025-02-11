---
title: Zeitverhalten
description: Lernzettel - Digitaltechnik
draft: false
date: 2025-02-11
tags:
---
## Abstrakte Eigenschaften logischer Schaltungen
- Eingänge
- Ausgänge 
- Spezifikation der realisierten (boole'schen) Funktion = Funktionales Verhalten
- Spezifikation des Zeitverhaltens
![[Screenshot 2025-02-11 165632_inverted 1.png]]
## Zeitverhalten einer kombinatorischen Schaltung
- [[Kombinatorische Logik|Kombinatorisch]]: Werte der Ausgänge hängen nur von Werten an Eingängen ab
- reale Schaltungselemente benötigen aber endliche Zeit, um Änderung am Eingang auf Ausgang zu übertragen
	- z.B. für Umladen von [[Feldeffekt-Transistoren#MOS Feldeffekttransistoren (MOSFETs)|MOSFET]] Gate-Kapazitäten
	$\Rightarrow$ Zentrale Fragen
	- Wann sind die Ausgänge stabil?
	- Gibt es funktional äquivalente Schaltungen mit geringerer Verzögerung?
- Timing-Analyse anspruchsvoll, denn
	- Eingang kann Ausgang über verschiedene Pfade beeinflussen
	- Verzögerung kann für steigende/fallende Flanken unterschiedlich sein
	- Verzögerung im (Sub-)Nanosekundenbereich
![[Screenshot 2025-02-11 170031_inverted.png]]
## Ausbreitungs- und Kontaminationsverzögerung
- $t_{td}$ maximale Zeit vom Eingang zum Ausgang (Ausbreitungsverzögerung, propagation delay)
- $t_{cd}$ minimale Zeit vom Eingang zum Ausgang (Kontaminationsverzögerung, contamination delay)
![[Pasted image 20250211170432.png]]
- Ursachen für Verzögerung
	- Kapazitäten, Induktivitäten und Widerstände in der Schaltung
	- Lichtgeschwindigkeit als maximale Ausbreitungsgeschwindigkeit: 30cm / ns
- Warum können $t_{pd}$ und $t_{cd}$ unterschiedlich sein?
	- mehrere Ein- und Ausgänge mit unterschiedlich langen Pfaden
	- unterschiedliche Verzögerungen für steigende ($t_{pd,\:LH}$) und fallende ($t_{pd,\:HL}$) Flanken
	- Schaltungen werden
		- langsamer bei Erwärmung (Hitze erhöht den Widerstand des Leitfähigen Materials)
		- schneller bei Abkühlung
## Kritische (lange) und kurze Pfade
![[Pasted image 20250211173432.png]]
![[Pasted image 20250211173528.png]]
Da $\text{max}(\dots)$ genutzt wird, ist $t_{pd,\:Y}=2t_{pd,\:AND}+t_{pd,\:OR}$ , weil dieser Pfad länger ist als die anderen. Genau so auch bei $\text{min}(\dots)$, allerdings umgekehrt und mit der Kontaminationsverzögerung (cd) anstelle der Ausbreitungsverzögerung (pd):
![[Screenshot 2025-02-11 173816_inverted.png]]
## Störimpulse (Glitches)
- eine Änderung eines Eingangs verursacht mehrere Änderungen des Ausgangs
- können durch geeignete Entwurfsdisziplin entschärft werden:
	- Ausgänge nur zu bestimmten Zeiten auswerten (synchroner Entwurf)
	- Pfade modifizieren / hinzufügen
	- nicht alle Störimpulse können eliminiert werden (z.B. gleichzeitiges Schalten mehrerer Eingänge)
- können durch Timing- und Karnaugh Diagramme analysiert werden
## Beispiel für Störimpuls: Erkennen
- Was passiert, wenn $(A,B,C)$ von $0,1,1$ nach $(0,0,1)$ schaltet?
- Ausbreitungsverzögerung [[Logikgatter#NOT|NOT]] / [[Logikgatter#OR|OR]]: $t_{pd,\:NOT/OR}=1$
- Ausbreitungsverzögerung [[Logikgatter#AND|AND]]: $t_{pd,\:AND}=2$
![[Screenshot 2025-02-11 174415_inverted.png]]
Man kann sehen, dass $n_1$ nach einer Zeiteinheit von `0` auf `1` springt, nachdem sich $B$ geändert hat. Danach springt das obere AND Gatter nach zwei Zeiteinheiten von `0` auf `1`, allerdings erst nachdem das vorherige NOT Gatter sich mit $n_1$ geändert hat. Das untere AND Gatter springt von `1` auf `0` ebenfalls nachdem sich $B$ geändert hat zusätzlich zu den zwei Zeiteinheiten.

Jetzt das Interessante: Da $n_3$ geändert hat, springt das OR Gatter zurecht auf `0`. Allerdings ändert sich ja dann leicht Zeitverzögert auch $n_2$ und das OR Gatter springt wieder zurück auf `1`. Das Verhalten des OR Gatters war hier völlig normal und nicht fehlerhaft, allerdings kam es trotzdem zu einem Störimpuls, da $n_2$ leicht zeitverzögert nach $n_3$ geschaltet hat.

## Beispiel für Störimpuls: Beheben
- Kritische Stelle im [[Karnaugh Diagramme|Karnaugh-Diagramm]] mit zusätzlichen Implikanten $\overline A \: C$ überdecken
![[Screenshot 2025-02-11 175925_inverted.png]]
Der Störimpuls ist im Karnaugh-Diagramm zwischen `00 1` und `01 1` aufgetreten. Um das zu Verhindern kann man einfach einen weiteren Primimplikanten hinzufügen, welcher während der Änderung des Zustands als Puffer agiert.