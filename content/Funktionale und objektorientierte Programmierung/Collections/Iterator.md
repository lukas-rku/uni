# Iterator
## Anwendungsbeispiel von `Iterator`
```java
Iterator<Number> it1 = c1.iterator();
Iterator<Number> it2 = c2.iterator();
Iterator<Number> it3 = c3.iterator();

while(it1.hasNext()) {
	System.out.print(it1.next().doubleValue());
}
```
Zu jeder Klasse, die das Interface [[Collection|Collection]] implementiert, gibt es eine eigene `Iterator`-Klasse, die das generische Interface `Iterator` implementiert. [[Collection#Anwendungsbeispiel von `Collection` packages|Schon früher]] hatten wir `c1` vom Typ `ArrayList`, `c2` vom Typ `HashSet` und `c3` vom Typ `Vector` beispielhaft eingerichtet. 

Das Interface `Collection` erbt die Methode `iterator` von `Iterable`, die ein `Iterator`-Objekt zurückgibt. Jede Klasse, die `Iterable` implementiert, liefert ihre eigene `Iterator`-Klasse, aber durch das Interface `Iterator` können alle Iteratoren einheitlich genutzt werden. Die Unterschiede stecken im dynamischen Typ.

Die `while`-Schleife verwendet beispielhaft den ersten `Iterator` `it1`. Die Methode `next` gibt ein bisher noch nicht zurückgegebenes Element zurück. Die Reihenfolge davon ist generell unbestimmt, allerdings besteht bei Klassen, die das Interface `List` implementieren die Pflicht, dass diese nach Index durchlaufen werden.

Die Methode `hasNext` gibt zurück ob *dieser* `Iterator` noch `next` Elemente hat. Zu betonen ist, dass `hasNext` nur zurückgibt ob der aufrufende `Iterator` noch Elemente hat. Das heißt, dass man mehrere Iteratoren nacheinender oder gleichzeitig auf der selben `Collection` haben kann.

Während man mit einem `Iterator` durch eine `Collection` läuft, darf diese eigentlich nicht geändert werden. Da dies allerdings oft der Sinn von `Iterator` ist, wurde eine default-Methode namens `remove` erstellt, die das letzte von `next` zurückgelieferte Element aus der `Collection` entfernt. Allerdings darf `remove` nur einmal nach `next` aufgerufen werden; vor dem nächsten Aufruf muss ein neues `next` kommen. ^e08a09