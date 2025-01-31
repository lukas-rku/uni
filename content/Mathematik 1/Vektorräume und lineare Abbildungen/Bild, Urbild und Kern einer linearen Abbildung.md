# Bild, Urbild und Kern einer linearen Abbildung
## Definition Bild
- Das Bild ist eine Menge.
- $\text{im}(f) = f(V) := \lbrace f(x) \mid x \in V \rbrace$
- $\text{im}(f) \subseteq W$
![[Pasted image 20250112123615.png]]

**Beispiele:**
1. Für $f: \mathbb{R} \to \mathbb{R}$, $f(x) = x^2$ ist $\text{im}(f) = [0, \infty)$.
2. Für $f: \mathbb{R}^2 \to \mathbb{R}$, $f(x, y) = x + y$ ist $\text{im}(f) = \mathbb{R}$.
## Definition Urbild
- $f^{-1}(N) = \lbrace x \in V \mid f(x) \in N \rbrace$
![[Pasted image 20250112123624.png]]

**Beispiele:**
1. Für $f: \mathbb{R} \to \mathbb{R}$, $f(x) = x^2$ und $N = \lbrace 4 \rbrace$, ist $f^{-1}(N) = \lbrace -2, 2 \rbrace$.
2. Für $f: \mathbb{R} \to \mathbb{R}$, $f(x) = x^3$ und $N = \lbrace 8 \rbrace$, ist $f^{-1}(N) = \lbrace 2 \rbrace$.
## Sonderfälle Urbild
- Das Urbild von der Bildmenge ist die gesamte Definitionsmenge:
  - $f^{-1}(\text{im}(f)) = V$
  - Beispiel: Für $f: \mathbb{R} \to \mathbb{R}$, $f(x) = x^2$, ist $f^{-1}([0, \infty)) = \mathbb{R}$.
![[Pasted image 20250112123636.png]]
- Das Urbild eines Elementes wird auch **Faser der Abbildung** über dem Element genannt.
- Wenn ein Wert in der Zielmenge von mehreren Elementen getroffen wird, hat das Urbild auch mehrere Elemente.
  - Beispiel: Für $f: \mathbb{R} \to \mathbb{R}$, $f(x) = \sin(x)$ und $N = \lbrace 0 \rbrace$, ist $f^{-1}(N) = \lbrace 0, \pi, -\pi, 2\pi, -2\pi, \dots \rbrace$.
![[Pasted image 20250112123651.png]]
## Definition Kern
- Alle Elemente aus der Definitionsmenge, für die der Funktionswert der Nullvektor ist.
- $\text{ker}(f)=\left\lbrace x\in V\mid f\left(x\right)=0\in W\right\rbrace$
## Bestimmen des Kerns
- Abbildungsmatrix mit dem Nullvektor gleichsetzen und Gleichungssystem aufstellen:
$$\begin{align*}
A&=\vec v_0\\
\begin{pmatrix}0 & 4 & -4\\1 & 1 & 0\\5 & 7 & -2\end{pmatrix}&=\begin{pmatrix}0\\0\\0\end{pmatrix}\\
\end{align*}
$$
$$
\begin{align*}
0x_1+1x_2-4x_3&=0\\
1x_1+1x_2+0x_3&=0\\
5x_1+7x_2-2x&=0\\
\end{align*}
$$
$$
\mathbb{L}=\lbrace x=0\mid y=0\mid z=0\rbrace
$$
- Das heißt das der Kern von $A = 0$ ist.