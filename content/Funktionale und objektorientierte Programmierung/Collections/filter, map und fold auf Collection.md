# Die Standardoperationen `filter`, `map` und `fold` auf Collection
## `filter`
```java
//Objectmethode von Collection<T>:
boolean removelf(Predicate<? super T> pred)
```
Für `filter` hat das Interface [[Collection|Collection]] tatsächlich schon eine Methode namens `removelf`. Alle Methoden die das `Predicate` werden aus der Collection entfernt. Allerdings entspricht dies nicht genau der `filter`-Operation in Racket, da dort eine neue Liste zurückgegeben und die Alte nicht verändert wird. Hingegen gibt `removelf` nur zurück, ob ein Element entfernt wurde oder nicht.

```java
public static<T> void filter(Collection<T> coll, Predicate<T> pred) {
	Iterator it = coll.iterator();
	while(it.hasNext()) {
		if(!pred.test(it.next)) {
			it.remove();
		}
	}
}
```
Hier eine mögliche Implementation der `filter`-Methode mittels [[Iterator|Iterator]], die wie `removelf` die Eingabeliste selbst verändert, allerdings ohne zurückgeben ob diese geändert wurde. Wichtig ist allerdings die implementation von `it.remove()` wie [[Iterator#^e08a09|hier]] schon beschrieben.

```java
public static <T> Collection<T> filter(Collection<T> coll, Predicate<T> pred) {
	Collection<T> result = new LinkedList<T>();
	for(T t:coll) {
		if(pred.text(t)){
			result.add(t);
		}
	}
	return result;
}
```
Hier eine Variation von `filter`, wo, wie bei Racket, die Eingabeliste nicht geändert, sondern stattdessen eine neue erstellt wird. Daher wird eine `Collection` vom selben generischen Typ zurückgeliefert. Erwähnenswert ist hier die [[Kurzform for-Schleife bei Collections|Kurzform]] der `for`-Schleife
## `map`
```java
public static <X,Y> Collection<Y> map(Collection<X> coll, Function<X,Y> fct) {
	LinkedList<Y> result = new LinkedList<Y>;
	for(X x:coll) {
		result.add(fct.apply(x));
	}
	return result;
}
```
%%Link zu 04c%%
Bei `map` wird wird ein Element aus der `Collection` `coll` mit einer Funktion `fct` berechnet und wieder zurückgegeben. %%Das ist so schlecht erklärt 😭%%
## `fold`
```java
public static <X,Y> Y fold(Y init, BiFunction<X,Y,Y>fct, Collection<X> coll) {
	Y tmp = init;
	for(X x:coll) {
		tmp = fct.apply(x,tmp);
	}
	return tmp
}
```
%%Link zu 04c%%
Die Methode `fold` reduziert eine Sammlung `coll` von Elementen des Typs `X` auf einen einzelnen Wert des Typs `Y`, indem sie mit einem Startwert `init` beginnt und eine bi-funktionale Reduktionsfunktion `fct` iterativ auf jedes Element der Sammlung anwendet. %%Danke chatgpt 🙏%%