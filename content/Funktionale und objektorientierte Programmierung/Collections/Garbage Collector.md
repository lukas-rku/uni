## Den Garbage Collector austricksen
Es besteht bei einer [[Eigene LinkedList-Klasse|LinkedList]] auch die Gefahr, dass der Speicherplatz durch einen Programmierfehler doch durch immer neue Objekte vollständig aufgebraucht wird bis das Programm dann irgendwann abbricht.
```java
X head = new X();
while(true) {
	X tmp = new X();
	tmp.next = head;
	head = tmp;
}
```
Dafür reicht schon dieses illustrative Beispiel. Durch die unendliche `while`-Schleife werden immer neue Elemente der Liste hinzugefügt. Allerdings darf keines davon vom Garbage Collector freigegeben werden, da alle Elemente noch vom Programm erreichbar bleiben müssen. Es ist nur eine Frage der Zeit, bis der gesamte zur Verfügung stehende Speicherplatz aufgebraucht ist.