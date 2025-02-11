---
title: Verzögerung in SystemVerilog
description: Lernzettel - Digitaltechnik
draft: false
date: 2025-02-11
tags:
---
## Überblick
- Verzögerung in SystemVerilog: `#Zeiteinheiten`
- **Kein synthetisierbarer Code**, eine Verzögerung lässt sich nicht ohne weiteres in Hardware umsetzen
	$\Rightarrow$ Nur für Simulationen und Tests!

## Beispiel: Störimpuls
```Verilog
`timescale 1ns / 10ps // Zeiteinheit / Präzision f. Rundung
module example_delay(input logic a,b,c output logic y);
	logic n0, n1, n2, n3;
	assign #1 n0 = ~a;       // Verzögerung 1 Einheit
	assign #2 n1 = ~b;       // Verzögerung 1 Einheit
	assign #2 n2 = n0 & n1;  // Verzögerung 2 Einheiten
	assign #2 n3 = b & c;    // Verzögerung 2 Einheiten
	assign #1 y = n2 | n3;   // Verzögerung 1 Einheit
```
![[Pasted image 20250211181125.png]]
Nach 3 Nanosekunden tritt ein [[Zeitverhalten#Störimpulse (Glitches)|Störimpuls]], ein Glitch, auf, da sich $n_2$ nicht zeitgleich mit $n_3$ ändert, sondern leicht verzögert.