---
title: Kombinatorische Logik in SystemVerilog
description: Lernzettel - Digitaltechnik
draft: false
date: 2025-02-11
tags:
---
## Module
- Ein Modul beschreibt wie eine Aufgabe (Berechnung) durchgeführt wird
	- Ähnlich einer Funktion in Programmiersprachen
- Schnittstellenbeschreibung:
	- Eingänge
	- Ausgänge
	- (Parameter)
- zwei Arten von Modul-Beschreibungen:
	- Strukturbeschreibung: Wie ist die Schaltung aus (Sub-)Modulen aufgebaut?
	- Verhaltensbeschreibung: Was tut die Schaltung
- strukturelle Modul-Hierarchie mit Verhaltensbeschreibung auf unterster Ebene
![[../../assets/Screenshot 2025-02-10 164334_inverted.png]]
## Beispiel für Verhaltensbeschreibung
```verilog
module example(input logic a, b, c, output logic y);

	assign y = ~a & ~b & ~c | a & ~b & ~c | a & ~b & ~c;

endmodule
```

^452699

| Bezeichnung       | Beschreibung                                                                                                                                                                               |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `module`          | Beginn der Schnittstellenbeschreibung                                                                                                                                                      |
| `example`         | Modulname                                                                                                                                                                                  |
| `input`, `output` | Port-Richtung                                                                                                                                                                              |
| `logic`           | Port-Datentyp                                                                                                                                                                              |
| `a, b, c, y`      | Port-Namen                                                                                                                                                                                 |
| `assign`          | ([[Kombinatorische Logik\|kombinatorische]]) Signalzuweisung                                                                                                                               |
| `~`, `&`, \|      | ([[Kombinatorische Logik\|kombinatorische]]) Operatoren ([[../Logik & Gatter/Logikgatter#NOT\|NOT]], [[../Logik & Gatter/Logikgatter#AND\|AND]], [[../Logik & Gatter/Logikgatter#OR\|OR]]) |
| `endmodule`       | Ende der Schnittstellenbeschreibung                                                                                                                                                        |
*Man kann eine beliebige [[../Logik & Gatter/Kombinatorische Logik|kombinatorische Logik]] eins zu eins abtippen.*
## Simulation von Verhaltensbeschreibungen
Plot mit Opensource Tools `Icarus Verilog` + `GTKWave`
![[../../assets/Screenshot 2025-02-10 165555_inverted.png]]
Man kann sehen, dass die [[../Logik & Gatter/Boole'sche Gleichungen#Minterm|Minterme]] von [[#^452699|example]] bei der ersten, fünften und sechsten Zeiteinheit bei `y = 1` sind.
## Synthese von Verhaltensbeschreibung
Plot mit Open-Source Tools `YoSyS` + `GraphViz`
![[../../assets/Screenshot 2025-02-10 170304_inverted.png]]

## Bitweise Verknüpfungsoperatoren
```Verilog
module gates (input logic [3:0] a, b, // 4 bit Vektoren
			  output logic [3:0] y1, y2, y3, y4, y5);

	/* Fünf unterschiedliche Logikgatter 
	   mit zwei Eingängen, jeweils 4 bit Vektoren */
	assign y1 = a & b;  /* AND wird auf jedes Element von a und b 
					       getrennt angwendet: y[0] = a[0] & b[0]... */
	assign y2 = a | b;
	assign y3 = a ^ b;
	assign y4 = a ~& b;
	assign y5 = a ~| b; 

endmodule
```

## Logische Verknüpfungsoperatoren
Achtung: Logische Operatoren $\not =$ bitweise Operatoren
```Verilog
module gates_logic (input logic [3:0] a, b, // 4 bit Vektoren
				    output logic [3:0] y,
				    output logic z);

	assign y = a & b;  // y[0] = (a[0] & b[0]), ...
	assign z = a && b; // z = (a[0] | a[1] | a[2] | a[3])
					   //   & (b[0] | b[1] | b[2] | b[3])
```
Die Ausgabe von `z` ist `1`, wenn irgendein bit von `a = 1` ist und irgendein bit von `b = 1` ist. `z` wäre also bspw. `1` wenn `a[0] = 1` und `b[2] = 1`. Allerdings ist `z = 0`, wenn der Inhalt einer der beiden oder beider Vektoren `0` ist.

## Reduktionsoperatoren (unär)
"unär" heißt, dass die Operation wird nur auf einen Operanden angewendet wird.
```Verilog
moduel and8 (input logic [7:0] a, output logic y);

	//assign y = a[7] & a[6] & a[5] & a[4] & 
	//  	     a[3] & a[2] & a[1] & a[0];
	assign y = &a;

endmodule
```
- analog:
	- `|` OR
	- `^` XOR
	- `~|` NOR
	- `~&` NAND
	- `~^` XNOR

## MUX auf Vektoren
Ternäre Operationen
```Verilog
module mux2x4 (input logic [3:0] d0, d1,
			   input logic s,
			   output logic [3:0] y);

	assign y = s ? d1 : d0;

endmodule
```
![[../../assets/Pasted image 20250212111048.png]]
## Interne Verbingungsknoten (Signale)
```Verilog
module fulladder(input logic a, b, cin,
				 output logic s, cout);

	logic p, g;   // Interne Verbindungsknoten
	assign p = a ^ b;
	assign g = a & b;
	assign s = p ^ cin;
	assign cout = g | (p & cin);
```
![[../../assets/Pasted image 20250212111301.png]]
## Konkatenation
```Verilog
module concat(input logic [2:0] a, b,
			  output logic [11:0] x, 
			  output logic y, 
			  output logic [2:0] z);

	assign x = {a[2:1], {3{b[0]}}, a[0], 6'b100010};
	// x = a[2] a[1] b[0] b[0] b[0] a[0] 100010

	assign {y, z} = 4'b1010;
	// y = 1; z = 010;
endmodule
```
Bei der Konkatenation wird einfach ein Vektor aus anderen Werten oder Vektoren zusammengeklebt. Mit einer `3` wird das einzufügende Element drei mal eingefügt.
![[../../assets/Pasted image 20250212111557.png]]

## Bindung von Operatoren (Präzedenz)
```
Da Darstellungsfehler:
¦ = |
```

| Priorität (hoch → niedrig) | Operator(en)             | Bedeutung                                          |
| -------------------------- | ------------------------ | -------------------------------------------------- |
| 1 (höchste)                | `[]`                     | Zugriff auf Vektorelement                          |
| 2                          | `~`, `!`, `&`,`¦` , `^`  | unäre Operatoren: NOT, Negation, Reduktion         |
| 3                          | `*`, `/`, `%`            | Multiplikation, Division, Modulo                   |
| 4                          | `+`, `-`                 | Addition, Subtraktion                              |
| 5                          | `<<`, `>>`, `<<<`, `>>>` | logischer und arithmetischer Shift                 |
| 6                          | `<`, `<=`, `>`, `>=`     | Vergleich                                          |
| 7                          | `==`, `!=`               | gleich, ungleich                                   |
| 8                          | `&`, `~&`                | bitweises AND, NAND                                |
| 9                          | `^`, `~^`                | bitweises XOR, XNOR                                |
| 10                         | `¦`, `~¦`                | bitweises OR, NOR                                  |
| 11                         | `&&`                     | logisches AND (wahr, wenn alle Bits 1 sind)        |
| 12                         | `¦¦`                     | logisches OR (wahr, wenn mindestens ein Bit 1 ist) |
| 13                         | `?:`                     | ternärer Operator                                  |
| 14 (niedrigste)            | `{}`                     | Konkatenation                                      |
## Wiederholung: Assign Statement
```Verilog
module example(input logic a, b, c, output logic y);
	assign y = ~a & ~b & ~c | a & ~b & ~c | a & ~b & c;
endmodule
```
- auch continuous assignment genannt, da `y` immer neu berechnet wird sobald sich etwas an `a`, `b`, oder `c` ändert.
- Linke Seite (LHS, "left hand side"): Variable oder Port
- Rechte Seite (RHS, "right hand side"): logischer Ausdruck
- Zuweisung, wenn der Wert von RHS sich ändert

## Alternative für kombinatorische Logik: Der `always_comb` Block
```Verilog
module ex_always_comb(input logic a, b, c, output logic y);
	always_comb y = ~a & ~b & ~c | a & ~b & ~c | a & ~b & c;
endmodule
```
- `always_comb <instruction>`
	- Zuweisung ebenfalls, wenn sich der Wert von RHS ändert
	- LHS Variablen dürfen nicht von anderen Blöcken geschrieben werden

## Zwei Möglichkeiten für kombinatorische Logik
Die Synthese beider Module ergibt den gleichen Schaltplan
![[../../assets/Pasted image 20250212113055.png]]
## `if-else`-Konstrukt
Anwendung des `always_comb` Block
```Verilog
module swap(input logic a1, b1, s, output logic a2, b2);

	always_comb begin
		if (s) begin
			a2 = b1;
			b2 = a1;
		end else begin
			a2 = a1;
			b2 = b1;
		end
	end

endmodule
```
- `if-else` darf nur in `always_comb` und `always/always_ff/...` Blöcken verwendet werden

![[../../assets/Pasted image 20250212113311.png]]
## Synthese von `if-else`
```Verilog
module swap_assign(input logic a1, b1, s, output logic a2, b2);

	assign b2 = s ? a1 : b1;
	assign a2 = s ? b1 : a1;

endmodule
```
Gleiche Synthese wie das Modul `swap` von oben:
![[../../assets/Pasted image 20250212113516.png]]
## Fallunterscheidung `case`
```Verilog
module sevenseg (
    input  logic [3:0] A,
    output logic [6:0] S
);

    always_comb begin
        case (A)
            0:        S = 7'b011_1111;
            1:        S = 7'b000_0110;
            2:        S = 7'b101_1011;
            3:        S = 7'b100_1111;
            4:        S = 7'b110_0110;
            5:        S = 7'b110_1101;
            6:        S = 7'b111_1101;
            7:        S = 7'b000_0111;
            8:        S = 7'b111_1111;
            9:        S = 7'b110_1111;
            default:  S = 7'b000_0000;
        endcase
    end

endmodule
```
- case darf nur in `always_comb` und `always` Blöcken verwendet werden
- für kombinatorische Logik müssen alle Eingabe-Optionen abgedeckt werden
- explizit oder per `default` ("alle anderen")
![[../../assets/Screenshot 2025-02-12 113716_inverted.png]]
## Fallunterscheidung `casez`
```Verilog
module priority_encoder (
    input  logic [3:0] A,
    output logic [3:0] Y
);

    always_comb begin
        casez (A) // casez erlaubt Don't-Cares
            4'b1???: Y = 4'b1000; // ? = Don't Care
            4'b01??: Y = 4'b0100;
            4'b001?: Y = 4'b0010;
            4'b0001: Y = 4'b0001;
            default: Y = 4'b0000;
        endcase
    end

endmodule

```
![[../../assets/Pasted image 20250212114000.png]]
## Eigenschaften von `assign` und `always_comb`
- werden bei Simulation immer ausgeführt, wenn sich ein Signal auf der rechten Seite ändert
- erlauben nur kombinatorische Logik
- Reihenfolge im Quellcode oft nicht relevant
	- nebenläufige Signalzuweisungen ("concurrent signal assignements")
	- **Aber:** Blockierende Signalzuweisungen (`a = b`) innerhalb von Blöcken `begin` / `end` werden nacheinander ausgeführt.