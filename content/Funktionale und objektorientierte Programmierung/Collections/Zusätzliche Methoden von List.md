---
title: Zusätzliche Methoden von `List`
description: In Java kann eine Liste von Objekten mithilfe eines benutzerdefinierten `Comparator` sortiert werden. Im Beispiel wird eine Liste von `Student`-Objekten anhand ihrer Immatrikulationsnummer geordnet, wobei der `EnrollmentNumberComparator` zur Sortierung verwendet wird.
draft: false
date: 2025-01-31
tags:
  - fop
  - collections
---
## Die zusätzlichen Methoden
```java
indexOf
set
add
get
```
Das Interface `List` erweitert das Interface [[Collection|Collection]], ebenfalls mit dem Elementtyp als Typparameter. In einer `List` existiert zum gegenteil zu einer `Collection` (welche in der Mathematik mit einer Menge vergleichbar ist) eine Reihenfolge. Die `List` enthält wie ein Array auch ein Index welche die Position eines Zeigers beschreibt.
## `indexOf`
`indexOf` gibt selbstverständlicherweise den Index einer `List` zurück und wird mit einem Parameter vom Typ `Object` aufgerufen. Wenn die `List` das `Object` nicht enthält gibt sie für den Index `-1` zurück.
## `set`
```java
T set(int index, T element) throws
	IndexOutOfBoundsException,
	UnsupportedOperationException,
	NullPointerException,
	ClassCastException,
	IllegalArgumentException
```
Die Methode `set` hat zwei Parameter: Den `index` an welchem das `element` eingefügt werden soll. Der Wert, der aktuell an dem `index` der `List` ist, wird durch `element` ersetzt. Zurückgegeben wird das Element, dass überschrieben wurde. Falls der `index` nicht im Indexbereich der `List` ist, wird eine `IndexOutOfBoundsException` geworfen. Die restlichen Exception sind identisch zu denen bei [[Methoden von Collection#`add`|add]].
## `add`
Die Methode `add` ist eine weitere Methode zu dem schon existierenden [[Methoden von Collection#`add`|add]] und ist fast identisch zu `set`, da sie zu dem eingefügten `element` noch ein `index` hat. Im Gegensatz zu `set` überschreibt sie das Element an der Stelle des `index` *nicht*, sondern verschiebt alle existierenden Elemente um einen Index nach hinten, sodass das neue `element` den angegebenen `index` hat.
```java
(a,b,c,d,e)
add(2,x)
(a,b,x,c,d,e)
```
## `get`
`get` gibt das Element an der Stelle des mitgelieferten Index der `list` zurück. Falls dieser Parameterwert außerhalb der Liste ist, wird eine `IndexOutOfBoundsException` geworfen.
