---
title: Speicherelemente
description: Lernzettel - Digitaltechnik
draft: false
date: 2025-02-12
tags:
---
## Bistabile Grundschaltung
- Grundlage des Zustandspeichers
- zwei Inverter mit Rückkopplung:
	- $Q_{\text{prev}}$ (previous $Q$)
- zwei Ausgänge: $Q,\overline Q$
- speichert 1 bit durch zwei stabile Zustände
	- $Q=0\Rightarrow\overline Q = 1 \Rightarrow Q=0$
	- $Q=1\Rightarrow\overline Q=0\Rightarrow Q = 1$
- keine Eingänge
	$\Rightarrow$ gespeicherter Zustand kann nicht beeinflusst werden
![[../../assets/Pasted image 20250212165738.png]]
> [!comment]
> Wie genau der Zustand der Schaltung ist, ist komplett zufällig. Wichtig ist, dass nachdem sich die Schaltung einmal eingependelt hat, sie diesen Zustand behält und ihn nicht ändert.
## SR-Latch
- bistabile Grundschaltung mit [[Logikgatter#NOR|NOR]] statt [[Logikgatter#NOT|NOT]]
- NOR: Ausgang `0`, wenn einer der Inputs `1` ist
- Interpretation der freien Eingänge $S$ und $R$
	- $\overline S\:\overline R\rightarrow$ Zustand halten ("latch" = verriegeln)
	- $\overline S\:R\rightarrow$ Zustand auf `0` zurücksetzen ("reset" $R$)
	- $S\:\overline R\rightarrow$ Zustand auf `1` setzen ("set" $S$)
	- $S\:R\rightarrow$ ungültiger Zustand ($Q=\overline Q=0$)
![[../../assets/Screenshot 2025-02-12 170514_inverted.png]]
## JK-Latch
- bistabile Grundschaltung mit SR-Latch und zwei [[Logikgatter#AND|AND]]-Gatter
- Ungültigen Zustand von SR am SR-Latch verhindern
- Historisch unklar, woher die Bezeichnung "JK" kommt
- Interpretation der freien Eingänge $J$ und $K$
	- $\overline J\:\overline K\rightarrow$ Zustand halten
	- $\overline J\:K\rightarrow$ Zustand auf `0` zurücksetzen, falls nötig
	- $J\:\overline K\rightarrow$ Zustand auf `1` setzen, falls nötig
	- $J\:K\rightarrow$ Zustand invertieren ("toggle")
![[../../assets/Screenshot 2025-02-12 171726_inverted.png]]
## D-Latch
- Daten-Latch mit Taktsignal (CLK) und Datensignale (D)
	- $\text{CLK}=1\rightarrow$ Zustand auf $D$ setzen (Latch transparent)
	- $\text{CLK}=0\rightarrow$ Zustand halten (Latch wird nicht transparent)
$\Rightarrow$ Ungültiger Zustand am SR-Latch wird vermieden
- Rückkopplung nur noch im SR-Latch
![[../../assets/Screenshot 2025-02-12 172335_inverted.png]]
## Problem des D-Latch
- periodische Taktsignale üblicherweise symmetrisch
	- `0`-Phase und `1`-Phase gleich lang
- D-Latch ist Taktphasen-gesteuert
	- für Hälfte der gesamten Zeit transparent
	- sequentielle Schaltungen mit D-Latches für Hälfte der Zeit kombinatorisch
- breites "Abtastfenster" sorgt für Unschärfe
	- bspw. unklar, ob Störimpuls übernommen wurde
![[../../assets/Pasted image 20250212172934.png]]
> [!comment]
> $Q_L$ übernimmt erst nachdem das Clocksignal auf `1` springt den Zustand von $D$. Allerdings ist unklar, wann genau das $D$ Signal übernommen wird. Wenn bspw. in dem Moment, in dem die Clock von `0` auf `1` springt ein Störimpuls in $D$ auftritt, ist unklar, ob dieser Störimpuls jetzt im D-Latch gespeicher ist oder nicht. 
## D-Flip-Flop
- Zwei D-Latches in Serie
	- First ($F$)
	- Second ($S$)
	- komplementäre Taktsignale
- $\text{CLK}=0$
	- First $F$ transparent $\rightarrow n = D$
	- Second $S$ nicht transparent $\rightarrow Q$  bleibt unverändert
- $\text{CLK}=1$
	- First $F$ nicht transparent $\rightarrow n$ bleibt unverändert
	- Second $S$ transparent $\rightarrow Q = n$
$\Rightarrow$ Taktflanken-gesteuert
- genau bei steigender $\text{CLK}$ Flanke wird $Q=D$
- es wird der Wert von $D$ übernommen, der *unmittelbar vor* der Taktflanke anliegt
![[../../assets/Screenshot 2025-02-12 173715_inverted.png]]
> [!comment]
> Der D-Flip-Flop übernimmt den Dateneingang $D$ genau in dem Moment, in dem die Clock von `0` auf `1` springt, bzw. exakt in dem Moment, in dem $\text{CLK}$ nicht mehr `0` ist. Der D-Flip-Flip ist einen Bruchteil später nicht mehr transparent und ignoriert alle Signale von $D$.
## Vergleich D-Latch mit D-Flip-Flop
![[../../assets/Pasted image 20250212174534.png]]

## Flip-Flops mit Taktfreigabe
- Freigabeeingang (Enable EN) steuert, wann Daten gespeichert werden
	- $EN=1\rightarrow D$ wird bei steigender CLK-Flanke gespeichert
	- $EN=0\rightarrow Q$ bleibt auch bei steigender CLK-Flanke unverändert
- Anwendungsbeispiele
	- Zähler
	- Speicher mit Adresscoder
![[../../assets/Screenshot 2025-02-12 174810_inverted.png]]
## Zurücksetzbare Flip-Flops
- Reset setzt internen Zustand unabhängig von $D$ auf `0`
	- synchron: nur zur steigenden Taktflanke wirksam
	- asynchron: jederzeit (unabhängig von CLK)
- Anwendungsbeispiele
	- sequentielle Schaltung in definierten Ausgangszustand versetzen
- setzbare Flip-Flops analog
![[../../assets/Screenshot 2025-02-12 175034_inverted.png]]
## Anwendungsbeispiel: (Shift-) Register
- Register bestehend aus parallelen D-Flip-Flops
- Bei Shift-Register ist $D_i=Q_{i-1}$
![[../../assets/Pasted image 20250212175204.png]]
