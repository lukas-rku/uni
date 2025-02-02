---
title: Streams & Dateien
description: Lernzettel - funktionale und objektorientierte Programmierung
draft: false
date: 2025-02-01
tags:
---
## Beispielanwendung
```java
String homeDir = System.getProperty("user.home");
String fileSep = System.getProperty("file.separator");
Path path = Paths.get(homeDir, "fop", "streams.txt");

try (Stream<String> stream = Files.lines(path)) {
    String fileContentAsString = stream.reduce("", String::concat);
} catch (IOException exc) {
    System.out.print("Could not open file " + fileSep + homeDir + fileSep + "fop" + fileSep + "streams.txt" + "!");
}
```
Die Klassen `Path` und `Paths` sind in dem Package `java.nio.file` zu finden und haben wie andere Klassen aus dem Package mit Dateien und Dateistrukturen zu tun. 

Ein `Path` verwaltet den Pfadnamen zu einer Datei, eines Verzeichnisses oder eines anderen Objektes, das über diesen Pfadnamen erreichbar ist. Zu einem Objekt der Klasse `Path` muss es kein Objekt im Dateisystem geben.

Die Klasse `Paths` ist eigentlich nur dazu da um, wie hier, ein Objekt der Klasse `Path` zu erzeugen. Diese besitzt die überladene%%Link überladene Klassen%% Klasse `get`. Die hier verwendete Variente der Methode hat eine variable Parameterzahl %%Link 03c variable Parameterzahl%%vom Typ `String`, dass heißt sie eine oder mehr `Strings` annehmen.
```java
Paths.get(homeDir, "fop"); // "{homeDir}\fop\"
Paths.get(homeDir, "fop", "streams.txt"); // "{homeDir}\fop\streams.txt"
```
Die Methode `get` erzeugt, wie hier im Beispiel gezeigt, einen `Path` ohne, dass sich der Nutzer um die Umgebung in der das Programm ausgeführt wird sorgen machen muss. Siehe [[System Properties#^ecb983|file.seperator]].

Die Klasse `Files` aus `java.nio.file` besitzt die Methode `lines`, welche die Datei eines Pfades öffnet. Zurückgeliefert wird ein [[Streams|Stream]] von Strings, dessen Inhalt die Zeilen der Datei sind. Als Erkennung für ein Zeilenende wird [[System Properties#^8a7a36|line.seperator]] genutzt. Bei binären Dateien macht ein solches öffnen ejer leomem Sinn. Wenn beim öffnen Datei durch `lines` etwas schief geht wird eine `IOException` geworfen, zum Beispiel wenn die Datei gar nicht vorhanden ist oder das Programm kein Leserecht hat. Da `IOException` nicht von `RuntimeException` abgeleitet ist, muss sie gefangen werden. Dadurch muss man, wenn man mit `java.nio.file` arbeiten will auch fast immer `java.io` importieren.

Die Methode `reduce` von `Stream` erstellt aus einem `Stream` wieder ein einzelnes Ergebnis. So werden hier alle Zeilensprünge aus `streams.txt` entfernt.