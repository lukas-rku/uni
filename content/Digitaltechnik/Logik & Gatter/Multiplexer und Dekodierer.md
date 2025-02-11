---
title: Multiplexer und Dekodierer
description: Lernzettel - Digitaltechnik
draft: false
date: 2025-02-11
tags:
---
## Multiplexer
MUX$n:\mathbb{B}^{n+\lceil log_2\:n\rceil}\rightarrow\mathbb{B}$
- Selektiert einen der $n$ Dateneingänge $A_0,\dots,A_{n-1}$ als Ausgang $Y$
- $k=\lceil log_2\:n\rceil$ Steuersignale $S_0,\dots,S_{k-1}$
- $Y=A_{u_{2,k}(S_{k-1\dots S_0})}$
### MUX2
![[Pasted image 20250211151914.png]]
Wenn $S_0=0$ ist, dann ist $Y=A_0$ und wenn $S_0=1$ ist, ist $Y=A_1$.
Erklärung der Logik unten rechts: Wenn $S_0=0$ ist, kommt beim oberen [[Logikgatter#AND|AND]] eine $1$ an, wodurch sozusagen alles von $A_0$ durchgelassen wird, während alles bei dem unteren AND von der $0$ überschrieben wird. Genau so aber anders herum bei $S_0=1$. Das [[Logikgatter#OR|OR]] Gatter kombiniert und reduziert die Ausgänge der AND Gatter auf ein Ausgang $Y$.
### MUX4
MUX4: $\mathbb{B}^6\rightarrow\mathbb{B}$
![[Pasted image 20250211152646.png]]
## Logikrealisierung mit Multiplexern
- Variablen als Steuersignale verwenden
- Wahrheitswertetabelle als Konstanten an Dateneingängen
- entspricht adressiertem Speicherzugriff
	- Look-up Tabelle
	- ROM oder RAM $\rightarrow$ rekonfigurierbare Logik
- Beliebige Funktion mit $N$ Variablen kann sogar via MUX2$^{N-1}$ realisiert werden
![[Screenshot 2025-02-11 152941_inverted.png]]
## Dekodierer
DECODE$n:\mathbb{B}^n\rightarrow\mathbb{B}^{2^n}$
- $n$ Eingängen $A_0,\dots,A_{n-1}$
- $2^n$ Ausgänge $Y_0,\dots,Y_{2^{n}-1}$
- "One-Hot" Kodierung: $Y_i=u_{2,n}(A_{n-1}\dots A_0)==i\:?\:1\::\:0$
![[Pasted image 20250211153541.png]]
## Implementierung von Dekodierern
![[Pasted image 20250211154038.png]]
## Logikrealisierung mit Decodern
- Summe über [[Boole'sche Gleichungen#Minterm|Minterme]], auf denen Zielfunktion wahr ist
	$\Rightarrow$ Decoder ersetzt erste Stufe der zweistufigen Logikrealisierung
![[Pasted image 20250211154219.png]]
