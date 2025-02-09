---
title: Bitbreitenerweiterung
description: Lernzettel - Digitaltechnik
draft: false
date: 2025-02-09
tags:
---
## Zero Extension und Sign Extension
- notwendig, um unterschiedliche Bitfolgen zu addieren
- *zero extension:*
	- Auffüllen mit führenden Nullen für [[Zahlensysteme#Definition vorzeichenloses Stellenwertsystem|vorzeichenlose]] Darstellung
$$
u_{2,k+1}(0a_{k-1},...,a_0)=0\cdot2^k+\sum^{k-1}_{i=0}a_i\cdot2^i=u_{2,k}(a_{k-1},...,a_0)
$$
	- Beispiel: von 2 bit zu 10 bit: $11_2=00\:0000\:0011_2$

- *sign extension:*
	- Auffüllen mit Wert des Vorzeichen-Bits für [[Zahlensysteme#Definition Zweierkomplement|Zweierkomplement]] Darstellung
$$
\begin{align*}
s_{k+1}(a_{k-1}a_{k-1},...,a_0)&=a_{k-1}\cdot(-2^k)+a_{k-1}\cdot2^{k-1}+\sum^{k-2}_{i=0}a_i\cdot2^i\\
&=a_{k-1}\cdot(-2^{k-1}-2^{k-1}+2^{k-1})+\sum^{k-2}_{i=0}a_i\cdot2^i\\
&=s_k(a_{k-1},...,a_0)
\end{align*}
$$
	- $00\:0000\:0100_2\not=100_2$ im Zweierkomplement
	- $11\:1111\:1100_2=100_2$
	- Immer das dran hängen, was das MSB ist.