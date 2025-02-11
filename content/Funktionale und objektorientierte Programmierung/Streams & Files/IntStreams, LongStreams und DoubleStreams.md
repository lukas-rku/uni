---
title: IntStreams, LongStreams und DoubleStreams
description: Lernzettel - funktionale und objektorientierte Programmierung
draft: false
date: 2025-02-02
tags:
---
## `IntStream` anstelle von `Stream<Integer>`
```java
IntStream stream1 = IntStream.of(1,2,3);
IntStream stream2 = stream1.filter(x -> x % 2 == 1);
IntStream stream3 = stream2.map(x -> x * x);
int n = stream3.max().getAsInt();
```
Die Arbeit mit einer dieser drei speziellen, nichtgenerischen [[Streams|Stream]]-Klassen ist weitestgehend identisch zur Arbeit mit der generischen `Stream`-Klasse. Wie [[Streams#^9cb8e4|Stream]] besitzt auch `IntStream` die Methode `of` zum Einrichten eines `Streams` aus einer Sequenz von Zahlen.

Der Vorteil der drei spezialisierten `Streams` ist, dass Operationen auf den Datentypen umstandslos hingeschrieben werden können. `OptionalInt` ist die primitive Variante von [[Optional]]`<Integer>` für `IntStream` (analog gibt es `OptionalLong` für `LongStream` und `OptionalDouble` für `DoubleStream`).`stream3.max()` gibt ein `OptionalInt` zurück, da der maximale Wert eines Streams nicht garantiert vorhanden ist (zum Beispiel, wenn der Stream leer ist). Um den Wert aus `OptionalInt` zu extrahieren, wird `getAsInt()` verwendet.

```java
int n = IntStream.of(1,2,3).filter(x -> x % 2 == 1).map(x -> x * x).max().getAsInt()
```
Wie bei generischen `Streams` kann man die Operationen auch wieder zusammen fassen.
## Unterschiede zwischen `IntStream` und `Stream<Integer>`
|               | `Stream<Integer>`                                                  | `IntStream`                                                       |
| ------------- | ------------------------------------------------------------------ | ----------------------------------------------------------------- |
| Typ           | Generischer `Stream<Integer>`                                      | Spezialisierter `IntStream`                                       |
| Speicherung   | Enthält `Integer`-Objekte                                          | Enthält primitive `int`-Werte (keine Objekte)                     |
| Effizienz     | Weniger effizient                                                  | Speicher- und Performance-optimiert                               |
| Methoden      | Allgemeine Stream-Methoden (`map()`, `filter()`, `collect()`, ...) | Spezialisierte Methoden (`mapToInt()`, `sum()`, `average()`, ...) |
| Rückgabetypen | Gibt `Optional<Integer>`, `List<Integer>`, etc. zurück             | Gibt `OptionalInt`, `int[]`, `int` zurück                         |
