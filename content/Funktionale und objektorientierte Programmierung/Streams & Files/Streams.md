---
title: Streams
description: Lernzettel - funktionale und objektorientierte Programmierung
draft: false
date: 2025-02-01
tags:
---
## Streams als generische Schnittstelle
Das Interface %%Link Interface%% `Stream` ist generisch und befindet sich in dem Package %%link package%% `java.util.stream`. `Streams` bilden eine einheitliche Schnittstelle für [[Eigene LinkedList-Klasse|Listen]], Arrays%%Link arrays%%, Dateien sowie unendliche Sequenzen von Werten des Typparameters.
## Ein Stream generiert aus Listen
```java
List<Number> list = new LinkedList<Number>();
for(int i = 0; i < 100; i++) {
	list.add(new Integer(3 + 4 * i));
}

Stream<Number> stream1 = list.stream();
Stream<Number> stream2 = stream1.filter(myPred);
Stream<Number> stream3 = stream2.map(myFct);
Optional<Number> opt = stream3.max(new MyNumberComparator());
```
Die Methode `stream` der generischen Klasse `List` liefert eine `Stream` vom selben generischen Typ der `List` zurück. Der `Stream` besteht auch aus den selben Elementen und der selben Reihenfolge der `List`. Bis hierin ist ein `Stream` also erstmal eine andere Zugriffsweise auf die Elemente der `List`.

Das Interface `Stream` hat unter anderem die Methode `filter`. Sie liefert einen `Stream` vom selben generischen Typ und benutzt das Predicate%%link Predicate%% `myPred` um dieses zu filtern. Das heißt, dass `stream2` die Elemente von `stream1` enthält, die das `Predicate` bestehen, bei denen `myPred` also `true` zurück gibt.

Die Methode `map` ist nun auch selber generisch, sie hat also neben dem Typparameter der Klasse `Stream` noch einen weiteren Typparameter. Die Rückgabe ist ein `Stream` des zweiten Typparameters. Das heißt, dass sie Potenziell unterschiediche Typen haben könnten. In diesem Beispiel ist dies aber nicht der Fall, da sowohl `stream2` und `stream2` vom Typ `Number` sind. So sind auch beide Typparameter von `myFct` %%link Function%% instanziiert mit `Number`. Die Methode `map` ist vom verhalten her völlig analog zu [[filter, map und fold auf Collection#`map`|map]].

Die Methode `max` liefert keinen `Stream` mehr, sondern nur noch ein Element des `Streams` die die Methode aufgerufen hat. Der formale Parameter von Methode `max` ist Comparator%%link Comparator%% des generischen Typ des `Streams`. Der Parameter entscheidet, welches Element von `Stream` zurückgeliefert wird, nämlich das, was bei der implementierten Vergleichsfunktion allen anderen Elementen des `Streams` nachfolgend ist. `max` liefert nicht das Element selbst, sondern der Verweis auf ein [[Optional||Optional]]-Objekt, für den Fall, dass Stream, und somit auch `Optional` leer ist.

Methoden der Klasse `Stream`, die wie `filter` und `map` wieder einen `Stream` zurückliefern, nennt man `intermediate operations`, also so etwas wie Zwischenoperationen.

Die Methode `max` ist ein Beispiel für eine `terminal operation`, also eine Terminalmethode, die am Ende der Kette von Zwischenoperationen sinnvoll ist.

```java
Optional<Number> opt = list.stream().filter(myPred)
									.map(myFct)
									.max(new MyNumberComparator());
```
Mehrere `intermediate operations` gefolgt von einer `terminal operation` können in einer einzigen Anweisung zusammengefasst werden. Wie auch sonst müssen die Rückgaben nicht unbedingt in Variablen zwischengespeichert werden, sondern können direkt vom nächsten Schritt weiterverwendet werden.
## Streams mit Arrays
```java
Number []a = new Number[100];
for(int i = 0; i < 100; i++) {
	a[i] = 3 + 4 * i;
}

Optional<Number> opt = Arrays.stream(a)
							 .filter(myPred)
							 .map(myFct)
							 .max(new MyNumberComparator());
```
Die Klasse `Arrays`%%link Arrays%% im Package `java.lang` bietet nützliche Methoden für die Arbeit mit Arrays. Die generische Methode `stream` nimmt ein Array als Parameter und gibt einen `Stream` zurück, der mit dem Komponententyp des Arrays instanziiert ist. Dieser `Stream` enthält die Array-Elemente in aufsteigender Reihenfolge der Indizes.

```java
Stream<Number> stream1 = Stream.of(new Integer(1), new Integer(2));
```
Mit der Methode `of` kann man auch ohne Umwege über eine `Liste` oder ein `Array` ein `Stream` definieren. Klassenmethoden bleiben bei Generizität außen vor, daher wird beim Aufruf kein generischer Typparameter benötigt.

```java
Optional <Number> opt = Stream.of(...)
							  .filter(myPred)
							  .map(myFct)
							  .max(new MyNumberComparator());
```
Und hier nochmal als Kurzschreibweise.
## Streams und Iteratoren
```java
Iterator iter = stream.iterator();

while(iter.hasNext()) {
	Number n = iter.next();
	doSomethingWith(n);
}
```
So wie [[Collection|Collections]] bieten Streams auch mithilfe eines [[Iterator|Iterators]] die Möglichkeit des elementweisen Durchlaufen. Lediglich die Generierung unterscheidet sich, je nachdem, worauf der `Iterator` laufen soll.
## Arrays aus Streams
```java
List<String> list = stream.collect(Collectors.toList());
Number[] a = stream.toArray(Number[]::new);
```
Die Klasse `Collectors` ist eine Sammlung von Klassenmethoden, die verschiedene Methoden  zur Weiterverarbeitung von Streams bereitstellt. Die Methode `collect` der Klasse `Stream` hat als Parameter exakt das, was die Methode `toList` von `Collectors` zurückliefert, nämlich das generische Interface `Collector`. (*Achtung; `Collectors` $\not=$`Collector`*). Sowohl auf `Collector` und `Collectors` wird hier nicht näher eingegangen.

Die generische Methode `toArray` von `Stream` besitzt einen Parameter vom Typ `IntFunction`, was ein generisches `Functional Interface` aus `java.util.function` ist. So wie hier bekommt sie ein `int` und liefert ein `Array` vom generischen Typ, hier also `Number`, zurück. Wie das `Array` konkret erzeugt wird, lässt sich durch den Parameter der Methode `toArray` steuern. %%Kapitel 04c, Link Lambda%%

```java
if(Arrays.equals(a, Arrays.stream(a).toArray(Number[]::new))) //true
```
Eine wichtige Erkenntnis ist, dass die beiden Ausdrücke zur Erzeugung einer `List` beziehungsweise eines `Arrays` aus einem `Stream` die exakte Umkehrung zu der Erzeugung eines `Streams` aus einem `Array` oder einer `List`. Bemerkenswert ist, dass hier die Nutzung von `equals` wichtig ist da 
```java
a == Arrays.stream(a).toArray(Number[]::new)
```
nur dann `true` ist, wenn beide Referenzen auf das gleich Objekt zeigen. Das ist allerdings höchst unwahrscheinlich.