# Methoden von `Collection`
```java
add
addAll
size
isEmpty
contains
containsAll
clear
remove
```
Hier eine Auswahl von Methoden im Interface [[Collection|Collection]].
## `add`
```java
boolean add(T elemt) throws 
	UnsupportedOperationException,
	NullPointerException,
	ClassCastException
	IllegalArgumentException,
	IllegalStateException
```
Zurückgeliefert wird `true`, wenn das Element erfolgreich eingefügt wurde. Manche Implementationen von `Collection` erlauben es nicht, dass zu einem Element, das schon in einer `Collection` vorhanden ist, noch einmal dasselbe oder ein wertgleiches Element eingefügt wird.
Eine `UnsupportedOperationException` wird dann geworfen, wenn die Methode `add` von dem Interface nicht unterstützt wird. Außerdem unterstützen manche kein `null` als Listenelement (`NullPointerException`). %%Der Rest der Exceptions ist für FOP irrelevant%%
## `addAll`
`addAll` erhält nicht ein einziges Element sondern eine andere `Collection` und fügt diese zu der `Collection` hinzu, die diese Methode aufruft. Sie besitzt die selben `throw` - Klauseln wie `add`.
## `size`
Die Methode `size` gibt einfach nur die Anzahl Elemente, die in der `Collection` gespeichert sind, als `int` zurück.
## `isEmpty`
Die recht selbsterklärende Methode `isEmpty` gibt `true` zurück, wenn die aufrufende `Collection` keine Elemente besitzt, also wenn `size` 0 ist.
## `contains` & `containsAll`
`contains` und `containsAll` überprüft ob das Element bzw. die `Collection` welches mitgeliefert wird in der aufrufenden `Collection` enthalten ist.
```java
Collection<String> coll = new ...;
String str1 = new String("Hallo");
String str2 = new String("Hallo");
coll.add(str1);
if(coll.contins(str2)) //true

Collection<string> coll1 = new...;
coll.add(null);
if(coll.contains(null)) //true
```
## `clear` & `remove`
`clear` entfernt alle und `remove` entfernt das mitgelieferte Element aus der `Collection`. Falls `remove` von einer `Collection` aufgerufen wird, die mehrfach das selbe Element enthält, entscheidet die Implementation der Methode das verhalten.
