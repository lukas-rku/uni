---
title: Boole'sche Gleichungen
description: Lernzettel - Digitaltechnik
draft: false
date: 2025-02-10
tags:
---
## Übersicht
- Beschreiben Ausgänge einer kombinatorischen Schaltung als (boole'sche) Funktion der Eingänge
	- Spezifikation des funktionalen Verhaltens (ohne zeitliche Information)
- Unter Verwendung elementarer boole'scher Operatoren (sortiert nach Operatorpräzedenz):
	- [[Logikgatter#NOT|NOT]]: $\overline{A}$
	- [[Logikgatter#AND|AND]]: $A\;B=A\cdot B$
	- [[Logikgatter#XOR|XOR]]: $A\oplus B$
	- [[Logikgatter#OR|OR]]: $A+B$
- Operatorpräzedenz Beispiel:
$$
((\overline{A})+((B\cdot C)\oplus D))
$$
## Grundlegende Definitionen
- Komplement: boole'sche Variable mit einem Balken (invertiert)
	- $\overline{A},\overline{B},\overline{C}$
- Literal: Variable oder ihr Komplement
	- $A,\overline A, B, \overline B, C, \overline C$
- Implikant: Produkt von Literalen
	- $ABC,A\overline C, BC, ...$
- Minterm: Produkt (UND, Konjunktion) über alle Eingangsvariablen
	- $ABC,AB\overline C,\overline ABC, ...$
	- $2^n$ mögliche Minterme
- Maxterm: Summe (ODER, Disjunktion) über alle Eingangsvariablen
	- $(A+\overline B + \overline C),(A+B+\overline C),(\overline A, \overline B, \overline C), ...$

## Minterm
- Produkt (Implikant), dass jede Eingangsvariable genau einmal enthält
- entspricht einer Zeile in Wahrheitswertetabelle
- jeder Minterm wird für genau eine Eingangskombination **wahr** (unabhängig von Ergebnisspalte)
![[../../assets/Screenshot 2025-02-10 160339_inverted.png]]
## Disjunktive Normaleform (DNF)
- Oder: Sum-of-products (SOP)
- Summe aller Minterme, für welche die Funktion *wahr* ist
	- jede boole'sche Funktion hat genau ein DNF (abgesehen von Kommutation)
- Im Beispiel: $Y = m_1 + m_2= \overline AB + A\overline B$
	- $A\oplus B$ nur kompakte Schreibweise für $\overline AB + A\overline B$
![[../../assets/Screenshot 2025-02-10 160857_inverted.png]]

## Maxterm
- Summe, welche jede Eingangsvariable genau einmal enthält
- entspricht einer Zeile in Wahrheitstablle
- jeder Maxterm wird für genau eine Eingangskombination falsch (unabhängig von Ergebnisspalte)
![[../../assets/Screenshot 2025-02-10 161039_inverted.png]]

## Konjunktive Normalform (KNF)
- oder Product-of-sums (POS)
- Produkt aller Maxterme, für welche die Funktion *falsch* ist
	- jede boole'sche Funktion hat genau eine KNF (abgesehen von Kommutation)
- Im Beispiel: $Y = M_0M_3=(A+B)(\overline A + \overline B)$
	- $A\oplus B$ nur kompakte Schreibweise für $(A+B)(\overline A + \overline B)$
![[../../assets/Screenshot 2025-02-10 161310_inverted.png]]
