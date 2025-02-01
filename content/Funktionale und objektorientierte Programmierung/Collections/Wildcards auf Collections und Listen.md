---
title: Wildcards auf Collections und Listen
description: Lernzettel - funktionale und objektorientierte Programmierung
draft: false
date: 2025-01-30
tags:
---
## Wildcards mit `extends` auf `Collection` und `List`
```java
public boolean containsNull(Collection<? extends Number> coll) {
	return coll.contains(null);
}

public double getVaule(List<? extends Number> list, int index) {
	return list.get(index).doubleValue();
}
```
In beiden Fällen wird jeweils nur eine Methode aufgerufen, die lesend auf [[Collection|Collection]] bzw. `List` zugreift. Insbesondere im zweiten Fall sieht man, dass das [[Wildcards#Beispiel mit Wildcard|extends]] im Typparameter der `List` kein Problem bei In-Parametern darstellt. Alle Klassen, die vom Typparameter Number direkt oder indirekt abgeleitet sind, haben die Methode `doubleValue`.
## Wildcards mit `extends Object` auf `Collection` und `List`
```java
public Object getVaule(List<?> list, int index) {
	return list.get(index);
}
```
Dasselbe geht auch für `<?>`, was synonym für `<? extends Object>` steht. Allerdings muss sich dieses Beispiel auf die Verwendungsmöglichkeiten beschränken, die schon für `Object` definiert sind.
## Wildcards mit `super` auf `Collection` und `List`
```java
public void addPi(Collection<? super Double> coll) {
	coll.add(Math.PI);
}
public void addSqrt2(List<? super Double> list, int index) {
	list.add(index, Math.sqrt(2));
}
```
In diesem Beispiel wird nun bei `List` und `Collection` ein Out-Parameter genutzt, d.h. anstatt von `extends` muss [[Wildcards#`super` mit Wildcards|super]] genutzt werden. In beiden Methoden wird nur schreibend auf die `Collection` bzw. `List` zugegriffen. Einen lesenden Zugriff gibt es hier nicht.