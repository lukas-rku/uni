---
title: Deklaratives Programmieren
description: Lernzettel - funktionale und objektorientierte Programmierung
draft: false
date: 2025-02-08
tags:
---
## Grundlegender Gedanke
Man schreibt nicht Befehle hin, die ausgeführt werden sollen, sondern nur die "Formel" für das Ergebnis. Das, im Gegensatz zum imparativen Programmierstil in `Java`, `C` und `C++` u.ä., nennt man den *deklarativen* Programmierstil.
Konsequenzen:
- Kein zeitlicher Ablauf
- Keine Objektidentität (Man muss keine sich Vorstellung entwickeln, wie das im Computerspeicher aussieht.)

Kein zeitlicher Ablauf heißt, dass der Zeitpunkt des Aufrufs einer Funktion mit den selben Parameterwerten keine Rolle spielt. Jeder Aufruf einer Funktion kann äquivalent durch den Wert, den die Funktion für die Parameterwerte berechnet, ersetzt werden. Eine Funktion hat keine anderen Effekte außer ihr Rückgabewert. Beispielsweise eine `void`-Funktion, die nichts zurückliefert, ist im funktionalen Paradigma ziemlich unsinnig. Der Fachbegriff dafür lautet *referentielle Transparenz*.

```java
int n = 10;
System.out.println(n);
n = 11;
System.out.println(n);
```
In Java hingegen gibt es Variablen, also Bezeichner, die an einen Wert gebunden sind, aber dieser Wert kann sich im Ablauf des Programm ändern. Derselbe Ausdruck kann zweimal völlig unterschiedliche Ergebnisse haben. In Racket gibt es allerdings nur Konstanten, und wann immer wir irgendwo eine Konstante einsetzen, kann man sich sicher sein, dass sie immer denselben Wert hat.