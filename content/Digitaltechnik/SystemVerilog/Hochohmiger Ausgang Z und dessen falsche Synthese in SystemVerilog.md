---
title: Hochohmiger Ausgang Z und dessen falsche Synthese in SystemVerilog
description: Lernzettel - Digitaltechnik
draft: false
date: 2025-02-11
tags:
---
## aa
```Verilog
module tristate (input logic a, input logic en, output logic y);
	assign y = en ? a : 1'bz;
endmodule
```
Wenn das Enable-Signal `1` ist, dann soll es `a` sein, sonst soll es [[Mehrwertige Logik#Z (ungetrieben / hochohmig) bei Tristate-Buffer|hochohmig]] sein. Die Ausgabe des [[Kombinatorische Logik in SystemVerilog#Synthese von Verhaltensbeschreibung|Synthesewerkzeugs]] ist falsch!

![[Pasted image 20250211183743.png]]
