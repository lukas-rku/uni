---
title: Bubble-Pushing
description: Lernzettel - Digitaltechnik
draft: false
date: 2025-02-11
tags:
---
## Graphische Umformung von Schaltungen
Nach [[Boole'sche Algebra#T12 De Morgan|De Morgan]] und [[Boole'sche Algebra#T4 Involution|Involution]]
![[Pasted image 20250211144831.png]]
## Invertierungsblasen verschieben
- über Gatter ([[Logikgatter#AND|AND]] / [[Logikgatter#OR|OR]] / [[Logikgatter#NOT|NOT]] / [[Logikgatter#BUF|BUF]]) hinweg
	- vorwärts: Eingang $\rightarrow$ Ausgang
	- rückwärts: Ausgang $\rightarrow$ Eingang
	- Art des Gatters ändern: AND $\leftrightarrow$ OR
	- Blasen al *allen* Eingängen ändern: vorhanden $\leftrightarrow$ nicht vorhanden
	- Blase an Ausgang ändern: vorhanden $\leftrightarrow$ nicht vorhanden
- zwischen Gattern
	- vorwärts: Treiber $\rightarrow$ *alle* Empfänger
	- rückwärts: *alle* Empfänger $\rightarrow$ Treiber
	- doppelte Blasen heben sich gegenseitig auf (Involution)
- verbleibende Buffer (vorher Inverter) können entfernt werden

## Beispiel
![[Pasted image 20250211145333.png]]
- De Morgan über G3
	- Blase am Ausgang $\rightarrow$ Blase an beiden Eingängen
	- AND $\rightarrow$ OR
![[Pasted image 20250211145440.png]]
- Blasen entlang der Leitungen verschieben
	- G3 $\rightarrow$ G1
	- G3 $\rightarrow$ G2 (Doppelblase aufheben)
![[Pasted image 20250211145526.png]]
- De Morgan über G1
	- Blasen an Ein- und Ausgängen invertieren
	- OR $\rightarrow$ AND
- Buffer G2 entfernen
![[Pasted image 20250211145611.png]]
- Zwei Inverter weniger

## Anwendungen
- Schaltungen vereinfachen
	- weniger Inverter
	- weniger Literale (z.B. nur $A$ statt $A, \overline A$)
	- weniger verschiedene Gatter-Arten
		- einfachere Zellbibliothek (z.B. nur AND, kein OR)
- Komplementäre Schaltungen für [[CMOS-Gatter|CMOS]]-Schaltungen ableiten
	- $Y$ für Pull-Up Netzwerk $\leftrightarrow$ $\overline Y$ für Pull-Down Netzwerk
	- $Y=\overline AB+C$
	- $\overline Y=\overline{\overline A B+C}=\overline{\overline A B}\overline C=(A+\overline B)\overline C$
