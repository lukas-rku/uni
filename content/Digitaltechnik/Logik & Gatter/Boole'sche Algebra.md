---
title: Boole'sche Algebra
description: Lernzettel - Digitaltechnik
draft: false
date: 2025-02-11
tags:
---
## Grundlagen
- Rechenregeln [[Boole'sche Gleichungen|boole'scher Gleichungen]]
	- Axiome: grundlegende Annahmen der Algebra (nicht beweisbar)
	- Theoreme: komplexere Regeln, die sich aus Axiomen ergeben (beweisbar)
- analog zur Algebra auf natürlichen Zahlen
- ergänzt um Optimierungen durch Begrenzung auf $\mathbb{B}$
- Axiome und Theoreme haben jeweils duale Entsprechung: AND $\leftrightarrow$ OR, `0` $\leftrightarrow$ `1`

## Axiome der boole'schen Algebra
|     | Axiom                        | Duales Axiom                      | Bedeutung  |
| --- | ---------------------------- | --------------------------------- | ---------- |
| A1  | $B \neq 1 \Rightarrow B = 0$ | A1': $B \neq 0 \Rightarrow B = 1$ | Dualität   |
| A2  | $\overline{0} = 1$           | A2': $\overline{1} = 0$           | Negieren   |
| A3  | $0 \cdot 0 = 0$              | A3': $1 + 1 = 1$                  | Und / Oder |
| A4  | $1 \cdot 1 = 1$              | A4': $0 + 0 = 0$                  | Und / Oder |
| A5  | $0 \cdot 1 = 1 \cdot 0 = 0$  | A5': $1 + 0 = 0 + 1 = 1$          | Und / Oder |

## Theoreme der boole'schen Algebra
| Theorem                                                                                              | Duales Theorem                                                                                        | Bedeutung       |
| ---------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | --------------- |
| T1: $A \cdot 1 = A$                                                                                  | T1': $A + 0 = A$                                                                                      | Neutralität     |
| T2: $A \cdot 0 = 0$                                                                                  | T2': $A + 1 = 1$                                                                                      | Extremum        |
| T3: $A \cdot A = A$                                                                                  | T3': $A + A = A$                                                                                      | Idempotenz      |
| T4: $\overline{\overline{A}} = A$                                                                    | T4': $\overline{\overline{A}} = A$                                                                    | Involution      |
| T5: $A \cdot \overline{A} = 0$                                                                       | T5': $A + \overline{A} = 1$                                                                           | Komplement      |
| T6: $A \cdot B = B \cdot A$                                                                          | T6': $A + B = B + A$                                                                                  | Kommutativität  |
| T7: $A \cdot (B \cdot C) = (A \cdot B)\cdot C$                                                       | T7': $A + (B + C) = (A + B) + C$                                                                      | Assoziativität  |
| T8: $A \cdot (B + C) = (A \cdot B) + (A \cdot C)$                                                    | T8': $A + (B \cdot C) = (A + B)\cdot(A + C)$                                                          | Distributivität |
| T9: $A \cdot (A + B) = A$                                                                            | T9': $A + (A \cdot B) = A$                                                                            | Absorption      |
| T10: $(A \cdot B) + (A \cdot \overline{B}) = A$                                                      | T10': $(A + B)\cdot (A + \overline{B}) = A$                                                           | Zusammenfassen  |
| T11: $(A \cdot B) + (\overline{A} \cdot C) + (B \cdot C)$ = $(A \cdot B) + (\overline A \cdot C)$    | T11': $(A + B)\cdot (\overline{A} + C)\cdot (B + C)$ = $(A + B)\cdot (A + C)$                         | Konsensus       |
| T12: $\overline{A \cdot B \cdot C \cdot \dots} = \overline{A} + \overline{B} + \overline{C} + \dots$ | T12': $\overline{A + B + C + \dots} = \overline{A} \cdot \overline{B} \cdot \overline{C} \cdot \dots$ | De Morgan       |
## Theorome grafisch
### T1: Neutralität von 1 und 0
![[../../assets/Pasted image 20250211135256.png]]
### T2: Extremum von 0 und 1
![[../../assets/Pasted image 20250211135355.png]]
### T3: Idempotenz
![[../../assets/Pasted image 20250211135411.png]]
### T4: Involution
![[../../assets/Pasted image 20250211135434.png]]
### T5: Komplement
![[../../assets/Pasted image 20250211135449.png]]
### T6: Kommutativität
![[../../assets/Pasted image 20250211135516.png]]
### T7: Assoziativität
![[../../assets/Pasted image 20250211135534.png]]
### T8: Distributivität
![[../../assets/Pasted image 20250211135554.png]]
### T9: Absorption
![[../../assets/Pasted image 20250211135610.png]]
### T10: Zusammenfassen
![[../../assets/Pasted image 20250211135633.png]]
### T11: Konsensus
![[../../assets/Pasted image 20250211135652.png]]
### T12: De Morgan
![[../../assets/Pasted image 20250211135707.png]]
## Beweis für Theoreme
- Methode 1: Überprüfen aller Möglichkeiten
- Methode 2: Gleichung durch Axiome und andere Theoreme vereinfachen

## Beweis für [[#T8 Distributivität|Distributivität]] (T8)
Durch Überprüfen aller Möglichkeiten

| $A$ | $B$ | $C$ | $B + C$ | ==$A(B + C)$== | $AB$ | $AC$ | ==$AB + AC$== |
| --- | --- | --- | ------- | -------------- | ---- | ---- | ------------- |
| $0$ | $0$ | $0$ | $0$     | $0$            | $0$  | $0$  | $0$           |
| $0$ | $0$ | $1$ | $1$     | $0$            | $0$  | $0$  | $0$           |
| $0$ | $1$ | $0$ | $1$     | $0$            | $0$  | $0$  | $0$           |
| $0$ | $1$ | $1$ | $1$     | $0$            | $0$  | $0$  | $0$           |
| $1$ | $0$ | $0$ | $0$     | $0$            | $0$  | $0$  | $0$           |
| $1$ | $0$ | $1$ | $1$     | $1$            | $0$  | $1$  | $1$           |
| $1$ | $1$ | $0$ | $1$     | $1$            | $1$  | $0$  | $1$           |
| $1$ | $1$ | $1$ | $1$     | $1$            | $1$  | $1$  | $1$           |
## Beweis für [[#T9 Absorption|Absorption]] (T9)
Durch Anwendung von Axiomen und Theoremen

| $A\cdot(A+B)$          | [[#T8 Distributivität\|Distributivität]]     |
| ---------------------- | -------------------------------------------------------------- |
| $A\cdot A + A \cdot B$ | [[#T3 Idempotenz\|Idempotenz]]               |
| $A+A\cdot B$           | [[#T1 Neutralität von 1 und 0\|Neutralität]] |
| $A\cdot 1 + A \cdot B$ | [[#T8 Distributivität\|Distributivität]]     |
| $A\cdot(1+B)$          | [[#T2 Extremum von 0 und 1\|Extremum]]       |
| $A\cdot1$              | [[#T1 Neutralität von 1 und 0\|Neutralität]] |
| A                      | $\text{q.e.d}$                                                 |
## Beweis für [[#T11 Konsensus|Konsensus]] (T11)
Durch Anwendung von Axiomen und Theoremen
![[../../assets/Pasted image 20250211143113.png]]

## Logikminimierung
- Gatter-Realisierung per DNF kann sehr aufwändig sein
- Logik (Anzahl Literale und Operatoren) minimieren
![[../../assets/Screenshot 2025-02-11 143355_inverted.png]]
## Anwendung von Axiome und Theoreme für Logikminimierung
$$
\begin{align*}
Y&=\overline A \overline B \overline C = \overline A \overline B C+A \overline B \overline C+A \overline B C+ABC\\
&=\overline A (\overline B \overline C + \overline B C)+ A(\overline B \overline C + \overline B C) + ABC\\
&=\overline A(\overline B (\overline C + C)) + A ( \overline B ( \overline C + C))+ABC\\
&= \overline A \overline B+A \overline B + ABC\\
&=(\overline A + A) \overline B +ABC\\
&=\overline B + ABC
\end{align*}
$$
- weitere Vereinfachungen möglich?
	- $Y=\overline B+AC$
![[../../assets/Screenshot 2025-02-11 144314_inverted.png]]
- Systematik notwendig, um minimale Ausdrücke zu erkennen/finden