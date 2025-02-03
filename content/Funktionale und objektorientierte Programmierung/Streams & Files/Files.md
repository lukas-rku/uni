 ---
title: Die Klasse Files
description: Lernzettel - funktionale und objektorientierte Programmierung
draft: false
date: 2025-02-03
tags:
---
## Methoden aus `Files`
```java
Path path = Paths.get(...);
if(Files.exists(path)) {
	if(Files.isReadeble(path)) {
		if(Files.isWriterble(path)) {
			if(Files.isRegularFile(path)) {
				if(Files.isDirectory(path)) {
					long size = Files.size(path);
				}
			}
		}
	}
}
```
Die Klasse `Files` ist eine Sammlung von Klassenmethoden. Das Grundprinzip hat man schon bei [[Streams und Dateien|Paths]] und `Arrays` gesehen.

Hier eine Auswahl an Methoden, mit denen man Attribute von Dateien abfragen kann.
- `exists` gibt zurück, ob in dem `path` überhaupt etwas existiert. Dies kann eine Datei, ein Verzeichnis oder auch irgendein anderes Objekt sein, dass das Dateisystem verwaltet.
- Die Methoden `isReadeble` und `isWriteble` sind recht selbstverständlich und fragen das Zugriffsrecht des Programms von eine Datei oder eines Pfades ab. Die Rückgabe ist allerdings Benutzerabhängig, da sich die Rechte ändern können.
- `isRegularFile` und `isDirectoy` überprüft, ob das Objekt des `path` eine Datei ist, da bspw. Verzeichnisse auch Objekte an dem `path` sein können. Es gibt aber auch Methoden, die genau zurückgeben von welchen Typ ein Objekt an dem `path` ist.
- Auch die Größe lässt sich einfach mit `size` abfragen. Allerdings können heutzutage so groß sein, dass sie nicht mehr in `int` gespeichert werden können.

## Manipulation von Objekten des Dateisystems
```java
Path path1 = Paths.get(...);
Path path2 = Paths.get(...);
Path path3 = Paths.get(...);
Path path4 = Paths.get(...);

Files.createFile(path1);
Files.copy(path1, path2);
Files.move(path3, path4); //move oder rename
Files.delete(path1);
Files.deleteIfExists(path2);
```
*Wichtig:* Ein Pfadname in einem `Path`-Objekt bedeute *nicht*, dass im Dateisystem tatsächlich ein Objekt mit diesem Pfad existiert. 
- Mit Methode `createFile` richten wir zu einem Pfadname ein Objekt ein, das dann diesen Pfadnamen hat. Also erstellt man auch die Verzeichnisstruktur drummherum.
- Mit `copy` kopiert man den Inhalt von einem `path` in einen anderen. Genauso das Umbennen eines Objektes, meist spricht man allerdings vom Bewegen `move` des Objekts im Dateisystem.
- Mit `delete` Entfernt man das Objekt des `path`. Wenn das Objekt gar nicht existiert, wird eine `NoSuchFileException` geworfen. Um das zu umgehen, kann man `deleteIfExists` benutzen, falls man sich nicht sicher sein kann, ob das zu entfernende Objekt existiert.