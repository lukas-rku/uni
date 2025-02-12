---
title: Arithmetische Grundschaltungen
description: Lernzettel - Digitaltechnik
draft: false
date: 2025-02-12
tags:
---
## Shifter
- $A$ um $B$ nach links/rechts verschieben
- Strategien zum Auffüllen der freien Stellen (Beispiele unten sind für $B=1$)
	- logischer Rechts- oder Linksshift: Auffüllen mit Nullen
	- umlaufender Rechts- oder Linksshift: Auffüllen mit den aus der anderen Seite herausfallenden Bits (Rotation)
	- arithmetischer Rechtsshift: Auffüllen mit Vorzeichen des als [[../Zahlensysteme/Zahlensysteme#Definition: Zweierkomplement|Zweierkomplement]] interpretierten Dateneingangs (entspricht Division durch $2^B$)
	- arithmetischer Linksshirt: Auffüllen mit Nullen (entspricht Multiplikation mit $2^B$)
![[../../assets/Pasted image 20250212094123.png]]

## Barrel-Shifter
Arithmetic Right
![[../../assets/Screenshot 2025-02-12 094640_inverted.png]]
Minimierte Schaltung ($Y_3$ ist immer $A_3$ usw.)
![[../../assets/Pasted image 20250212094814.png]]
## Arithmetische Shifter als Multiplizierer und Dividierer
- Arithmetischer Linksshift um $n$ Stellen multipliziert den Zahlenwert mit $2^n$
	- $00001_2<<<3=01000_2=1\cdot2^3=8$
	- $11101_2<<<2=10100_2=-3\cdot2^2=-12$
	- *Man kann nicht zu weit schieben, da sonst das Vorzeichen verloren geht.*
- Multiplikation mit Konstanten kann aus Arithmetischen Linksshift und Additionen zusammengesetzt werden
	- $a\cdot6=a\cdot110_2=(a<<<2)+(a<<<1)=(a\cdot2^2)+(a\cdot2^1)=4a+2a$
- Arithmetischer Rechtsshift um $n$ Stellen dividiert den Zahlenwert durch $2^n$
	- $010000_2>>>4=000001_2=16/2^4=1$
	- $100000_2>>>2=111000_2=-32/2^2=-8$

## Ripple-Carry-Adder (RCA)
$$
\begin{align*}
&\text{Summand: }&1011& \quad C_4&C_3& \quad C_2&C_1& \quad C_0\\
&\text{Summand: }&+1011&&A_3& \quad A_2&A_1& \quad A_0\\
&\text{Übertrag: }&10110&&B_3& \quad B_2&B_1& \quad B_0\\
&&\text{-------}\\
&\text{Summe: }&=10110& \quad S_4&S_3& \quad S_2&S_1& \quad S_0
\end{align*}
$$
![[../../assets/Pasted image 20250212100258.png]]
- Überträge werden über Kette von 1bit Volladdierern vom LSB zum MSB weitergeben
- *Problem*: Langer kritischer Pfad (steigt linear mit Bitbreite)
## Halbaddierer
![[../../assets/Pasted image 20250212100407.png]]
Ein Halbaddierer besteht aus einem [[Logikgatter#XOR|XOR]] und einem [[Logikgatter#AND|AND]] Gatter.
## Volladdierer
![[../../assets/Pasted image 20250212100709.png]]
Ein Volladdierer besteht aus zwei Halbaddierern dessen Ausgang der Übertrag $C_0$ ist.

## Subtrahierer
- kann mit Addition und Negation realisiert werden: $A-B=A+(-B)$
- Negation im Zweierkomplement: Komplement und Inkrement
$\Rightarrow$ Addierer mit [[Logikgatter#NOT|NOT]]-Gatter an $B$-Eingängen und $C_0=1$
![[../../assets/Pasted image 20250212101133.png]]
## Vergleich: Kleiner als
- kann mit Subtraktion realisiert werden: $A<B\Leftrightarrow A-B<0$ 
![[../../assets/Pasted image 20250212101304.png]]
## Vergleich: Gleichheit
- Bitweise [[Logikgatter#XNOR|XNOR]] und [[Logikgatter#AND|AND]]-Baum
![[../../assets/Pasted image 20250212101503.png]]
Die 3 AND-Gatter in dieser Baum-Form agieren als großes AND-Gatter mit $\mathbb{B^4}\rightarrow\mathbb{B}$.

## Multiplizierer
- Produkt von $n$ und $m$ bit breiten Faktoren ist $n+m$ bit breit
- Teilprodukte aus einzelnen Ziffern des Multiplikators mit dem Multiplikanden
- verschobene Teilprodukte
![[../../assets/Pasted image 20250212101713.png]]
Wenn man Binärzahlen schriftlich multipliziert schreibt man wie hier, wenn die obere untere Zahl an der aktuellen Stelle eine $1$ hat die obere Zahl unter den Strich und wenn sie eine $0$ hat schreibt man einfach Nullen. Daher ist die unterste Zeile von den Teilprodukten auch $0000$. Danach werden die Teilprodukte aufaddiert. Falls es zu einem größeren Übertrag kommt, kann man die Teilprodukte auch untereinander aufaddieren.
## Kombinatorische $4\times4$ Multiplikation
![[../../assets/Pasted image 20250212102101.png]]
