---
title: Generische Klassen
description:
draft: false
date: 2025-01-29
tags:
---
## Beispiel einer generischen Klasse
### Die Klasse `Pair`
```java
public class Pair<T1, T2> {
	private T1 attribute1;
	private T2 attribute2;

	public Pair(T1 a1, T2 a2) {
		attribute1 = a1;
		attribute2 = a2;
	}

	public T1 get Attribute1() {
		return attribute1;
	}
	
	public void setAttribute1(T1 a1){
		attribute1 = a1;
	}
}
```

^ad4d86

`T1` und `T2` sind Platzhalter für Referenztypen. Das heißt, die Klasse `Pair` ist mit `T1` und `T2` parametrisiert, bzw. sind `T1` und `T2` Typparameter von der Klasse `Pair`.
### Einrichtung der Klasse `Pair`
```java
Integer i = new Integer(123);
Double d = new Double(3.14);
Pair<Integer,Double> pair = new Pair<Integer,Double>(i,d);
```
Die Variable `pair` hat also als statischen Typ sozusagen den Typ "Paar von Integer und Double", d.h. `Pair` ist hier mit `Double` und `Integer` instanziiert.
## Methoden von generischen Klassen
```java
Integer i1 = pair.getAttribute1;
System.out.print(i1.intValue()); // 123
Integer i2 = new Integer(234);
pair.setAttribute1(i2);
```
Hier wird nun die Methode `getAttribute1()` von `pair` aufgerufen, welche, wie schon definiert, ein Integer sein muss. *Für die Methode `intValue()` siehe ~~Boxing/Unboxing~~.*

%%Hier war noch irgendein verweiß von Lambda Ausdrücken keine Ahnung.%%