---
title: Feldeffekt-Transistoren
description: Lernzettel - Digitaltechnik
draft: false
date: 2025-02-10
tags:
---
## Transistoren
- [[Logikgatter|Logikgatter]] werden üblicherweise aus Transistoren aufgebaut
	- heute überwiegend Feldeffekttransistor (FET, "Field Effect Transistor")
- Transistoren sind spannungsgesteuerte Schalter
	- zwei Anschlüsse (Source $s$ & Drain $d$), werden je nach Spannung am dritten Eingang (Gate $g$) verbunden oder getrennt
![[Screenshot 2025-02-10 135931_inverted.png]]
## Der Feldeffekt
![[Screenshot 2025-02-10 140143_inverted.png]]
- zwei metallische Streifen mit dünner isolierender Zwischenlage
- Streifen bilden Plattenkondensator (Kapazität $C$)
- Steuerspannung $V_g$ an Kondensator lädt diesen auf
	- jeweils Ladung $Q=C\cdot V_g$ auf beiden Streifen (gegensätzliche Ladung)
	- $V_g$ beeinflusst Menge der freien Ladungsträger, also Widerstand $R_{sd}$

- etwa $10^{14}$ zusätzliche freie Ladungsträger pro Kubikzentimeter $f$. $V_g=1V$
- etwa $10^{22}$ freie Ladungsträger pro Kubikzentimeter in Metallen
	- Ladungsträgeranreicherung durch Feldeffekt in Metallen unerheblich

- aber etwa $10^{13}$ freie Ladungsträger pro Kubikzentimeter in Halbleitern
	- erst mit Halbleitern wird Feldeffekt technisch nutzbar

## Silizium-basierte Halbleiter
- reines Silizium ist schlechter Leiter (keine freien Ladungsträger)
- Dotierung ermöglicht gezieltes einbringen freier Ladungsträger
![[Screenshot 2025-02-10 140903_inverted.png]]
- Durch Dotierung können gezielt Elektronen entfernt oder hinzugefügt werden.
- p-Dotiert = Löcher
- n-Dotiert = Elektronenüberschuss

## P/N Übergang = Diode
![[Screenshot 2025-02-10 141326_inverted.png]]
Elektronen werden im zweiten Schritt durch die Batterie in die mittlere Zone gedrückt. Dadurch ist die Schwelle durch sie wesentlich geringer weshalb der Transistor anfängt zu leiten. Wenn die Batterie allerdings anders herum angeschlossen wird, werden die Elektronen an die Ränder gedrückt wodurch die neutrale Zone größer wird. Der Transistor leitet erst recht nicht. 

Also: Eine Diode leitet von p-Typ nach n-Typ, aber nicht von n-Typ nach p-Typ.

## MOS Feldeffekttransistoren (MOSFETs)
- Metalloxid-Halbleiter (MOS) Transistoren
	- Undotiertes Silizium (früher Metallschicht) für Gate
	- Oxid (Siliziumdioxid = Glas) für Isolator
	- Dotiertes Silizium für Substrat und Anschlüsse
![[Screenshot 2025-02-10 142218_inverted.png]]

## nMos
- Gate = `0`, ausgeschaltet (keine Source-Drain Verbindung)
	- zwischen n -> p entsteht eine Depletion Zone
- Gate = `1`, eingeschaltet (leitfähiger Source-Drain Kanal)
	- Kondensator bei $V_{DD}$ lädt sich auf
	- Der Feldeffekt erzeugt einen "Kanal". Die zusätzlichen Elektronen neutralisieren die Depletion Zone

![[Screenshot 2025-02-10 142506_inverted.png]]
- Majoritätsleitungsträger sind Elektronen
- leiten `0`'en gut von Source nach Drain weiter
## pMOS
- Gate = `1`, ausgeschaltet (keine Source-Drain Verbindung)
- Gate = `0`, eingeschaltet (leitfähiger Source-Drain Kanal)

![[Screenshot 2025-02-10 143304_inverted.png]]

- Majoritätsleitungsträger sind Löcher
- leiten `1`'en gut von Source nach Drain weiter

## MOSFET Schaltverhalten
![[Screenshot 2025-02-10 143658_inverted.png]]