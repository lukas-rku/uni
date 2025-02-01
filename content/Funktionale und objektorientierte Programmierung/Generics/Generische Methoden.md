---
title: Generische Methoden
description:
draft: false
date: 2025-01-29
tags:
---

## Die Beispielmethode `makePair`

```java
public class X { //Die Klasse ist nicht generisch!
	public <T1,T2> Pair<T1,T2> makePair(T1 t1, T2 t2) {
		return new Pair<T1,T2> (t1,t2)
	}
}
```

^35eb40

[[Generische Klassen#^ad4d86|Pair]]
Der Typparameter `<T1, T2>` wird – wie bei [[Generische Klassen|generischen Klassen]] – parametrisiert, nur diesmal auf Methodenebene. Die Methode `makePair` ist generisch, obwohl die umgebende Klasse es nicht ist. Dies teilt der Methode mit, dass es sich um eine generische Methode handelt und die Typparameter `T1` und `T2` eingeführt werden müssen. 

Da der Rückgabetyp der Methode `Pair` sein soll, müssen wir diesen ebenfalls mit denselben Typparametern `<T1, T2>` spezifizieren. Dies entspricht der Angabe eines konkreten Typs, wie z. B. `int` bei einer Methode `public int getInt();`. Hier stellt `<T1, T2>` sicher, dass der `Pair`-Typ mit den Typen der Eingabeparameter (`t1`, `t2`) übereinstimmt.

Der Sinn der Methode `makePair` ist, die beiden Parameter der Methode zu einem Paar zusammenzufassen.
## Anwendung von `makePair`
```java
X x = new X();
Pair<A,B> pair1 = x.makePair(new A(), new B());
Pair<C,D> pair2 = x.makePair(new C(), new D());
```
Die vier Klassen `A`,`B`,`C` und `D` sind beliebig. 