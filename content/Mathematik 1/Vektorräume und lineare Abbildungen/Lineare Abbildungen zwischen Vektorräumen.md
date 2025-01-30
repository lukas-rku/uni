# Lineare Abbildungen zwischen Vektorräume
### Definition
- Sei Vektorraum $(V,\oplus, \odot)$ und $(W,\oplus, \odot)$
- Es muss gelten:
	1. Homogenität: $f(a\cdot \vec v) = a \cdot f(\vec v)$ 
	2. Additivität: $f(\vec w + \vec v) = f(\vec w )+ f(\vec v)$ 

### Test auf Linearität
$a \cdot \vec v + \vec w$ in die Abbildung einsetzen:
$f(a\cdot \vec v + \vec w)= a \cdot f(\vec v ) + f(\vec w)$

### Beispiel:
Streckung in $x$ - Richtung um 2 und $y$ - Richtung um 3 in $f: \mathbb{R}^2\rightarrow\mathbb{R}^2$
$$f\begin{pmatrix}x\\y\end{pmatrix}=\begin{pmatrix}2x\\3y\end{pmatrix}=\begin{pmatrix}2&0\\0&3\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}$$
