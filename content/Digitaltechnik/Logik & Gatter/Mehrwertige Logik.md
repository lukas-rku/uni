---
title: Mehrwertige Logik
description: Lernzettel - Digitaltechnik
draft: false
date: 2025-02-11
tags:
---
## Einführung
- bisher galt:
	- jeder Schaltungsknoten (außer Eingänge) wird von *genau einem* Schaltungselement von `0` auf `1` getrieben
	- Axiome der [[Boole'sche Algebra|boole'schen Algebra]] basieren auf $\mathbb{B}=\{0,1\}$
- ignoriert wichtige Teile der Realität
	-  Wie breiten sich ungültige Spannungen in einer Schaltung aus?
- Unterscheidung von zwei weiteren Logikwerten neben `0` und `1`
	- $X$ mehrfach getrieben: fehlerhaft
	- $Z$ ungetrieben / hochohmig (high impedance): geziehlt
- Achtung:
	- nicht mit [[Karnaugh Diagramme#Karnaugh Diagramm mit "Don't Cares"|"Don't Cares"]] (`*`) verwechseln
	- tatsächliche Spannung kann auch im `0` oder `1` Bereich liegen, das Schaltungsdesign stellt dies aber nicht sicher
## X (mehrfach getrieben) bei Konkurrierenden Ausgängen
- mehrere (unabhängige) Treiber für den selben Schaltungsknoten
- Konflikt, sobald Treiber in entgegengesetzte Richtung ziehen
	- instabil: abhängig von Betriebsspannung, Temperatur etc.
	- destruktiv: Kurzschluss verursacht hohen Energieverbauch
- fast immer ein Entwurfsfehler
	- z.B. doppelte Zuweisung in Hardwarebeschreibung (`Unresolved net/uwire cannot have multiple drivers.`)
	$\Rightarrow$ Konflikt-Quelle muss in Simulation leicht nachvollziehbar sein
![[../../assets/Pasted image 20250211182253.png]]
## Z (ungetrieben / hochohmig) bei Tristate-Buffer
- zusätzliches Enable-Signale EN an Buffer
	- EN = `1`: Funktion wie normaler Buffer
	- EN = `0`: Ausgang hochohmig (offen, ungetrieben, floating, high-impedance) Z
- Achtung: $Z\not=0$
![[../../assets/Pasted image 20250211182430.png]]
## Bus mit Tristate-Buffern
- mehrere Treiber an gemeinsamer Leitung
- zu jedem Zeitpunkt genau ein aktiver Treiber
- erlaubt Wechsel der Kommunikationsrichtung
![[../../assets/Pasted image 20250211182538.png]]
Wenn bspw. $en_1$ auf `1` Schaltet, dann kann der Prozessor auf den Bus "schreiben". Währenddessen können alle anderen Bauteil zuhören, aber da ihr Tristate-Buffer auf hochohmig geschaltet ist, senden sie nichts. Wenn man allerdings mehrere auf `1` schaltet hat man ein Problem. Das wäre ein Entwurfsfehler.
## Tristate-Buffer für Multiplexer
![[../../assets/Pasted image 20250211182936.png]]
## Mehrwertige Logik in Schaltnetzen
- Resolutionstabllen definieren Ausbreitung von $X$ (mehrfach getrieben) und $Z$ (hochohmig)
- mehr Konvention (für Simulator) als physikalische Realität
- z.B. IEEE 1164:
![[../../assets/Pasted image 20250211183106.png]]
Zweite Zeile der linken Tabelle: Wenn $A$ `0` ist, dann ist $Y$ für $B=X$ `X`, für $B=0$ `0`, für $B=1$ `X` und für $B=Z$ `0`. So liest man den rest der Tabellen ebenfalls.