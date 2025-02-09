---
title: Zahlensysteme
description: Lernzettel - Digitaltechnik
draft: false
date: 2025-02-09
tags:
---
## Definition: vorzeichenloses Stellenwertsystem
Für eine Basis $b\in\mathbb{N}\wedge b\ge2$ ist $Z_b:=\{0,1,...,b-1\}$ die Menge der verfügbaren Ziffern. Die Funktion $u_{b,k}$ bildet eine Ziffernfolge der Breite $k \in \mathbb{N}$ auf eine natürliche Zahl ab:
$$
u_{b,k}:(a_{k-1}...a_1a_0)\in Z^k_b\mapsto\sum^{k-1}_{i=0}a_i\cdot b^i\in\mathbb{N}
$$
Trick zu effizienteren Berechnung ohne Exponentiationen $b^i$: Horner Schema
$$
\sum^{k-1}_{i=0}a_i\cdot b^i=((...((a_{k-1}\cdot b+a_{k-2})\cdot b+a_{k-3})...)\cdot b + a_1)\cdot b + a_0
$$

- polyadisches Zahlensystem
- niedrigstwertige Stelle (LSD, least significant digit): $a_0$
- höchstwertige Stelle (MSD, most significant digit): $a_{k-1}$
- kleinste darstellbare Zahl: $\sum^{k-1}_{i=0}0\cdot b^i=0$
- größte darstellbare Zahl: $\sum^{k-1}_{i=0}(b-1)\cdot b^i=b^k-1$
- Anzahl der darstellbaren Werte: $|Z^k_b|=|Z_b|^k=b^k$
- eineindeutig (bijektiv) abbildbar auf Wertebereich $\{0,...,b^k-1\}$ für festes $k$

## Definition: Zweierkomplement
Die Funktion $s_k$ bildet eine Bitfolde der Breite $k\in\mathbb{N}$ auf eine ganze Zahl ab:
$$
s_k:(a_{k-1}...a_1a_0)\in\mathbb{B}^k\mapsto a_{k-1}\cdot (-2^{k-1})+\sum^{k-2}_{i=0}a_i\cdot2^i\in\mathbb{Z}
$$
- niedrigstwertige Stelle: $a_0$
- höchstwertige Stelle : $a_{k-1}$
- kleinste darstellbare Zahl: $1\cdot(-2^{k-1})+\sum^{k-2}_{i=0}0\cdot2^i=-2^{k-1}$
- größte darstellbare Zahl: $0\cdot(-2^{k-1})+\sum^{k-2}_{i=0}1\cdot2^i=2^{k-1}-1$
- Anzahl der darstellbaren Werte: $2^k$
- eineindeutig (bijektiv) abbildbar auf Wertebereich $\{-2^{k-1},...,2^{k-1}-1\}$