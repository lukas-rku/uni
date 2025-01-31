# Eingeschränkte Typparameter
## Die generische Beispielklasse A mit Einschränkung auf `X`, `Y` und `Z`
```java
abstract public class X{
	public void m1() {...}
	abstract public int m2();
}

public class Y extends X {...}
public class Z extends Y {...}

public class A <T extends X> {
	public void m (T t) {
		t.m1();
		System.out.print(t.m2);
	}
}
```
Der [[Typparameter|Typparameter]] `T` wird durch das Schlüsselwort `extends` eingeschränkt, sodass `T` entweder gleich `X` oder direkt oder indirekt von `X` abgeleitet sein darf, also auch `Y` und `Z`. Der Typparameter `T` ist also durch die Klasse `X` *beschränkt*. Anstelle eine Klasse kann auch ein Interface einen Typparameter beschränken.

Gezeigt hier ist nur die Einschränkung mit einem einzigen Typparameter. Allerdings funktioniert das Konzept auch bei Klassen mit mehreren Typparameter und auch bei [[Generische Methoden|generischen Methoden]].

Ein wichtiger Aspekt eingeschränkter Typparameter in Java ist die Garantie, dass Methoden in Typparameter-Klassen definiert sind und sicher verwendet werden können. Der entscheidende Punkt dabei ist, dass die Klasse `X` die Methoden `m1` und `m2` definiert, wobei `m2` zwar abstrakt bleibt, aber durch abgeleitete Klassen wie `Y` oder `Z` implementiert wird. Dadurch kann ein Objekt einer abgeleiteten Klasse als Parameter verwendet werden, und es ist sichergestellt, dass die erforderlichen Methoden existieren.

Die Einschränkung des Typparameters durch das Schlüsselwort `extends` stellt sicher, dass `T` entweder `X` oder von `X` abgeleitet ist. Dies erlaubt es, in generischen Klassen oder Methoden nur Typen zu verwenden, bei denen klar ist, dass die benötigten Methoden korrekt definiert und aufrufbar sind.

## Anwendungsbeispiel von `A`
```java
A<X> a1 = new A<X>();
A<Y> a2 = new A<Y>();
A<Z> a3 = new A<Z>();

A<String> a4 = new A<String>();// nicht möglich
```
Da `String` nicht `X` ist oder von `X` abgeleitet wurde, darf sie nicht der Typparameter der Klasse `A` sein. Das ist auch gut so, denn wenn eine Klasse wie hier Klasse `String` nicht von `X` abgeleitet ist, dann sind die Methoden `m1` und `m2` in der Regel auch nicht vorhanden, und wenn sie doch vorhanden sind, dann nicht unbedingt mit derselben Parameterliste und demselben Rückgabetyp wie in Klasse `X`, also nicht kompatibel zur Verwendung in Klasse `A`.

## Mehrfache Einschränkung von Typparametern
```java
public class X{...}
public interface Int1{...}
public interface Int2{...}
public interface Int3{...}

public class A<T extends X & Int1 & Int2 & Int3> {...}
```
*Erinnerung:* Eine Klasse kann nur von *einer* anderen Klasse abgleitet sein, aber beliebig viele Interfaces implementieren.

Auf diesem Weg lässt sich erzwingen, dass `T` sowohl auf `X` als auch auf die drei Interfaces eingeschränkt ist. Das heißt, erlaubt als Instanziierungen von `T` sind nur Klassen, die jedes der drei Interfaces direkt oder indirekt implementieren und entweder gleich `X` oder von `X` direkt oder indirekt abgeleitet sind.

Wenn eine Klasse in der Liste vor kommt, muss sie als erstes geschrieben werden.