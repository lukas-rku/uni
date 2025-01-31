## `Keys` und `Values`
```java
public class X {
	private int n;
	public X(int n) {
		this.n = n;
	}
	public int getN(){
		return n;
	}
}
///---
Map<String, X> map = new HashMap<String,X> ();
for(int i = 0; i < 100; i++) {
	String key = "Nr." + i;
	X value = new X(2 * i + 3);
	map.put(key.value);
}
```
Ein Interface [[Collection|Maps]] besitzt zwei Typparameter. Der erste ist der `Key` und der zweite ist die Information - die `Value` - die zu dem `Key` gespeichert wird. Eine `Map` realisiert also Abbildung von den `Keys` in die `Values`.

Als Beispiel werden nun 100 `Keys`-`Value` Paare in die `HashMap` eingefügt. Wie in der Mathematik bei einer Abbildung wird jedem `Key` genau eine `Value` zugeordnet. Allerdings dürfen mehrere `Keys` die gleiche `Value` haben, was mathematisch Gesprochen heißt, dass die Abbildung *injektiv* sein muss.
## Beispielanwendung
```java
String str1 = new String("Nr. 23");
X x1 = map.get(str1);
System.out.print(x1.getN()); //49
String str2 = new String("Hallo");
X x2 = map.get(str2);
if(x2 == null) {
	System.out.print("Wie erwartet");
}
```
Mit `get(Key)` wird bei einer `HashMap` die `Value` des `Keys` zurückgegeben. Wenn ein nicht definierter `Key` mit `get` aufgerufen wird, dann wird `null` zurück gegeben.