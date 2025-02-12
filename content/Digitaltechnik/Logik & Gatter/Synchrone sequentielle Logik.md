---
title: Synchrone sequentielle Logik
description: Lernzettel - Digitaltechnik
draft: false
date: 2025-02-12
tags:
---
## Sequentielle Logik
- alle nicht-kombinatorischen Schaltungen (bspw. [[Sequentielle Schaltungen|sequentielle Schaltungen]])
- erlaubt Rückkopplungen, beispielsweise:
![[../../assets/Pasted image 20250212175358.png]]
$\Rightarrow$ instabile (oszillierende) Schaltung
- Verhalten abhängig von Herstellungsprozess, Spannung, Temperatur
- nicht vorhersagbar
## Entwurf synchroner sequentieller Logik
- Rückkopplung durch Register aufbrechen
	- halten den Zustand der Schaltung
	- ändern Zustand nur zur Taktflanke
	$\Rightarrow$ gesamte Schaltung synchronisiert mit Taktflanke
![[../../assets/Pasted image 20250212175705.png]]
## Synchrone sequentielle Schaltungen
- Regeln für Aufbau
	- jedes Schaltungselement ist entweder Register oder kombinatorische Schaltung
	- mindestens ein Schaltungselement ist ein Register
	- alle Register werden durch gleiches Taktsignal gesteuert
	- jeder zyklische Pfad enthält mindestes ein Register
- Anwendungsbeispiele
	- Pipelines %%Link Pipelines%%
	- Endliche Zustandsautomaten %%Link endliche Zustandsautomaten%%
- Wie schnell kann so eine Schaltung betrieben werden?
	$\Rightarrow$ Was ist die kürzeste Taktperiode? %%Link Taktperiode%%