---
title: Logikgatter
description: Lernzettel - Digitaltechnik
draft: false
date: 2025-02-09
tags:
---
## Logische Operationen
- verknüpfen binäre Werte: $\mathbb{B}^n\rightarrow\mathbb{B}^k$
- zunächst $k=1$
- Beispiele für
	- n = 1: NOT
	- n = 2: AND, OR, XOR
	- n = 3: MUX
- Charakterisierung durch Wahrheitstabellen

## Logikgatter: Übersicht
### BUF
$\mathbb{B} \rightarrow \mathbb{B}$
![[../../assets/buf_inverted.png]]
### NOT
$\mathbb{B} \rightarrow \mathbb{B}$
![[../../assets/not_inverted.png]]
### AND
$\mathbb{B}^2 \rightarrow \mathbb{B}$
![[../../assets/and_inverted.png]]
### OR
$\mathbb{B}^2 \rightarrow \mathbb{B}$
![[../../assets/or_inverted.png]]
### XOR
$\mathbb{B}^2 \rightarrow \mathbb{B}$
![[../../assets/xor_inverted.png]]
### NAND
$\mathbb{B}^2 \rightarrow \mathbb{B}$
![[../../assets/nand_inverted.png]]
### NOR
$\mathbb{B}^2 \rightarrow \mathbb{B}$
![[../../assets/nor_inverted.png]]
### XNOR
$\mathbb{B}^2 \rightarrow \mathbb{B}$
![[../../assets/xnor_inverted.png]]
### XOR3
$\mathbb{B}^3 \rightarrow \mathbb{B}$
![[../../assets/xor3_inverted.png]]
### XOR mit mehreren Eingängen
- "repräsentiert" die Anzahl der Einsen an Eingängen (modulo 2)
- Paritätsfunktion $p:(a_{k-1},...,a_0)\in\mathbb{B}^k\mapsto a_{k-1}\oplus,...,\oplus a_0\in\mathbb{B}$
	- $p(a)=0\rightarrow$ Quersumme von $a$ ist gerade
	- $p(a)=1\rightarrow$ Quersumme von $a$ ist ungerade
