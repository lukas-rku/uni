---
title: Arithmetische Grundschaltungen 2
description: Lernzettel - Digitaltechnik
draft: false
date: 2025-02-12
tags:
---
## Rekursiver Aufbau des Ripple-Carry-Adders

![[../../assets/Pasted image 20250212152338.png]]
- Aufteilen in unteres (==L==ow) und oberes (==H==igh) Halbwort ("Divide and Conquer")
- zweiter Addierer muss auf Übertrag aus erstem Addierer "warten"
$\Rightarrow$ [[Zeitverhalten#Kritische (lange) und kurze Pfade|kritische Pfade]] beider Teiladdierer werden addiert
- für schnellen Addierer müssen oberes und unteres Halbwort gleichzeitig bearbeitet werden
> [!comment]
>Das die Eingänge $\frac{2}{n}$ sind bedeutet, dass die Menge der Eingänge abhängig von der gewünscht Länge der berechenbaren Zahl ist. D.h., dass ein rekurisver Ripple-Carry-Adder auch mehr als 2 Eingänge haben kann. In dem r. RCA ist dann wieder erneut ein r. RCA, diesmal aber mit halb so vielen Eingängen, da die andere Hälfte von dem anderen "Zweig" der Rekursion bearbeitet wird.
## Conditional Sum Adder (CSA)

![[../../assets/Screenshot 2025-02-12 153213_inverted.png]]
- Übertrag vom unteren (L) in oberes (H) Halbwort kann nur `0` oder `1` sein
- für beide Optionen kann oberes Halbwort schon mal vorberechnet werden
- Auswahl des richtigen Ergebnisses, sobald tatsächlicher Übertrag bekannt
$\Rightarrow$ nach halbem CSA folgt nur noch ein [[Multiplexer und Dekodierer#MUX2|MUX]] auf kritischem Pfad
> [!comment]
> Der CSA berechnet vorläufig schon die Ergebnisse für beide Übertrags-Werte und entscheidet dann anhand des vorherigen RCA's welchen er schlussendlich ausgibt. Dieser Aufbau ist wieder rekursiv, dass heißt, dass in den CSA's immer wieder CSA's vorkommen bis man die benötigte Menge an Eingängen erreicht hat. Die Schaltung ist dadurch Schneller aber benötigt mehr Bauteile.
## Carry Lookahead Adder (CLA)
- für $A_iB_i=1$ ist $C_i=1$ unabhängig von $C_{i-1}$
$\Rightarrow$ Spalte $i$ generiert einen Übertrag ("generate")
![[../../assets/Screenshot 2025-02-12 155621_inverted.png]]
>[!comment]
>Egal was der Eingang $C_{i-1}$ des RCA's ist, wenn die beiden oberen Eingänge $A$ und $B$ `1` ist, ist auch der ausgehende Übertrag `1`.

---
- für $A_iB_i=1$ ist $C_i=1$ wenn $C_{i-1}=1$
$\Rightarrow$ Spalte $i$ leitet einen Übertrag weiter ("propagate")
![[../../assets/Screenshot 2025-02-12 155648_inverted.png]]
>[!comment]
>Wenn einer der Eingänge $A$ oder $B$ `1` ist und der eingehende Übertrag $C_{i-1}$ auch `1`, dann ist der ausgehende Übertrag auch immer `1`.

---
- für $A_iB_i=0$ ist $C_i=0$ unabhängig von  $C_{i-1}$
$\Rightarrow$ Spalte $i$ leitet einen Übertrag nicht weiter
![[../../assets/Screenshot 2025-02-12 155718_inverted.png]]
>[!comment]
>Wenn beide Eingänge $A$ oder $B$ `0` sind, dann ist auch der ausgehende Übertrag $C_i$ auch immer `0`.

### Generate und Propagate pro Spalte
- Generate-Flag für Spalte $i$: $G_i = A_iB_i$           *Wenn $A_i$ und $B_i$ `1` sind*
- Propagate-Flag für Spalte $i$: $P_i=A_i+B_i$     *Wenn $A_i$ oder $B_i$ `1` sind*
$\Rightarrow$ aus Spalte $i$: $C_i = G_i+P_i\:C_{i-1}$

- Bei naiver Verwendung davon (links) kein Vorteil gegenüber [[Arithmetische Grundschaltungen#Volladdierer|Volladdierer]] (rechts):
	- In beiden Fällen [[Logikgatter#AND|AND]] und [[Logikgatter#OR|OR]] auf kritischem Pfad zwischen $C_{i-1}$ und $C_i$
![[../../assets/Pasted image 20250212161023.png]]
### Generate und Propagate über k Spalten
- Generate- und Propagate-Flags können über mehrere Spalten kombiniert werden (hier gezeigt für $k=4$ Spalten)
- $k$-Spalten Block propagiert Übertrag, wenn jede einzelne Spalte propagiert
$\Rightarrow$ $P_{\:3:0}=P_3\:P_2\:P_1\:P_0$

- k-Spalten Block generiert Übertrag, wenn eine der Spalten generiert, und alle andere Spalten darüber propagieren
$\Rightarrow$ $G_{\:3:0}=G_3+P_3G_2+P_3P_2G_1+P_3P_2P_1G_0$

- Übertrag überspringt $k$ Spalten auf einmal:
$$
\begin{align*}
C_n&=G_{n:n-k+1}&+C_{n-k}\cdot P_{n:n-k+1}\\
&=(G_n+P_n(G_{n-1}+\dots+(P_{n-k+2}G_{n-k+1})))&+C_{n-k}\cdot\prod^n_{i=n-k+1}P_i
\end{align*}
$$
### Block für k Spalten
- Addierer in $\frac{N}{k}$ jeweils $k$ bit breite Blöcke unterteilen
- Jeder Block besteht aus
	- einem RCA zum Berechnen der Summ $S_{n:n-k+1}$
	- einer Schaltung zur schnellen Berechnung des Carries $C_n$ aus $G_{n:n-k+1}+C_{n-k}$, $P_{n:n-k+1}$ und $C_{n-k}$
	- durch die zusätzliche Schaltung erhalten folgende Blöcke schneller ihr Carry-In
![[../../assets/Screenshot 2025-02-12 162929_inverted.png]]
### Block für k = 4 Spalten
Oben der RCA und unten der "kürzere" CLA
![[../../assets/Screenshot 2025-02-12 163049_inverted.png]]
$$
C_n=(G_n+P_n+(G_{n-1}+\dots+(P_{n-k+2G_{m-k+1}})))+C_{n-k}\:\cdot \prod^n_{i=n-k+1}P_i
$$
>[!comment]
>Das große AND4 Bauteil unten rechts bearbeitet den rechten Teil der Gleichung ($C_{n-k}\:\cdot \prod^n_{i=n-k+1}P_i$) und die Treppe an AND und OR Gates berechnet den linken Teil der Gleichung ($(G_n+P_n+(G_{n-1}+\dots+(P_{n-k+2G_{m-k+1}})))$).
>
>Der kritische Pfad ist nun der markierte Pfad, welcher wesentlich kürzer ist als bei einem RCA. Zudem ändert sich dieser bei einer höheren Spaltenzahl, im Gegensatz zum RCA, nicht.

### Kritischer Pfad
- Propagate und Generate Signale in allen Blöcken gleichzeitig berechnen
- für große Bitbreiten $N$ dominiert $\frac{N}{k}\cdot(t_{pd,\:AND}+t_{pd,\: OR})$
$\Rightarrow$ Blöcke möglichst groß wählen (kostet aber mehr Ressourcen)
- kritischer Pfad für $N=20$ bit und $k=4$:
	- RCA: $\approx 20 \cdot (t_{pd,\:AND}+t_{pd,\: OR})$
	- CLA: $\approx 10 \cdot (t_{pd,\:AND}+t_{pd,\: OR})$
		- $G$/$P$ von Block 1
		- Carry zum letzten Block
		- RCA im letzten Block
![[../../assets/Pasted image 20250212163948.png]]
## Weitere schnelle Addierer
- Parallel Prefix Adder
	- alle $C_i$ per Generate und Propagate möglichst schnell bestimmen
	- Kritischer Pfad logarithmisch in Bitbreite $N$
- Carry-Save Adder
	- Verwendet parallele Volladdierer, um 3 Werte in Vektor aus Carries $C_i$ und Summen $S_i$ zu addieren