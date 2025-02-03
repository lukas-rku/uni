---
title: Bytedaten direkt (ohne Streams)
description: Lernzettel - funktionale und objektorientierte Programmierung
draft: false
date: 2025-02-03
tags:
---
## Byteweises Lesen von Dateien
```java
public static void m(InputStream in) throws IOException {
	while(true) {
		int n = in.read();
		if(n == -1) {
			return;
		}
		processByte(n);
	}
}

try(FileInputStream in = new FileInputStream(fileName)) {
	X.m(in);
} catch (FileNotFoundException | IOException exc) ...
```
In [[Streams und Dateien]] haben wir schon gesehen, wie man [[Streams|Streams]] aus Dateien erzeugt. Hier sieht man Dateien *ohne* Bezug zur [[Streams|Streams]]. Die Klassen und Interfaces finden sich in Package `java.io`. Wie hier haben ein paar Klassen das Wort `Stream` im Namen, haben aber nichts mit der Klasse `Stream` zu tun.

In dem Code oben sieht man das byteweise Lesen aus Dateien. Das ist sinnvoll, wenn die Datei nicht einen Text sondern binäre Daten enthält. Allerdings werden die wenigsten jemals Programme schreiben, die Binärdaten tatsätchlich byteweise verarbeiten, da viele Bibliotheken solche Funktionalitäten zur verfügung stellen. Mit der Klasse `InputStream` wird man also eher selten arbeiten.

Woraus genau die Bearbeitung der Bytes besteht verhüllt die Methode `processByte`. Wichtig ist, dass `n` ein `int` ist und nicht ein `byte`. Das hat den Grund, dass der primitive Datentyp `byte` vorzeichenbehaftet mit Werten zwischen `-128` und `127` ist, die Methode `read` aber nur einen "normalen" Byte mit acht Bits zurück gibt. Außerdem muss es noch die Möglichkeit geben anzuzeigen, dass das Dateiende, hier mit `-1`, erreicht ist.

Wenn die Methode `read` nicht `-1` zurückgibt, dann ist gewährleistet, dass nur das unterste Byte von Datentyp `int` ungleich `0` ist. Die imaginäre Methode `processByte` verarbeitet nur dieses.

Die Klasse `InputStream` ist abstrakt, es sind also nur Objekte von abgeleiteten Klassen, wie `FileInputStream`, möglich. `FileInputStream` hat einen Konskruktor, in dem man den Dateinamen als `String` angibt.

*Wichtig:* Die Klasse `InputStream` hat schon einen Lesepointer implementiert. Bei jedem Aufruf von `read` wird dieser um ein Byte verschoben. Daher bleibt das eigene Implementieren des Lesefortschritts aus.

## Byteweises Schreiben
```java
public static void m(OutputStream out) throws IOException {
	for(int i = 0; i <= 2 * Byte.MAX_VALUE + 1; i++) {
		out.write(i);
	}
}

try(FileOutputStream out = new FileOutputStream(fileName)){
	X.m(out);
} catch(FileNotFoundException | IOException exc) ...
```
Das unterste Byte der `int`-Variable `i` durchläuft hier rein zur Illustration alle `256` Bitmuster, die ein Byte bestehend aus acht Bits annehmen kann.

Die Methode `write` von `OutputStream` hat `int` als formalen Parametertyp. Aber es wird nur das unterste Byte geschrieben, ale anderen Bits des `int`-Wertes werden ignoriert.

Das Schreiben der Datei ist recht analog zum lesen. Zu beachten ist, dass, wenn eine Datei schon existiert, ihr Inhalt überschrieben. Andererseits wird sie neu erstellt.
```java
FileOutputStream out = new FileOutputStream(fileName, true)
```
Hier wird im Fall, das die Datei schon existiert, kein Inhalt überschrieben, sondern an das Ende angehängt.

## Das Lesen und Schreiben buffer'n
```java
try(FileInputStream in = new FileInputStream(fileName)) {
	X.m(new BufferedInputStream(in));
} catch(FileNotFoundException | IOException exc) ...

try(FileOutputStream out = new FileOutputStream(fileName)) {
	X.m(new BufferedOutputStream(out));
} catch(FileNotFoundException | IOException exc) ...
```
Man kann die Methode `read` von `BufferedInputStream` genau so benutzen wir bei `InputStream`. Allerdings ist die Implementierung anders. Im Hintergrund bekommt `read` ein `Array` an Bits als Puffer das es nacheinander abarbeitet. Wenn das `Array` am Ende ist, bekommt es ein neues. Das hat den Vorteil, dass man nicht für jede `read`-Operation auf die Datei zugreifen muss.

Ähnlich dazu funktioniert auch `write` von `BufferedOutputStream`. Die Bytes werden zunächst in ein `Array` geschrieben und dann in einem Rutsch in die Datei eingefügt.

## `PrintStream`
```java
try(FileOutputStream out1 = new FileOutputStream(fileName);
BufferedOutputStream out 2 = new BufferedOutputStream(out1);
PrintStream out3 = new PrintStream(out2)) {
	out3.print("pi = ");
	out3.print(3.14);
	out3.println(`!`);
} catch(FileNotFoundException | IOException exc) ...
```
*Erinnerung:* %%Link Try Catch%%In `try`-Blöcken können auch mehrere, durch Semikolons getrennte, Ressourcen geöffnet werden. Die letzte darf allerdings nicht mit einem Semikolon abgeschlossen werden.

Zunächst benötigen wir wieder einen `FileOutputStream` und puffern diesen mit `BufferedOutputStream`. 

Neu ist allerdings `PrintStream`: Sie besitzt mehrere Methoden `print` für die byteweise Ausgabe von Werten verschiedener Datentypen auf den im Konstrukter übergebenen `OutputStream`. Klasse `PrintStream` dient sozusagen als Konvertierer von den verschiedenen primitiven Datentypen sowie `String` in eine byteweise Repräsentation. Das eigentliche Schreiben übernimmt dann der `OutputStream`. So ist `PrintStream` ein Aufsatz auf den `OutputStream`.

## Erinnerung an `System.out`, `System.err` und `System.in`
Das Klassenatribut `out` von `System` ist von Klasse `PrintStream`. Neben den `print`-Methoden hat `PrintStream` auch diverse Methoden wie `println` zum Schreiben von Zeilenumbrüchen.

Die Klasse `System` hat noch ein weiteres Klassenattribut namens `err` von `PrintStream`. Die Ausgaben erscheinen auch dort, wo die Ausgaben von `System.out` erscheinen. Allerdings ist es dennoch [[Bytedaten direkt#^5f6e8a|sinnvoll]] zwei `PrintStreams` hier zu haben.

Außerdem hat die Klasse `System` noch das Klassenattribut `in` von `InputStream`. Dieser `InputStream` liest zunächst einmal Daten von der Tastatur, solange wir nichts daran ändern.

```java
try(FileInputStream in = new FileInputStream(filename1);
FileOutputStream out = new FileOutputStream(filename2);
FileOutputStream err = new FileOutputStream(filename3)) {
	System.setIn(in);
	System.setOut(new PrintStream(out));
	System.setErr(new Printstream(err));
	makeSomethingWirthInOutAndErr();
}
```
Bei Einrichtung von Klasse `System` werden diese drei Klassenattribute auf Bildschirmausgabe beziehungsweise Tastatureingabe gesetzt.

`System` bietet die drei Klassenmethoden `setIn`, `setOut` und `setErr` für die drei Klassenattribute. Damit können die drei Klassenattribute auf andere `Streams` umgesetzt werden. Im Beispiel wird `System.in` auf eine Datei umgesetzt, liest also aus dieser Datei statt von der Tastatur. Analog werden `System.out` und `System.err` auf Dateien umgesetzt, in die sie dann schreiben, statt auf den Bildschirm.

Hier lässt sich auch zeigen, warum es sinnvol ist, zwei `PrintStream` als Klassenattribut von `System` zu haben. So schreibt man auf `out` die normalen Ausgaben eines Programms und auf `err` die Fehlerausgaben, die man bspw. in `catch`-Blöcken definiert hat. ^5f6e8a

So sieht man, dass die Ausgaben auf `out` und `err` getrennt werden können, wie zum Beispiel in getrennte Dateien umgeleitet. In der Praxis ist es häufig so, dass `out` nicht umgeleitet wird, also weiterhin auf den Bildschirm schreibt, und `err` in eine Log-Datei schreibt.

## Weitere Hilfreiche `Input-/OutputStream` Klassen
```java
java.util.zip.ZipInputStream
java.util.jar.JarInputStream
javax.sound.sampled.AudioInputStream
java.io.PipedInputStream
java.io.PipedOutputStream
```
Hier ein paar ausgwählte Klassen die von `InputStream` oder `OutputStream` abgeleitet sind und die Vielseitigkeit des Konzepts demonstrieren.

So gibt es `InputStream`-Klassen zum einlesen von komprimierten Dateien und für `jar`-Dateien. Eine `jar`-Datei enthält kompilierte Java-Dateien, mit `zip` komprimiert. Sie befinden sich nicht in `java.io` sondern in `java.util` wo auch weitere nützliche Funktionalitäten zusammengefasst sind.

`javax.sound.sampled.AudioInputStream` von `InputStream` bietet spezielle Zugriffsmethoden für Audio-Dateien an. Sie befindet sich ebenfalls nicht in `java.io`.

Grob gesprochen kann man ein `PipedInputStream`-Objekt und ein `PipedOutputStream`-Objekt so miteinander koppeln, dass alles, was in das `PipedOutputStream` geschrieben wurde, aus dem `PipedInputStream` gelesen werden kann. %%Link Threads 09%%