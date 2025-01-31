## Inhalt von `Collection`
```java
//in java.util:
Collection
Collections
List
Iterator
//---
Vector
LinkedList
ArrayList
TreeSet
HashSet
```
Alle `Collection` Klassen implementieren das Interface `Collection`. Nicht zu verwechseln mit der Klasse `Collections`, welche nützliche Basisalgorithmen, wie bspw. für das Sortieren, enthalten. `List` erweitert `Collection` und implementiert spezielle `Collection` - Klassen für erweiterte Funktionalitäten. Der `Iterator` um über die Inhalte von `Collection` zu iterieren. 
Weiter unten sind Beispiele für Klassen, die `Collection` implementieren.
## Anwendungsbeispiel von `Collection` packages
```java
Collection<Number> c1 = new ArrayList<Number>();
Collection<Number> c2 = new HashSet<Number>();
Colleciton<Number> c3 = new Vector<Number>();

for(int i = 0; i < 100; i++) {
	c1.add(new Integer(i));
	c2.add(new Double(i));
	c3.add(new Float(i));
}
```
Da die Algorithmen und Datenstrukturen in Java gut eingekapselt sind, kann man diese nutzen ohne verstehen zu müssen was hinter der "Fassade" passiert.