---
title: Spann
description:
draft: false
date: 2025-01-28
tags:
---
## Definition
- Der **Spann** ist ein [[Untervektorräume#Definition|Untervektorraum]] von $V$, der alle Linearkombinationen der gegebenen Vektoren enthält.
- **Notation:** $\text{span}(M)$ oder $\langle M \rangle_K$, wobei $M$ eine Teilmenge des Vektorraums $V$ ist, die aus Vektoren $v_1, v_2, \ldots, v_k$ besteht:  
  $\text{span}(\{v_1, \dots, v_k\})$

## Beispiel:
$$
M = \left\lbrace
\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, 
\begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, 
\begin{pmatrix} 2 \\ 2 \\ 0 \end{pmatrix} 
\right\rbrace
$$

Der Spann $\text{span}(M)$ umfasst alle Linearkombinationen der Vektoren in $M$.  
Das bedeutet:
$$
\text{span}(M) = \left\lbrace a \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} 
+ b \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} 
+ c \begin{pmatrix} 2 \\ 2 \\ 0 \end{pmatrix} 
\mid a, b, c \in \mathbb{R} \right\rbrace
$$

$$
a \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} 
+ b \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} 
+ c \begin{pmatrix} 2 \\ 2 \\ 0 \end{pmatrix} 
= \begin{pmatrix} a + 2c \\ b + 2c \\ 0 \end{pmatrix}
$$

Da die dritte Komponente immer $0$ ist, liegt der Spann in einer zweidimensionalen Ebene innerhalb von $\mathbb{R}^3$, genauer gesagt in der $xy$-Ebene.

## Überprüfung der Linearunabhängigkeit:
Die Vektoren 
$$
\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} 
\quad \text{und} \quad 
\begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}
$$
sind linear unabhängig, da keine Linearkombination der beiden einen der anderen darstellen kann.

Der Vektor 
$$
\begin{pmatrix} 2 \\ 2 \\ 0 \end{pmatrix}
$$
ist jedoch eine Linearkombination der beiden anderen Vektoren:
$$
\begin{pmatrix} 2 \\ 2 \\ 0 \end{pmatrix} = 2 \cdot \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} + 2 \cdot \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}.
$$

## Fazit:
Die Menge $M$ spannt den Unterraum $\mathbb{R}^2$ auf, der durch die Basisvektoren
$$
\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}
\quad \text{und} \quad
\begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}
$$
beschrieben wird. Es gilt:
$$
\text{span}(M) = \mathbb{R}^2 = \left\langle 
\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, 
\begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}
\right\rangle
$$
