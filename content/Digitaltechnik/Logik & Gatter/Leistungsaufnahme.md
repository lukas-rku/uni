---
title: Leistungsaufnahme
description: Lernzettel - Digitaltechnik
draft: false
date: 2025-02-10
tags:
---
## Übersicht
- alternative Begriffe: Leistungsumsatz, Leistungsverbrauch
- Leistung = Energieverbrauch pro Zeiteinheit
- zwei Arten der Leistungsaufnahme
	- statische Leistungsaufnahme
	- dynamische Leistungsaufnahme

## Statische Leistungsaufnahme
- Leistungsbedarf wenn kein Gatter schaltet
- verursacht durch Leckstrom $I_{DD}$
	- immer kleinere Transistoren schalten nicht mehr vollständig ab
	- [[CMOS-Gatter#Pseudo-nMOS Gatter|Pseudo-nMOS]], ...
- statische Leistungsaufnahme ist also $P_{\text{static}}=I_{DD}\cdot V_{DD}$

## Dynamische Leistungsaufnahme
- Aufladen der Gate-Kapazität $C$ von $0A$'s auf $Q=C\cdot V_{DD}$
- Schaltung wird mit Frequenz $f$
	- Transistoren schalten $f$-mal pro Sekunde
- nur die Hälfte davon sind Aufladungen
- $I=\frac{Q}{t}=Q\cdot\frac{f}{2}=C\cdot V_{DD}\cdot\frac{f}{2}$
- dynamische Leistungsaufnahme ist:
	- $P_{\text{dynamic}}=I\cdot V=(C\cdot V_{DD}\cdot\frac{f}{2})(V_{DD})=\frac{1}{2}C\cdot V^2_{DD}\cdot f$

## Beispielrechnung Leistungsaufnahme
![[Screenshot 2025-02-10 154141_inverted.png]]