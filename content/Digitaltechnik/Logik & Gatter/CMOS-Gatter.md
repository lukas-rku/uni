---
title: CMOS-Gatter
description: Lernzettel - Digitaltechnik
draft: false
date: 2025-02-10
tags:
---
## Kombinieren komplementärer Transistoren
- [[Feldeffekt-Transistoren#pMos|pMOS]] Transistoren leiten `1`'en "gut" von Source nach Drain weiter
	- Source an $V_{DD}$ anschließen
- [[Feldeffekt-Transistoren#nMos|nMOS]] Transistoren leiten `0`'en "gut" von Source nach Drain weiter
	- Source an GND anschließen

- Complementary Metal-Oxide-Semiconductor (CMOS) Logik
![[Screenshot 2025-02-10 144112_inverted.png]]
- Das pull-u==p== Netz wird aus ==p==Mos-Transistoren gebaut
- Das pull-dow==n== Netz wird aus ==n==Mos-Transistoren gebaut

## Beispiel anhand von [[Logikgatter#NOT|NOT]]
![[Screenshot 2025-02-10 144639_inverted.png]]
## Beispiel anhand von [[Logikgatter#NAND|NAND]]
![[Screenshot 2025-02-10 150342_inverted.png]]
## Struktur eines CMOS Gatters
Immer wenn man "[[CMOS-Gatter#Kombinieren komplementärer Transistoren|oben]]" pMOS Transistoren parallel schaltet, muss man unten die nMOS Transistoren in Serie schalten.
- pMOS Parallelschaltung $\leftrightarrow$ nMOS Serienschaltung
- pMOS Serienschaltung $\leftrightarrow$ nMOS Parallelschaltung

## Aufbau eines [[Logikgatter#NOR|NOR]]-Gatters mit drei Eingängen
![[Screenshot 2025-02-10 151448_inverted.png]]
Problem bei hoher Anzahl an Transistoren (hier als Veranschaulichung übertrieben):
- Bei Stromverlust bei jedem Transistor leidet die Ausgangsspannung
- Irgendwann kippt die Ausgangsspannung unter die [[Spannungen als Logikpegel|akzeptierte]
- ] Spannung $V_{IH}$

## Pseudo-nMOS Gatter
- Ersetzen des Pull-Up Netzes durch schwachen, immer eingeschalteten pMOS
	- Pull-Up kann durch das Pull-Down Netz "überstimmt" werden
- nützlich, um lange Reihen von Transistoren zu vermeiden
![[Screenshot 2025-02-10 152011_inverted.png]]
## Beispiel für Pseudo-nMOS Gatter
- Pseudo-nMOS NOR5
- verbraucht aber mehr Energie: schwacher Dauerkurzschluss bei Y = 0
![[Screenshot 2025-02-10 152130_inverted.png]]
## Transmissionsgatter
- nMOS leitet `0`'en gut von Source nach Drain weiter
- pMOS leitet `1`'en gut von Source nach Drain weiter
- Transmissionsgatter ist ein besserer Schalter
	- leitet `0`'en und `1`'en gut weiter
- $\text{EN}=1$ und $\overline{\text{EN}}=0\;\;\rightarrow$ Schalter ist EIN (A mit B verbunden)
- $\text{EN}=0$ und $\overline{\text{EN}}=1\;\;\rightarrow$ Schalter ist AUS (A nicht mit B verbunden)