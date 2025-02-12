---
title: Sequentielle Schaltungen
description: Lernzettel - Digitaltechnik
draft: false
date: 2025-02-12
tags:
---
## Rückblick: [[Kombinatorische Logik|Kombinatorische Schaltungen]]
- kombinatorische Logik ("Schaltnetz")
	- Ausgänge hängen nur von aktuellen Eingangswerten ab
- Warum reichen kombinatorische Schaltungen nicht aus?
	- Nicht alle Funktionalitäten lassen sich sinnvoll als kombinatorische Schaltung realisieren
		- (Zwischen-) Ergebnisse können nicht gespeichert / wiederverwendet werden
		- kritische Pfade können nicht beliebig lang werden
	- Zeitverhalten bei kombinatorischen Schaltungen schwer kontrollierbar (siehe [[Zeitverhalten|Timing-Analyse]])

## Sequentielle Schaltungen
- Ausgänge hängen ab von
	- aktuellen Eingabewerten
	- vorherigen Eingabewerten
$\Rightarrow$ sequentielle Schaltung speichert internen Zustand
- (Kurzzeit-)  Gedächtnis repräsentiert bisherige Eingabesequenzen
- realisiert durch Rückkopplung von Ausgängen
	$\Rightarrow$ nicht kombinatorisch