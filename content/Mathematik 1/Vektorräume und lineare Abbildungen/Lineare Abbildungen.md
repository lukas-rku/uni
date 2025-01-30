# Lineare Abbildungen
### Definition
Zuordnung $f: \mathbb{R}^n\rightarrow\mathbb{R}^m$
- Jedem Punkt $P$ von $\mathbb{R}^n$ wird $P'$ von $\mathbb{R}^m$ zugeordnet
- Es gibt $m\times n$ - Matrix $A$ (**Abbildungsmatrix**), sodass für Ortsvektoren $\vec x$ von $P$ und $\vec x '$ von $P'$ gilt: $A\times \vec x = \vec x'$ 
### Beispiel
Spiegelung des Punktes $P$ an der $x$ - Achse:
$$
\begin{align*}
P&=(x\mid y)\\
P'&=(x'\mid y')=(x\mid -y)\\
\vec x'&= \begin{pmatrix}x'\\y'\end{pmatrix} = \begin{pmatrix}x&\\&-y\end{pmatrix}= \begin{pmatrix}1&0\\0&-1\end{pmatrix}\cdot\begin{pmatrix}x\\y\end{pmatrix}\\
 A &=\begin{pmatrix}1&0\\0&-1\end{pmatrix}\text{ (Abbildungsmatrix)}
\end{align*}$$
"Eine lineare Abbildung liegt vor."
### Anmerkung
Ein Vektor könnte auch von bspw. $\mathbb{R}^2\rightarrow\mathbb{R}^3$ abgebildet werden wodurch eine $2\times 3$ - Matrix entstehen würde.