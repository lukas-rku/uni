---
title: Korrektheit von Klassen
description: Lernzettel - funktionale und objektorientierte Programmierung
draft: false
date: 2025-02-05
tags:
---
## Darstellungsinvariante (`representation invariant`) von Klassen und Interfaces
Die Darstellungsinvariante legt fest, wie Objekte einer Klasse für den Nutzer erscheinen sollen. Sie wird durch die `public` definierten Attribute und Methoden bestimmt, die die sichtbare Schnittstelle der Klasse bilden.
## Implementationsinvariante (`implementation invariant`) von Klassen
Die Implementationsinvariante ist das Gegenstück zur Darstellungsinvariante, betrifft aber die nicht-`public` Teile einer Klasse. Sie beschreibt interne Eigenschaften der Implementierung und sollte für Nutzer der Klasse nicht sichtbar sein. Oft wird sie in Form von Kommentaren im Quellcode festgehalten.
## Beispiel anhand eigener Matrixklasse
**Darstellungsinvariante**: Ein Objekt von Klasse `DMatrix` repräsentiert zu jedem Zeitpunkt seiner Lebenszeit eine Matrix von `double`; Zeilen- und Spaltenzahl sind konstant und größer `0`; die Indizes sind ab `0` aufsteigend.

**Implementationsinvariante**: Attribut `matrix` vom Typ `double[][]` hat als Länge die Zeilenzahl, und seine Komponenten haben als Länge die Spaltenzahl; `matrix[i][j]` ist der Eintrag in Zeile `i` und Spalte `j`.
## Beispiel anhand von `FopBot`
**Darstellungsinvariante**: Ein Objekt von Klasse `Robot` repräsentiert zu jedem Zeitpunkt seiner Lebenszeit einen Roboter mit vier jederzeit veränderbaren Attributen: Zeile, Spalte, Richtung und Anzahl Münzen, sowie einem konstanten Attribut: der FopBot-World, zu der der Roboter gehört. ...

**Implementationsinvariante**: abhängig von der tatsächlichen Implementation der Klasse Robot.
## Beispiel anhand von [[Eigene LinkedList-Klasse|MyLinkedList]]
**Darstellungsinvariante**: Ein Objekt von `List` repräsentiert zu jedem Zeitpunkt seiner Lebenszeit eine geordnete Sequenz (die auch leer sein kann) seines generischen Elementtyps; die Positionen sind ab `0` aufsteigend; Suchen, Einfügen und Entfernen von Elementen kann zum Wurf einer `RuntimeException` führen; ... 

**Implementationsinvariante** von MyLinkedList:
![[Pasted image 20250131114410.png]]
## Ableitung von Klassen und Implementation von Interfaces
Wenn eine Klasse von einer anderen abgeleitet wird oder ein Interface implementiert, muss die Darstellungsinvariante der Basisklasse in der neuen Klasse weiterhin gelten. Das bedeutet, dass alle Bedingungen und Regeln, die für die Darstellung der Basisklasse definiert wurden, auch von der abgeleiteten oder implementierenden Klasse eingehalten werden müssen. Gleichzeitig muss die Implementationsinvariante übernommen werden, soweit sie sich auf `protected`-Attribute der Basisklasse bezieht. Dabei gilt, dass bestehende Invarianten erweitert oder verfeinert werden dürfen, aber nichts zurückgenommen werden darf.

Ein zentrales Prinzip in diesem Zusammenhang ist das **Liskov Substitution Principle (LSP)**. Wenn eine Methode der Basisklasse in der abgeleiteten Klasse überschrieben wird, muss sichergestellt sein, dass der Effekt dieser Methode auf die Darstellungsinvariante identisch bleibt. Das bedeutet, dass jede logische Aussage über das Verhalten der Basisklasse auch auf die abgeleitete Klasse zutreffen muss. Dies stellt sicher, dass eine Instanz der abgeleiteten Klasse überall dort eingesetzt werden kann, wo eine Instanz der Basisklasse erwartet wird, ohne dass sich das Verhalten unerwartet ändert.

Ein weiterer wichtiger Aspekt ist der Umgang mit Attributen. `Protected`-Attribute können in der abgeleiteten Klasse gelesen und überschrieben werden, müssen aber weiterhin die internen Regeln der Basisklasse befolgen, die in der Implementationsinvariante festgelegt sind. Private Attribute hingegen bleiben vollständig unter der Kontrolle der Basisklasse und müssen nicht übernommen werden.

Daher sollte die Entscheidung, ein Attribut als `protected` statt `private` zu definieren, gut überlegt sein. Änderungen an `protected`-Attributen erfordern potenziell Anpassungen in allen abgeleiteten Klassen, was zu einem erhöhten Wartungsaufwand führen kann.

Zusammenfassend bedeutet dies, dass sowohl die Darstellungsinvariante als auch – soweit es `protected`-Attribute betrifft – die Implementationsinvariante in jeder Hinsicht eingehalten werden müssen. Eine abgeleitete Klasse darf die bestehende Invarianz nicht aufweichen, sondern höchstens erweitern oder präzisieren.