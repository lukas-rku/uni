---
title: Logikgatter
description: Lernzettel - Digitaltechnik
draft: false
date: 2025-02-10
tags:
---
## Binärwerte als Spannungspegel
Definiere Spannungspegel für die Werte `0` und `1`
- Logikpegel (logic levels)
- Beispiel:
	- 0 V $\mapsto$ `0` (Erde, GND, $V_{SS}$ "Voltage Source Source")
	- 5 V $\mapsto$ `1` (Versorgungsspanung, $V_{DD}$ "Voltage Drain Drain")
- aber: reale Spannungspegel unterliegen Rauschen
	- Temperaturabhängige Widerstände
	- Instabile Betriebsspannungen
	- Übersprechen zwischen benachbarten Leitungen

## Beispiel für Rauschen
![[Screenshot 2025-02-10 132921_inverted.png]]
- Ausgang eines Gatters ("Treibers") treibt Ausgangsleitung auf 5 V
- lange Leitung zum nächsten Gatter ("Empfänger") hat hohen Widerstand
- Spannungsabfall bspw.  0,5 V
- Empfänger sieht nur 4,5 V
- Soll immer noch als `1` zählen

## Binärwerte als Spannungsbereiche
- definiere Spannungsbereiche für die Werte `0` und `1` 
- steigere Robustheit durch unterschiedliche Bereich für Ein-/Ausgänge
	- $V_{OH}$: kleinste Spannung, die der Treiber als `1` ausgibt ("Voltage Output High")
	- $V_{IH}$: kleinste Spannung, die der Empfänger als `1` interpretiert ("Voltage Input High")
	- $V_{IL}$: größte Spannung, die der Empfänger als `0` interpretiert ("Voltage Input Low")
	- $V_{OL}$: größte Spannung, die der Treiber als `0` ausgibt ("Voltage Output Low")

## Störabstände
![[Screenshot 2025-02-10 133508_inverted.png]]
Die niedrigste Spannung, die der Ausgangsbereich für `1` ausgibt ($V_{OH}$), sollte immer höher als die niedrigste Spannung, die der Eingangsbereich als `1` interpretiert ($V_{IH}$), sein. Genau so sollte auch die höchste Spannung, die für `0` ausgegeben wird ($V_{OL}$), niedriger sein als die Spannung, die vom Eingangsbereich für `0` interpretiert wird ($V_{IL}$).

- oberer Störabstand $NM_H = V_{OH}-V_{IH}$ ("Noise Margin High")
- unterer Störabstand $NM_L=V_{OL}-V_{IL}$ ("Noise Margin Low")

## Gleichstrom-Transferkurve
![[Screenshot 2025-02-10 134511_inverted.png]]
In der Realität kann ein elektronisches Bauteil, hier ein [[Logikgatter#BUF $ mathbb{B} rightarrow mathbb{B}$|Buffer]], niemals Problemlos funktionieren. Daher werden hier auch wieder Störabstände eingesetzt, damit der Empfänge die Signale richtig interpretiert. Hier sieht man, dass ein Buffer, der mit Strom gefüttert wird, schon vor seinem "Wechselpunkt" anfängt leicht zu leiten und auch nachträglich abflacht.
![[Screenshot 2025-02-10 135111_inverted.png]]
## Absenken der Versorgungsspannung $V_{DD}$
- $V_{DD}=5V$ in 1970er-80er Jahre
- Verbesserte Chip-Fertigungstechnologie erfordert / ermöglicht Absenkung
	- hohe Spannung würden immer kleinere Transistoren beschädigen
	- Energiebedarf reduzieren
	- $3.3V\rightarrow2.5V\rightarrow1.8V\rightarrow1.5V\rightarrow1.2V\rightarrow1.0V$
- Vorsicht beim Verbinden mit Chips mit unterschiedlichen Versorgungsspannungen!

## Logikfamilien mit kompatiblen Spannungspegeln
- Die Spannungspegel für bestimmte Bauteile sind fest definiert.