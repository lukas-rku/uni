---
title: Die Klasse Optional
description: Lernzettel - funktionale und objektorientierte Programmierung
draft: false
date: 2025-02-01
tags:
---
## Illustratives Beispiel
```java
Optional<Number> opt1 = Optional.ofNullable(new Integer(123));
Optional<Number> opt2 = Optional.ofNullable(null);

Number n1 = opt1.get(); // n == 123
Number n2 = opt2.get(); // NoSuchElementException
Number n3 = opt1.orElseGet(() -> 0);
Number n4 = opt2.orElseGet(() -> 0);
```
Zunächst werden zwei Variablen vom Typ Optional eingerichtet, bei denen der [[Generische Klassen|generische]] Typparameter mit Number instanziiert ist. Die Klasse `ofNullable` erzeugt ein Objekt von Klasse `Optional` und liefert einen Verweiß darauf zurück.

Wenn die Methode `get` versucht, ein statt einem Objekt `null` zurückzugeben, wird eine `NoSuchElementException` geworfen. Diese kann man allerdings umgehen, indem man stattdessen `orElseGet` verwendet. Hier wird im Falle, dass `opt2` auf `null` zeigt, mit Hilfe eines Lambda-Ausdrucks %%Link für Lambda Ausdruck bitte%%die Zahl `0` zurückgegeben, statt das eine `NoSuchElementException` geworfen wird.
## Weitere nützliche Methoden
```java
opt1.ifPresent(x -> {System.out.print(X);});
opt2.ifPresent(x -> {System.out.print(x);});

Optional<Number> opt3 = opt1.map(x -> x * x);
Optional<Number> opt4 = opt2.map(x -> x * x);

Optional<Number> opt5a = opt3.filter(x -> x % 2 == 1);
Optional<Number> opt5b = opt3.filter(x -> x % 2 == 0);
Optional<Number> opt6 = opt4.filter(x -> x % 2 == 1);
```
Die Methode `ifPresent` ermöglicht eine sichere Verarbeitung einer Referenz, falls sie nicht `null` ist. Sie nimmt einen `Consumer<T>` als Parameter, der angibt, was mit dem enthaltenen Objekt gemacht werden soll. Dadurch lässt sich das häufige Muster „Prüfung auf `null` und dann Verarbeitung“ vermeiden. Der Parameter kann auch ein Lambda-Ausdruck sein.

Analog zu `ifPresent` kann eine Funktion nur ausgeführt werden, wenn das `Optional` nicht leer ist. In diesem Beispiel enthält `opt1` ein `Number`-Objekt, dessen Quadrat in `opt3` gespeichert wird. Da `opt2` leer ist, bleibt auch `opt4` leer.

Die Methode `filter` gibt ein `Optional` desselben generischen Typs zurück. Sie nimmt ein `Predicate<T>`%%link Predicate%% als Parameter, das aus dem Package `java.util.function` stammt. Wenn das enthaltene Objekt die Bedingung erfüllt, bleibt es erhalten, sonst wird ein leeres `Optional` zurückgegeben.