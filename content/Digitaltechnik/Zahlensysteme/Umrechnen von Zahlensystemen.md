---
title: Umrechnen von Zahlensystemen
description: Lernzettel - Digitaltechnik
draft: false
date: 2025-02-09
tags:
---
## Binär/Hexadezimal -> Dezimal
polyadische Abbildung anwenden:
- Basis 2, 5 Stellen:
$$
\begin{align*}
u_{2,5}(10011_2)&= 1 \cdot 2^ 0 + 1 \cdot 2 ^ 1 + 0 \cdot 2 ^ 2 + 0 \cdot 2^ 3 + 1 \cdot 2 ^ 4 + 1 \cdot 2 ^ 5 \\&= 1 + 2 + 16 \\&= 19_{10}
\end{align*}
$$

- Basis 16, 3 Stellen:
$$
\begin{align*}
u_{16,3}(\text{4AF}_{16})&=15 \cdot 16 ^ 0 + 10 \cdot 16 ^ 1 + 4 \cdot 16 ^ 2 15 + 160 + 4\cdot(2^4)^4\\&=15+16+4\cdot 2 ^ 8\\&=15+160+1024\\&=1199_{10}
\end{align*}
$$

## Binär $\leftrightarrow$ Hexadezimal
- Nibble-weise umwandeln
- bei least significant bit beginnen
- führende Nullen weglassen oder ergänzen (je nach geforderter Bitbreite)
$$
\begin{align*}
11\:1010\:0110\:1000_2&=0011\:1010\:0110\:1000_2\\
&=(2_8+1_8=3_{16})( 8_8 +2_8=A_{16})(4_8+2_8=6_{16})(8_8=8_{16})\\
&=\text{3A68}_{16}
\end{align*}
$$
*Jeder Nibble (alle 4 Bits) wird einzeln betracht und zu hexadezimal umgerechnet.*
$$
\text{7BF}_{16}=111\:1011\:1111_2
$$
## Dezimal $\rightarrow$ Binär
- Methode 1 (links nach rechts): maximale Zweierpotenzen abziehen
$$
\begin{align*}
53_{10}&=32+21\\
&=32+16+5\\
&=32+16+4+1\\
&=2^5=2^4+2^2+2^0\\
&=11\:0101_2
\end{align*}
$$
- Methode 2 (rechts nach links): Halbieren mit Rest (sukzessives Durch-2-Teilen)
$$
\begin{align*}
53_{10}\mod2 &=1\\
26_{10}\mod2 &= 0\\
13_{10}\mod2 &= 1\\
6_{10}\mod2 &= 0\\
3_{10}\mod2 & =1 \\
1_{10}\mod2 &=1\\
\end{align*}
$$
*Von unten nach oben ist Methode 2 = Methode 1. Der Rest von $1:2$ ist $1$.*
![[../../assets/Screenshot 2025-02-09 144628_inverted.png]]
*Von dezimal zu hexadezimal ist der Weg über binär am besten.*

## Binärdarstellung im [[Zahlensysteme#Definition Zweierkomplement|Zweierkomplement]]
$$
\begin{align*}
s_4(1010_2)&=0\cdot2^0+1\cdot2^1+0\cdot2^2+1\cdot(-2^3)\\
&=-6_{10}
\end{align*}
$$
$$
\begin{align*}
s_4(0110_2)&=0\cdot2^0+1\cdot2^1+1\cdot2^2+0\cdot(-2^3)\\
&=6_{10}
\end{align*}
$$
- $s_4$ steht für Zweierkomplement mit 4 bits. Das ist wichtig zu definieren, da man sonst nicht weiß ob die Zahl vorzeichenbehaftet oder nicht ist.
- Man kann nicht direkt sehen, ob eine Zahl das direkte negativ/positiv einer Zahl ist.
- Allerdings kann man anhand der ersten Stelle sehen ob die Zahl negativ oder positiv ist.

## Dezimal $\rightarrow$ Zweierkomplement
- Methode 1 (links nach rechts): maximale Zweierpotenzen abziehen
$$
\begin{align*}
-53_{10}&=-64+11\\
&=-64+8+3\\
&=-64+8+2+1\\
&=1\cdot(-2^6)+1\cdot2^3+1\cdot2^1+1\cdot2^0\\
&=100\:1011_2
\end{align*}
$$
- Methode 2 (rechts nach links): Betrag negieren = Komplement (bitweise $\overline{a}$) und Inkrement ($+1$), Reihenfolge beachten!
$$
\begin{align*}
-&53_{10}\\
&\text{--------}\\
\text{Positiv als binärzahl: }&53& =32+16+4+1\\
\text{null vorne Anhängen: }&53_{10}&=11\:0101_2  =011\:0101_2\\
&\text{--------}\\
\text{Negieren: }&\overline{53_{10}}&=100\:1010_2\\
&\text{--------}\\
\text{+1 Addieren: }&100\:1010_2+1&=100\:1011_2
\end{align*}
$$
- In beiden Fällen auf korrekte/geforderte Bitbreite achten
- ggf. müssen führende Null(en) schon für Betragsdarstellung eingefügt werden

## Zweierkomplement $\rightarrow$ Dezimal
- Methode 1: polyadische Abbildung direkt anwenden\
$$
100\:1011_2=2^0+2^1+2^3-2^6=1+2+8-64=-53_{10}
$$
- Methode 2 (bei MSB = 1): Betrag berechnen - Komplement und Inkrement
$$
\begin{align*}
&100\:1011_2\xrightarrow{\text{inv}}011\:0100\xrightarrow{\text{+1}}011\:0101\\&=2^0+2^2+2^4+2^5=1+4+16+32\\&=53\xrightarrow{\text{inv}}-53
\end{align*}
$$
*$\text{inv}$ = invertiert.*
- Methode 2 (bei MSB = 0)
$$
000\:1011_2=2^0+2^1+2^3=11_{10}
$$
