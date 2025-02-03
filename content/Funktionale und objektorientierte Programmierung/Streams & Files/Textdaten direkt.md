---
title: Textaden direkt (ohne Streams)
description: Lernzettel - funktionale und objektorientierte Programmierung
draft: false
date: 2025-02-03
tags:
---
## Textweises Lesen von Dateien
```java
public static int m(Reader reader, char[] buffer) throws IOException {
	return reader.read(buffer);
}

try(FileReader reader1 = new FileReader(fileName));
BufferedReader reader2 = new BufferedReader(reader1)) {
	char[] a = new char[256];
	int numberOfReadChars = X.m(reader2, a);
}
```
Hier sieht man auf dem ersten Blick, dass vieles sehr ähnlich zum [[Bytedaten direkt|byteweisen]] Einlesen aussieht. Analog zur Basisklasse `InputStream` für das Einlesen von Bytedaten gibt es die Basisklasse `Reader` für das Einlesen von Textdaten.

Klasse `Reader` bietet mehrere Methoden namens `read`, darunter diese, die ein `char`-Array als Parameter hat. Diese Methoden liest so viele Zeichen ein, bis entweder das `Array` voll, oder das Ende der Datenquelle erreicht ist. Rückgabe ist die Anzahl der tatsächlich eingelesenen Zeichen.

Völlig analog zu `InputStream` und `FileInputStream` gibt es auch eine von `Reader` abgeleitete Klasse `FileReader`, die die Datei, deren Name im Parameter übergeben wird, zum Lesen öffnet. Ebenso analog kann man noch eine Pufferung darauf setzen.

## `readLine`
```java
public static String m(BufferedReader reader) throws IOException {
	return reader.readLine();
}

try(FileReader reader1 = new FileReader(fileName);
BufferedReader reader2 = new BufferedReader(reader1)) {
	X.m(reader2);
}
```
Hier eine Vereinfachung: Die Klasse `BufferedReader` hat die Methode `readLine`, die ein Stringobjekt einrichtet und eine ganze Zeile einliest. Genauer gesagt, wird alles eingelesen von dem letzten eingelesenen Zeichen bis zum nächsten Zeilenende.

## `InputStreamReader` als Brücke zwischen byteweises und zeichenweises Lesen
```java
InputStream in = ...;
Reader reader = new InputStreamReader(in);
```
Byteweises Einlesen von Daten lässt sich auch in zeichenweises Einlesen umwandeln, was in der Regel nur dann Sinn macht, wenn ein `InputStream` eine Datenquelle öffnet, die Textdaten anstatt Bytedaten enthält. Die Brücke zwischen byteweise und zeichenweise ist Klasse `InputStreamReader`, die von `Reader` abgeleitet ist und den `InputStream` als Parameter im Konstruktor bekommt.

## Schreiben von Texten in Dateien
```java
public static void m(Writer writer) throws IOException {
	writer.write("H");
	writer.write("ello World!");
}

try(FileWriter writer1 = new FileWriter(fileName)
BufferedWriter writer2 = new BufferedWriter(writer1)) {
	X.m(writer2);
}
```
Hier ist auch vieles wieder ähnlich zum Lesen. Allerdings hat die Klasse `Writer` mehrere Methoden namens `write`, zudem auch eine, die ein einzelnes Zeichen schreibt und eine, die einen ganzen `String` schreibt.

## `OutputStreamWriter` als Brücke zwischen byteweises und zeichenweises Schreiben
```java
OutputStream out = ...;
Writer writer = new OutputStreamWriter(out);
```
Wie beim `InputStreamReader` gibt es den `OutputStreamWriter` als Brücke zwischen `OutputStream` und `Writer`.