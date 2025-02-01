---
title: Eigene `LinkedList`-Klasse
draft: false
date: 2025-01-31
---
## Beispielhafte Implementation von `LinkedList`
```java
public class ListItem <T> {
	public T key;
	public ListItem<T> next;
}

ListItem<T> head = new ListItem<T>();
head.next = new ListItem<T>();
```
Ein Objekt von der Klasse `ListItem` hat ein Attribut von Klasse `ListItem`. Das heißt, dass die Listenelemente miteinander verkettet sind.
![[Pasted image 20250131113743.png#d0]]
![[Pasted image 20250131114410.png#d0]]
Man kann nahezu unbegrenzt viele Listenelemente miteinander verketten. Genau das ist das Konzept einer `LinkedList`. 
## `LinkedList` erstellen
```java
public class MyLinkedList<T> implements List<T> {
	private ListItem<T> head;
	...
}
```
So würde man eine `LinkedList` erstellen. Diese muss auf den `head`, also auf das erste Listenelement zeigen. 

## Durchlaufen einer `LinkedList`
Für das Durchlaufen einer `LinkedList` benötigt man einen sogenannten `Pointer`, welcher auf das aktuelle Listenelement zeigt. Dies ist Vergleichbar mit dem `Index` eines `Arrays`. Dieser besitzt auch den Typ der Listenelemente, da er ja nacheinander auf diese verweisen soll.
```java
p = p.next;
```
Dabei sieht jeder Vorwärtsschritt gleich aus: Der Wert in dem Attribut `next` des ersten Listenelement ist die Adresse des zweiten Listenelements. Wenn der `Pointer p` nun auf den Wert `p.next` gesetzt wird, dann verweißt er auf das zweite Element. Dieser Schritt ist identisch bei jeder Position des `Pointers`. Das bedeutet auch zwangsweise, dass der `Pointer` auf `null` gesetzt wird, sobald er das letzte Element erreicht hat, da dieses ja mit seinem `next` auf `null` zeigt.
```java
public void processAll(Consumer<T> consumer) {
	for(ListItem<T> p = head; p != null; p = p.next) {
		consumer.accept(p.key);
	}
}
```
Die hier gezeigte `for`-Schleife demonstriert die Flexibilität dieser Schleifen. Statt eines Indexes wird ein `Pointer` als Laufvariable mit dem `head` festgelegt. An Stelle der Inkrementierung wird `p` auf `p.next` gesetzt, was das durchlaufen ermöglicht.

Das generische Functional Interface `Consumer` aus `java.util.function` bietet mit der Methode `accept` eine einheitliche Schnittstelle, für den Fall, dass man Werte von `T` prozessiert, ohne dass ein Rückgabewert herauskommt.
## Weitere Beispielmethoden
```java
public class ScreenNumberWriter implements Consumer<Number> {
	public void accept(Number n) {
		System.out.print(n.doubleValue());
	}
}
```
Eine beispielhafte Implementation der Methode `accept` von `Consumer`, die eine Zahl `n` in die Konsole ausgibt.
```java
public boolean contains(Object obj) {
	for(ListItem<T> p = head; p != null; p = p.next) {
		if(Object.equals(obj,p.key)) {
			return true;
		}
	}
	return false;
}
```
Hier eine Implementation von `processAll`, die im Prinzip auch schon für `List` und sogar schon für [[Collection|Collection]] definiert ist. In dieser Variation wird die Liste nicht unbedingt bis zum Ende durchlaufen. Sobald das gesuchte Element mithilfe von `Object.equals` gefunden wurde, liefert die Methode true zurück.

Erwähnenswert ist, dass unter anderem die Methode `equals` aus `Objects` in dem Package `java.util` enthalten ist. Diese behandelt Sonderfälle wie beispielsweise `obj == null` und/oder `p.key == null`.
## Hinzufügen von Elementen zu einer `LinkedList`
```java
public void add(int pos, T key) throws IndexOutOfBoundsException {
	if(pos < 0) {
		throws new IndexOutOfBoundsException("Wrong position: " + pos);
	}
	ListItem<T> tmp = new ListItem<T>();
	tmp.key = key;

	if(pos == 0) {
		if(head == null) {
			head = tmp;
		} else {
			tmp.next = head;
			head = tmp;
		}
		return;
	}

	for(ListItem<T> p = head; p != null; p = p.next) {
		pos--;
		if(pos == 0) {
			tmp.next = p.next;
			p.next = tmp;
			return;
		}
	}
	throw new IndexOutOfBoundsException("Wrong position: " + pos);
}
```
Als erstes wird geprüft, ob `pos` überhaupt eine zulässige Position ist. Daraufhin wird eine temporäre Liste erstellt, dessen `key` auf den angegebenen `key` gesetzt wird. 

Danach wird der Fall behandelt, dass `pos == 0` ist. Wenn die `LinkedList` leer ist, wird das `tmp` Element zum `head`. Wenn sie nicht leer ist, wird `head` um eins nach hinten verschoben, sodass `tmp` der neue `head` der `LinkedList` wird.

Falls `pos > 0` ist, wird die `LinkedList` durchlaufen, bis der Zeiger `p` an der richtigen Stelle ist. Da wir allerdings das Element `tmp` and die aktuelle Stelle des Zeigers und nicht eins danach setzen wollen, muss `p` um eins verringert werden. Danach wird der `head` des Listenelements, was ja eins vor der Stelle von `pos` ist, auf unser `tmp` gesetzt. Der `head` von `tmp` nimmt dann das darauffolgende Element an.

Falls `pos` außerhalb der `LinkedList` ist, wird ein Fehler geworfen.
## Entfernen von Elementen aus einer LinkedList
```java
public boolean remove(Object obj) {
	if(head == null) {
		return false;
	}
	
	if(Object.equals(obj,head.key)) {
		head = head.next;
		return true;
	}
	
	for(ListItem<T> p = head; p.next != null; p = p.next) {
		if(Objects.equals(obj,p.next.key)) {
			p.next = p.next.next;
			return true;
		}
	}
	
	return false;
}
```
Im Vergleich zu der Methode `add`, ist die Implementation von `remove` erstaunlich simpel. Zunächst versichert man, wie schon zuvor, dass die `LinkedList` nicht leer ist. 

Der Fall, dass das zu entfernende Objekt der `head` der Liste ist, wird daraufhin behandelt. Hier setzt man einfach den `head` der `LinkedList` auf das darauffolgenden Listenelement.

Andererseits wird die Liste durchlaufen, bis `obj` gefunden wurde. Um dies zu entfernen wird `next` des vorherigen Elements auf das nachfolgende gesetzt. Zu beachten ist allerdings, dass die `for`-Schleife leicht modifiziert ist. So wird in der Schleife nach `p.next != null` und nicht `p != null` gesucht. Das versichert, dass der Fall, dass `p.next` kein Listenelement mehr hat abgedeckt ist.

*Wichtig ist, dass andere Programmiersprachen wie bspw. C keinen sogenannten [[Garbage Collector|Garbage Collector]] hat. Das heißt, dass dort die zu entfernenden Elemente sorgfältiger behandelt werden müssen. So muss man bespielsweise manuell den Speicherplatz wieder freigeben, bevor er nicht mehr erreichbar ist.*
## Eine passende Iterator-Klasse zu `LinkedList`
```java
class MyLinkedListIterator<T> implements Iterator<T> {
	private ListItem<T> p;
	public MyLinkedListIterator(ListItem<T> head) {
		p = head;
	}

	public boolean hasNext() {
		return p != null;
	}
	
	public T next() {
		T key = p.key;
		p = p.next;
		return key;
	}
}
```
Hier die Implementation einer [[Iterator|Iterator-Klasse]] für eine `LinkedList`. Der `Pointer` `p` ist hier als Attribut an Stelle eines Laufzeiger in einer `for`-Schleife eingebaut. 

Im Konstruker des `Iterators` wird dieser dann auf den `head` der Liste gesetzt. Die Idee ist, dass p immer auf das nächste mit `hasNext` zurückliefernde Element verweist, also auf das erste in der Liste, dessen `key` bis dahin noch nicht durch das `hasNext` zurückgeliefert wurde.

Da `p` immer auf das erste noch nicht zurückgelieferte Listenelement verweisen soll, ist die Abfrage ob es ein solches Listenelement überhaupt noch gibt sehr einfach.

Die Methode `next` muss p um eine Position weiter schalten. Allerdings wird zuvor der `key` von `p` gespeichert, damit er danach zurückgegeben werden kann. Dieser ist nämlich nach Fortschaltung unerreichbar

```java
public Iterator<T> iterator() {
	return new MyLinkedListIterator(head);
}
```
Die Methode `iterator` von `MyLinkedListIterator` ist nun einfach benutzbar.