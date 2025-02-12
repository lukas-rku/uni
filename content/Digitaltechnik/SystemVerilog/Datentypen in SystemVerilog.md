---
title: Datentypen in SystemVerilog
description: Lernzettel - Digitaltechnik
draft: false
date: 2025-02-12
tags:
---
## Auswahl wichtiger Datentypen
==*Relevant*==
- `bit` = `{1'b0, 1b'1}` (zweiwertige Logik)
- ==`logic`== = `{1'b0, a'b1, 1'bx, 1'bz} = bit signed` (vierwertige Logik)
- `int` = `{-2**31, ..., 2**31-1} = bit signed [31:0]`
- `integer` = `{-2**31, ..., 2**31-1} = logic signed [31:0]`
- ==`enum`== = Aufzählung symbolischer Werte (bspw. für endliche Automaten)
- `time, real, typedef, struct, ...`
- ==Vektoren und Arrays==

## Vektoren
```Verilog
module vectors(input logic [3:0] A,B,        // 4 bit Vektoren [MSB:LSB]
               output logic [7:0] JOINED,    // 8 bit Vektor   [MSB:LSB]
               output logic MSB, 
               output logic [3:0] A_FLIPPED_MSB);

	assign JOINED[7:4] = A;            // Vektorbereich überschreiben
	assign JOINED[3:0] = B;            // Vektorbereich überschreiben

	assign MSB = A[3];                 // Einzelnes Vektorbit lesen

	assign A_FLIPPED_MSB[3] = ~A[3];   // Einzelnes Vektorbit lesen/schreiben
	assign A_FLIPPED_MSB[2:0] = A[2:0];

endmodule
```
![[../../assets/Pasted image 20250212103523.png]]
Aufbau von `JOINED`:
![[../../assets/Screenshot 2025-02-12 103645_inverted.png]]
## Operationen auf Vektoren
```Verilog
module vecop(input logic [3:0] A, B, output logic [3:0] U, V, X, output logic [7:0] Y);

	// Bitweise Verknüpfung
	assign U = A & B;   // U[0] = (A[0] & B[0]), V[1] = (A[1] & B[1])...
	assign V = A ^ B;   // V[0] = (A[0] ^ B[0]), V[1] = (A[1] ^ B[1])...

	// (unsigned) Arithmetik
	assign X = A + B;
	assign Y = A * B;

endmodule
```
![[../../assets/Pasted image 20250212104219.png]]
## Synthese von Operationen auf Vektoren
Von Operationen auf Vektoren wird in der Realität abgeraten aus dem folgenden Grund:
![[../../assets/Pasted image 20250212104341.png]]
## Vektoren $\not=$ Arrays
```Verilog
logic [3:0] A;        // 4 bit Vektor
logic A [1:0];        // Array mit 2 bits
logic [3:0] A [1:0];  // Array mit 2 4 bit Vektoren
```
- SystemVerilog unterstützt Vektoren und Arrays
- Arrays unterstützen jedoch weniger Operationen, beispielsweise keine bitweisen oder arithmetischen Operationen
$\Rightarrow$ Vektoren als einen Haufen Drähte
$\Rightarrow$ Arrays als Darstellung von Speicher