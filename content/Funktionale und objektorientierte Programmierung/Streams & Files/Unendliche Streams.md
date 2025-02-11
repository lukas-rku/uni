---
title: Unendliche Streams selbstgemacht
description: Lernzettel - funktionale und objektorientierte Programmierung
draft: false
date: 2025-02-02
tags:
---
## Erstellung von unendlichen Streams
```java
public class StreamOfSineValues implements DoubleStream {
	private double start;
	private double samplingDist;
	public StreamOfSineValue(double start, double samplingDist) {
		this.start = start;
		this.samplingDist = samplingDist;
	}
}
```
Für die Abtastung werden ein Startpunkt `start` und eine Distanz `dist` definiert, was im Endeffekt die Abtastrate ist.
```java
public class StreamOfSineValuesIterator implements PrimitiveIterator.ofDouble{
	private int n = 0;
	public boolean hasNext() {
		return true;
	}
	public double next() {
		return Math.sin(start + samplingDist * n++);
	}
}
```
An der [[../Collections/Iterator]]-Klasse lässt sich das Prinzip des unendlichen [[Streams]] sehr gut zeigen. Daher wird sich hier nicht die gesamte Klasse `StreamOfSineValues` angeschaut.

Die `Iterator`-Klasse zu [[IntStreams, LongStreams und DoubleStreams|DoubleStream]] heißt `ofDouble` und ist in einem `Interface` namens `PrimitiveIterator` im Package `java.util`.

Um bei jedem Aufruf von `next` die korrekt folgende Zahl zu erhalten wird mit `n` der aktuelle Fortschritt des `Iterators` festgehalten. Mithilfe von `n++` in dem Aufruf von `Math.sin` wird während dem Zurückgeben von `next` `n` erhöht.

In `hasNext` sieht man am deutlichsten den Unterschied zu endlichen `Streams`: Ohne nachzufragen wird immer `true` zurückgegeben, da es bei unendlichen `Streams` nie *nicht* ein nächstes Element geben kann.