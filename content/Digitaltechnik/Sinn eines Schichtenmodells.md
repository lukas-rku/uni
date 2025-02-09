---
title: Sinn eines Schichtenmodells
description: Lernzettel - Digitaltechnik
draft: false
date: 2025-02-09
tags:
---
## Wesentliche Eigenschaften
- Untere Schicht erbringt Dienstleistungen für die nächst höhere Schicht
- Obere Schicht nutzt nur die Dienste der nächst niedrigeren Schicht
- Eindeutige Schnittstellen zwischen den Schichten
	- Eine obere Schicht weiß nicht, wie eine untere Schicht eine Funktion implementiert hat
- Vorteile einer sauberen Schichtenstruktur
	- Austauschbarkeit einzelner Schichten, ohne benachbarte Schichten oder das gesamte System ändern zu müssen
	- Benutzer braucht nur die von ihr zu bearbeitende Schicht zu kennen
	- Darunterliegende Schichten bilden fest definierte Funktionalität
	- Für manche Aufgaben ist genauere Kenntnis der unteren Schichten dennoch notwendig (z.B. Programmierung von Gerätetreibern)
- Nachteil ist eine ggf. geringere Leistungsfähigkeit des Systems

## Disziplin
- Disziplin ist die wissentliche Beschränkung der Realisierungsmöglichkeiten
	- Erlaubt produktivere Arbeit auf höhere Entwurfsebenen
- Beispiel: Digitale Entwurfsdisziplin
	- Arbeite mit diskreten statt mit stetigen Spannungspegeln
	- Digitalschaltungen sind einfacher zu entwerfen als analoge
		- Erlaubt den Entwurf komplexerer Schaltungen
	- Digitale Systeme  ersetzen zunehmend analoge
		- Digitalkamera, digitales Fernsehen, moderne Handys, CD, DVD

## Digitale Abstraktion
- Die meisten physikalischen Größen haben stetige Werte
	- Elektrische Spannung
	- Frequenz einer Schwingung
	- Position einer Masse
- Berücksichtigen unendlich viele Werte der Größe
- Digitale Abstraktion: Berücksichtigt nur endlich viele Werte
	- Untermenge aus einem stetigen Wertebereich

## Wesentliche Techniken
- Hierarchie (Hierarch**y**)
	- Aufteilen eines Systems in Module und Untermodule
- Modularität (Modularit**y**)
	- wohldefinierte Schnittstellen und Funktionen
- Regularität (Regularit**y**)
	- bevorzuge einheitliche Lösungen für einfachere Wiederverwendbarkeit