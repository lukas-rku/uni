---
title: Wildcards
description:
draft: false
date: 2025-01-29
tags:
---
## Beispiel ohne Wildcard
```java
public class X<T> {
	public T attribute;
}

public class A{
	public double m (X<Number> n) {
		return n.attribute.doubleValue();
	}
}
```
Eine Klasse `A` hat die Methode `m` mit einem Parameter `n` der instanziierten Klasse `X`.

## Beispiel mit Wildcard
```java
public class X<T> {
	public T attribute;
}

public class A{
	public double m (X<? extends Number> n) {
		return n.attribute.doubleValue();
	}
}
```
Hier wird festegelegt, dass der Typ des Parameters `n` entweder `Number` oder eine von `Number` direkt oder indirekt abgeleitete Klasse ist. `X` ist eine [[Generische Klassen|generische Klasse]].

## Unterscheidung
```java
public <T extends Number> double m (X <T>n, T m) {...}
```
Die ganze Methode `m` ist [[Generische Methoden|generisch]]: `Number` und alle Subtypen von `Number`.

```java
public double m (X<? extends Number> n, Integer m) {...}
```
Die Methode `m` ist nicht generisch: Der einzelne Parameter ist generisch, also `Number` und alle Subtypen von `Number`.

Die erste Methode ermöglicht eine größere Flexibilität, da der Typ von `m` dynamisch auf denselben Typ wie der von `n` angepasst wird. In der zweiten Methode ist der Typ `m` explizit auf `Integer` festgelegt, während `n` mit einer beliebigen Unterklasse von `Number` arbeiten kann.

## `?` als alleinige Wildcard
```java
public class X {
	public T attribute;
}

public class A { 
	public String m (X<?> obj) {
		return obj.attribute.toString();
	}
}
```
Implizit zu verstehen ist `<?>` als `<? extends Object>`, also `java.lang.Object`. Damit sind alle Klassen und Interface - Typen eingeschlossen.  Es darf aber nur Funktionalität verwendet werden, die schon in `Object` definiert sind.

## `super` mit Wildcards
```java
public class X <T> {
	public void m1(T t) {...}
}

public class A {
	public void m2(X<? super Double> x) {
		x.m1(new Double(3.14));
	}
}
```
Mit `extends` kann der Typparameter nach oben in der Vererbungshierarchie beschränkt werden (Upper Bounded Wildcard). Es gibt auch die Beschränkung nach unten mit `super` (Lower Bounded Wildcard).

In diesem Beispiel kann Methode `m2` von Klasse `A` mit verschiedenen Instanziierungen von `X` als aktualen Parametern aufgerufen werden, nämlich mit der angegebenen Klasse, hier `Double`, der direkten Basisklasse von `Double`, allen indirekten Basisklassen von `Double` sowie allen von `Double` implementierten Interfaces.

Da `Double` direkt von `Number` und `Number` direkt von `Object` abgeleitet ist, kommen im Falle von `Double` nur diese drei Klassen in Frage, sowie ggf. Interfaces, die von `Double` implementiert wurden.

## Wann sollte man was benutzen?
```java
<? extends T
```
Verwendung, wenn man Daten aus einer generischen Struktur *lesen* möchte.
"Akzeptiere einen Typ, der `T` ist oder von `T` erbt."

```java
<? super T
```
Verwendung, wenn man Daten in eine generische Struktur *schreiben* möchte.
"Akzeptiere einen Typ, der `T` ist oder ein Elternteil (Supertyp) von `T`."

| Ziel                               | Verwende          | Beispiel                                                                                                                    |
| ---------------------------------- | ----------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Nur **lesen** aus einer Struktur   | `? extends T`     | Eine Methode, die Elemente aus einer `List<? extends Number>` verarbeitet, z. B. `List<Double>` oder `List<Integer>`.       |
| Nur **schreiben** in eine Struktur | `? super T`       | Eine Methode, die Elemente vom Typ `T` (oder Unterklassen von `T`) in eine `List<? super T>` einfügt, z. B. `List<Object>`. |
| **Lesen und schreiben**            | **Kein Wildcard** | Verwende den genauen Typ wie `List<T>`, wenn du volle Kontrolle über Lesen und Schreiben benötigst.                         |
