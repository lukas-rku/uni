---
title: Eigenwerte & Eigenvektoren
description: Lernzettel - Mathematik 1
draft: false
date: 2025-01-24
tags:
  - missingImage
---
[3Blue1Brown](https://www.youtube.com/watch?v=PFDu9oVAE-g)
### Definition Eigenvektor
Ein Eigenvektor ist ein Vektor zugehörig zu einer [[Lineare Abbildungen#Definition|lineare Abbildung]], welcher nicht von seinem [[Spann#Definition|Spann]] "geworfen" wird. Das heißt, dass er lediglich gestaucht oder gestreckt wird, wenn eine Abbildung auf ihm angewendet wird. Nicht jede Abbildung muss Eigenvektoren haben.
### Definition Eigenwerte
Ein Eigenwert wird einem Eigenvektor zugeordnet. Er besagt, wie stark der Eigenvektor gestaucht oder gestreckt wird durch die [[Lineare Abbildungen#Definition|lineare Abbildung]]. Ist der Eigenwert negativ, so wird der Eigenwert in gegengesetzte Richtung gestaucht / gestreckt.
### Beispiel Eigenvektor & Eigenwert
$$
\begin{gather*}
A = \begin{bmatrix}3&1\\0&2\end{bmatrix}\\
\text{Eigenvektoren: } v_1=\begin{pmatrix}3\\0\end{pmatrix},v_2=\begin{pmatrix}-1\\1\end{pmatrix}\\
\text{Eigenwerte: } \lambda_1=3, \lambda_2=2
\end{gather*}
$$
![[Pasted image 20250120162648.png]]
### Berechnung von Eigenvektoren & Eigenwerten
Da der Eigenvektor $e$ mit der Matrix $A$ multipliziert das gleiche ergibt wie die Multiplikation von $e$ mit dem Eigenwert $\lambda$ versucht man einen Wert für $\lambda$ zu finden, bei dem die [[Determinante#Definition|Determinante]] der Gleichung $0$ ist.
$$
\begin{gather*}
\text{lineare Abbildung } A\\
\text{Eigenvektor } e\\
\text{Eigenwert } \lambda \\ \\
A \cdot e = (\lambda I) \cdot e\\
(A-\lambda I)e=0\\
\text{det}(A-\lambda I)=0
\end{gather*}
$$