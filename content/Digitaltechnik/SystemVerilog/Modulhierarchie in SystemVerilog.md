---
title: Modulhierarchie in SystemVerilog
description: Lernzettel - Digitaltechnik
draft: false
date: 2025-02-10
tags:
---

## Strukturbeschreibung - Modulinstanziierung
*`and3.sv`*
```verilog
module and3(input logic a, b, c, output logic y);
	assign y = a & b & c;
endmodule
```

*`inv.sv`*
```verilog
module inv(input logic a, output logic y);
	assign y = ~a;
endmodule
```

*`nand3.sv`*
```verilog
module nand3(input logic d, e, f, output logic w);
	logic s;                     // internes Signal für Modulverbindung
	and3 andgate(d, e, f, s);    // Instanz von and3 namens andgate
	inv inverter(s, w);          // Instanz von inv namens inverter
endmodule
```
![[../../assets/Screenshot 2025-02-10 171420_inverted.png]]

## Portzuweisung nach Position oder Namen
*`nand3_named.sv`*
```verilog
module nand3_named(input logic d, e, f, output logic w);
	logic s;
	and3 andgate(a.(d), .b(e), .y(s));
	inv inverter(.a(s), .y(w));
endmodule
```
*Der Eingang, der `a` heißt, dem Übergebe ich den Wert `d`.*

- 10 bis 100 ports pro Modul nicht unüblicher
- absolute Portzuweisung per Namen übersichtlicher