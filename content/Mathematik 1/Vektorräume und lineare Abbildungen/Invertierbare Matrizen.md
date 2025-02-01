---
title: Invertierbare Matrizen
description:
draft: false
date: 2025-01-25
tags:
---
### Definition
Wenn man eine Matrix $A$ mit der Inversen von sich selbst multipliziert so entsteht die Einheitsmatrix:
$$
A^{-1}A=\begin{bmatrix}1&0\\0&1\end{bmatrix}
$$
Wenn man beispielsweise den Vektor $\vec x$ sucht der mit der Matrix $A$ multipliziert den Vektor $\vec v$ ergibt, so kann man die Inverse von  $A$ nutzen:
$$
\begin{align*}
A\vec x&=\vec v\\
A^{-1}A\vec x&=A^{-1}\vec v\\
\vec x&=A^{-1}\vec v
\end{align*}
$$
### Bedingung
Die [[Determinante#Definition|Determinante]] von $A$ darf nicht null sein, da die [[Lineare Abbildungen#Definition|lineare Abbildung]] sonst den [[Bild, Urbild und Kern einer linearen Abbildung#Definition Bild|Bildraum]] verändert:
$$
\text{det}(A)\not=0
$$
Allerdings kann man in manchen Fällen trotzdem den Vektor $\vec x$ berechnen, solange $\vec v$ im durch die Matrix $A$ geänderten Bildraum liegt.
