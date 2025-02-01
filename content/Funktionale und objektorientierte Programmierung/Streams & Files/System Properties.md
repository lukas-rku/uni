---
title: System Properties
description: Lernzettel - funktionale und objektorientierte Programmierung
draft: false
date: 2025-02-01
tags:
---
## System Properties abfragen
Die Klasse `java.lang.System` kann Informationen aus Umgebung, in der das Java-Programm abläuft zurückgeben. Diese können bei jedem Ablauf unterschiedlich sein und sich sogar während der Ausführung ändern. Daher kann man diese Attribute nicht sinnvoll im Programm konstant festlegen, sondern muss sie jedes mal neu abfragen. die Klasse `System` ermöglicht und vereinfacht das. Eine bekannte Methode von `System` ist `System.out.print`.
## Einige Methoden von `System`
```java
String homeDirectory    = System.getProperty("user.home");
String workingDirectory = System.getProperty("user.dir");
String accountName      = System.getProperty("user.name");
String fileSeperetor    = System.getProperty("file.seperator");
String lineSeperator    = System.getProperty("line.seperator");
```
Die Methode `getProperty` von Klasse `System` erhält als Parameter einen `String` und liefert einen `String` zurück. Nur bei bestimmten `Strings`, wie zum Beispiel den hier gezeigten, wird etwas sinnvolles und ansonsten wird `null` zurückgeliefert.

Hat das Programm nicht die Berechtigung auf eines dieser Attribute zuzugreifen, wird eine `SecurityException` geworfen. Da `SecurityException` von `RuntimeException` abgeleitet ist, kann man das ignorieren. Eigentlich müssen `Exceptions` immer gefangen oder weitergereicht werden, mit eben der Ausnahme von `RuntimeExceptions`. Falls diese oder eine von ihr abgeleitete Klasse unerwartet dennoch eine `Exception` wirft, so wird das Programm abgebrochen.

- `user.home` gibt das Heimatverzeichnis des Nutzers, der das Programm ausführt, zurück.
- `user.dir` gibt das momentane Arbeitsverzeichnis (`working directory`) des Prozesses zurück.
- `user.name` gibt den Namen des Nutzers zurück
- `file.seperator` gibt das Zeichen, dass von dem Betriebssystem als Trennung bei Verzeichnispfaden genutzt wird zurück. Bei Microsoft ist dies ein `\` und bei `UNIX`- Systemen ein `/`.
- `line.seperator` gibt das Zeichen, welches von dem Betriebssystem als Zeilentrennung in Textdateien genutzt wird zurück.