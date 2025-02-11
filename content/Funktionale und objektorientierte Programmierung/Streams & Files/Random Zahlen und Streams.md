---
title: Random Zahlen und Streams
description: Lernzettel - funktionale und objektorientierte Programmierung
draft: false
date: 2025-02-02
tags:
---
## Füllen eines `Arrays` mit random Zahlen
```java
static double[] randomDoubleArray(int length) {
	double[] return Array = new double[length];
	Random random = new Random();
	for(int i = 0; i < returnArray.length; i++) {
		returnArray[i] = random.nextDouble();
	}
	return returnArray;
}
```
Zur Erzeugung von Zufallszahlen steht Klasse `Random` aus Package `java.util` bereit. `nextDouble` gibt bei jedem Aufruf eine neue Zufallszahl zurück. Im Fall von `nextDouble` und `nextFloat` ist das ein Wert aus `[0...1)` und im Fall von `nextInt` und `nextLong` eine beliebige Zahl aus dem zugehörigen Wertebereich.
## Füllen von `Streams` mit random Zahlen
```java
IntStream stream1 = new Random().ints();
LongStream stream2 = new Random().longs();
DoubleStream stream3 = new Random().doubles();
```
`Random` hat schon je eine Methode für jede der drei [[IntStreams, LongStreams und DoubleStreams|spezialisierten]] `Stream`-Klassen. Alle drei Methoden liefern jeweils einen `Stream` zurück. Hier zeigt sich ein Vorteil von `Streams`: `Streams` können im Gegensatz zu Listen, Arrays und Dateien unendlich lang sein. Ein `Stream` von Zufallszahlen endet nie, und ein [[../Collections/Iterator]] darüber liefert stets `true` bei `hasNext`, egal wie viele Werte bereits entnommen wurden.