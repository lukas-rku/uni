---
title: Basiswechsel
description: Lernzettel - Mathematik 1
draft: false
date: 2025-01-29
tags:
  - missingImage
---
[3Blue1Brown](https://www.youtube.com/watch?v=P2LTAUO1TdA)
## Definition 
Der Nullpunkt ist immer identisch allerdings kann man Koordinaten unterschiedlich definieren. Das übliche Koordinatensystem ist:
![[Pasted image 20250114125508.png#medium]]
mit $\begin{pmatrix}3\\2\end{pmatrix}=3\cdot\begin{pmatrix}1\\0\end{pmatrix}+2\cdot\begin{pmatrix}0\\1\end{pmatrix}$. 

---
In diesem Fall werden $\begin{pmatrix}1\\0\end{pmatrix}$ und $\begin{pmatrix}0\\1\end{pmatrix}$ Basisvektoren des Koordinatensystems genannt. Allerdings kann man diese für alles mögliche nehmen wie zum Beispiel $\vec b_1 = \begin{pmatrix}2\\1\end{pmatrix}$ und $\vec b_2 = \begin{pmatrix}-1\\1\end{pmatrix}$:
![[Pasted image 20250114130305.png#medium]]

---
## Übersetzen von Basiswechsel zur Standardbasis
Um nun bspw. den Vektor $\begin{pmatrix}-1\\2\end{pmatrix}'$ in "unser" Koordinatensystem zu übersetzen, ersetzt man unsere Basisvektoren mit $\vec b_1$ und $\vec b_2$:
$$-1 \cdot \vec b_1 + 2 \cdot \vec b_2 = -1 \cdot \begin{pmatrix}2\\1\end{pmatrix} + 2\cdot \begin{pmatrix}-1\\1\end{pmatrix} = \begin{pmatrix}-4\\1\end{pmatrix}$$
![[Pasted image 20250114131216.png#medium]]
Im Endeffekt ist das Übersetzen eine einfache [[Lineare Abbildungen|lineare Abbildung]]:
$$-1 \cdot \begin{pmatrix}2\\1\end{pmatrix} + 2\cdot \begin{pmatrix}-1\\1\end{pmatrix} = \begin{bmatrix}2&-1\\1&1\end{bmatrix}\cdot\begin{pmatrix}-1\\2\end{pmatrix}'= \begin{pmatrix}-4\\1\end{pmatrix}$$

---
## Übersetzung von Standardbasis zu Basiswechsel
Das [[Invertierbare Matrizen|Inverse]] der [[Lineare Abbildungen|linearen Abbildung]] des Basiswechsels wird benötigt:
$$\begin{bmatrix}2&-1\\1&1\end{bmatrix}^{-1} = \begin{bmatrix}1/3&1/3\\-1/3&2/3\end{bmatrix}$$
Um beispielsweise den Vektor $\begin{pmatrix}3\\2\end{pmatrix}$ zu übersetzen multipliziert man ihn damit:
$$\begin{bmatrix}1/3&1/3\\-1/3&2/3\end{bmatrix}\cdot\begin{pmatrix}3\\2\end{pmatrix}=\begin{pmatrix}5/3\\1/3\end{pmatrix}'$$

---
## Übersetzung von linearen Abbildungen in andere Basiswechsel
Die [[Lineare Abbildungen|lineare Abbildung]] des Basiswechsels: $A = \begin{bmatrix}2&-1\\1&1\end{bmatrix}$
Die [[Lineare Abbildungen|lineare Abbildung]] der Standardbasis: $M = \begin{bmatrix}0&-1\\1&0\end{bmatrix}$
Das [[Invertierbare Matrizen|Inverse]] des Basiswechsels: $A^{-1} = \begin{bmatrix}2&-1\\1&1\end{bmatrix}^{-1}$
$$M' = A^{-1} \cdot M \cdot A \cdot = \begin{bmatrix}2&-1\\1&1\end{bmatrix}^{-1}\cdot\begin{bmatrix}0&-1\\1&0\end{bmatrix}\cdot\begin{bmatrix}2&-1\\1&1\end{bmatrix}$$
