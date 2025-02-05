---
title: Was heißt eigentlich "Korrektheit von Software"?
description: Lernzettel - funktionale und objektorientierte Programmierung
draft: false
date: 2025-02-05
tags:
---
## Kein Programmabbruch durch Fehler
In **Racket** führt ein Typfehler nicht zum Abbruch des Programmlaufs, sondern `DrRacket` setzt die Ausführung fort. In **Java** hingegen wird der Programmablauf unterbrochen, wenn eine nicht gefangene `Exception` auftritt. Dabei muss jede `Exception`%%Link Exception%%, die nicht von `RuntimeException` oder einer ihrer Unterklassen abstammt, entweder gefangen oder weitergereicht werden. Ein Programmabbruch in Java tritt auf, wenn eine `RuntimeException` oder eine davon abgeleitete `Exception` auf dem `Call-Stack` nicht abgefangen wird.
## Termination
Beim Thema **Termination** gibt es zwei Fälle:
- **Endliche Programme** – Eine Softwarekomponente soll eine bestimmte Aktion ausführen und danach enden. Korrekte Termination bedeutet hier, dass sie nach endlich vielen Schritten tatsächlich stoppt und nicht in eine Endlosschleife gerät.
- **Unendlich laufende Programme** – Komponenten, die dauerhaft Prozesse steuern (zum Beispiel eine Ampel), sollen nur dann terminieren, wenn ein autorisierter Befehl dies anordnet, etwa durch ein Event in einer GUI.
## Korrekte Ausgaben und Effekte
Die Ausgaben einer Software müssen korrekt sein, ebenso wie ihre Effekte auf die Außenwelt, etwa bei der Steuerung von Geräten.