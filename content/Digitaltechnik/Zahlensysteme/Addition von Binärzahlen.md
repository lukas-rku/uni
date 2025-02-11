---
title: Addition von Binärzahlen
description: Lernzettel - Digitaltechnik
draft: false
date: 2025-02-09
tags:
---
## Schriftliche Addition von [[Zahlensysteme#Definition vorzeichenloses Stellenwertsystem|vorzeichenlosen Binärzahlen]]
$$
\begin{align*}
&\text{Summand: }&1011\\
&\text{Summand: }&+0011\\
&\text{Übertrag: }&0110\\
&&\text{-------}\\
&\text{Summe: }&=1110
\end{align*}
$$
## Addition mit Überlauf
- Digitale Systeme arbeiten i.d.R. mit festen Bitbreiten
	- Langzahlaritmehtik nur in Software (Bitbreite nur durch verfügbaren Arbeitsspeicher beschränkt)
	- Overflow-flag zum Signalisieren arithmetischer Ausnahmen in Hardware
- Operation (bspw. Addition) läuft über, wenn Ergebnis nicht mit der verfügbaren Bitbreite dargestellt werden kann
- für 4 bit Addiere gilt zum Beispiel: $11+6=1$, da $10001=0001$

## Addition von [[Zahlensysteme|Zweierkomplement]]
Binärzahlen des Zweierkomplements sind kompatibel mit der [[#Schriftliche Addition von Zahlensysteme Definition vorzeichenloses Stellenwertsystem vorzeichenlosen Binärzahlen|schriftlichen Addition]]:
$$
\begin{align*}
&\text{Summand: }&1010 &= -6_{10}\\
&\text{Summand: }&+0110&=+6_{10}\\
&\text{Übertrag: }&1\:1100\\
&&\text{-------}\\
&\text{Summe: }&=1\:0000\\
&&=0000\\
&&=0_{10}
\end{align*}
$$
Hier erfreut man sich tatsächlich über den [[#Addition mit Überlauf|Überlauf]]. Wichtig ist allerdings, dass beide Zahlen die gleich Breite benötigen.