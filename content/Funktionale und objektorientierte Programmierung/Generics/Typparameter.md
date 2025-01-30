# Typparameter
## Beispiele für mögliche und nicht mögliche Typparameter

```java
X x = new X();

//Klassen
Integer i = new Integer(345);
Double d = new Double(3.14);
Pair<Integer, Double> pair1 = x.makePair (a, b);

//Arrays
int[] ia = new int[3];
String[] sa = new String[5];
Pair<int[], String[]> pair2 = x.makePair(c,d);

//Parametrisierte Klassen
Pair<Integer, Double> pair3 = new Pair (i, d);
Pair<Pair<Double, Integer>, String[]> pair4 = new Pair<Pair<Double, Integer>, String[]>(pair3, sa);

//Primitive Datentypen sind nicht möglich
Pair<int, double> // NICHT MÖGLICH!!
Pair<Integer, Double> //Wrapper Klassen als work-around

//Abgeleitete Klassen können die Basisklasse nicht ersetzen
public class X{...}
public class Y extends X{...}
public class Z extends Y{...}
public class A {
	public void m(Pair<X,Y> pair) {...}
}

A a = new A();
a.m(new Pair<X,Y>(x,y));
a.m(new Pair<X,Z>(x,z)); //NICHT MÖGLICH!! Es wird versucht ein die von Y abgeleitete Klasse Z anstelle von Y zu verwenden. Das ist kann man nicht tun.
```
[[Generische Klassen#^ad4d86|Pair]] & [[Generische Methoden#^35eb40|makePair]]
## Kurzschreibweise
```java
Pair<String,Integer> pair;
pair = new Pair<> ("Hello", 123);
```
[[Generische Klassen#^ad4d86|Pair]]
Der Compiler kann selbst herausfinden, welche Typparameter `pair` besitzt. In solchen Fällen, wo dies eindeutig ist, kann man den Inhalt der spitzen Klammern weglassen.