# Lineare Unabhängigkeit, Erzeugungssysteme und Basen
## Lineare Unabhängigkeit & Erzeugungssysteme
Ein Vektor ist linear unabhängig von einem anderen, wenn er **kein Vielfaches von ihm** ist.  
Beispiele:
$$
\begin{align*}
\text{Linear abhängig: } & \left\{\begin{pmatrix}1\\0\end{pmatrix}, \begin{pmatrix}2\\0\end{pmatrix}\right\}, \quad \text{da } \begin{pmatrix}2\\0\end{pmatrix} = 2 \cdot \begin{pmatrix}1\\0\end{pmatrix}. \\
\text{Linear unabhängig: } & \left\{\begin{pmatrix}1\\0\end{pmatrix}, \begin{pmatrix}2\\1\end{pmatrix}\right\}, \quad \text{da keiner ein Vielfaches des anderen ist.}
\end{align*}
$$

Eine Basis ist eine Menge von **linear unabhängigen Vektoren**, die den gesamten Vektorraum aufspannen. Das bedeutet, dass jeder Vektor im Vektorraum als Linearkombination der Basisvektoren dargestellt werden kann. Eine Basis ist gleichzeitig ein **Erzeugendensystem**. Die Anzahl der Vektoren in einer Basis ist die **Dimension** $\text{dim}()$ des Vektorraumes.

Beispiel:
$$
\begin{align*}
\text{Vektorraum: } & \mathbb{R}^2 \\
\text{Linear unabhängige Basisvektoren: } & \left\{\begin{pmatrix}1\\0\end{pmatrix}, \begin{pmatrix}0\\1\end{pmatrix}\right\}.
\end{align*}
$$

Jeder Vektor im $\mathbb{R}^2$, z. B. $\begin{pmatrix}20\\40\end{pmatrix}$, kann als Linearkombination der Basisvektoren dargestellt werden:
$$
\begin{pmatrix}1\\0\end{pmatrix} \cdot 20 + \begin{pmatrix}0\\1\end{pmatrix} \cdot 40 = \begin{pmatrix}20\\40\end{pmatrix}.
$$
---
## Basen
Eine Basis ist ein **Erzeugungssystem**, jedoch muss die Darstellung eindeutig bzw. **linear unabhängig** sein. Ein Beispiel dafür sind zum Beispiel die drei Einheitsvektoren $$\lbrace\begin{pmatrix}1\\0\\0\end{pmatrix},\begin{pmatrix}0\\1\\0\end{pmatrix}\begin{pmatrix}0\\0\\1\end{pmatrix}\rbrace$$ für die Menge $\mathbb{R}^3$, da sich alle Vektoren aus diesen erzeugen lassen. Meistens besitzt ein Vektorraum mehrere Basen.

---
## Prüfung auf Basis
$$\begin{gather*}
B=\left\lbrace
\begin{pmatrix}1\\0\\2\end{pmatrix},
\begin{pmatrix}3\\2\\1\end{pmatrix},
\begin{pmatrix}1\\1\\1\end{pmatrix}
\right\rbrace\\
\begin{pmatrix}x\\y\\z\end{pmatrix} = 
\lambda_1\cdot\begin{pmatrix}1\\0\\2\end{pmatrix}+
\lambda_2\cdot\begin{pmatrix}3\\2\\1\end{pmatrix}+
\lambda_3\cdot\begin{pmatrix}1\\1\\1\end{pmatrix}\\
\begin{vmatrix}1\cdot\lambda_1+3\cdot\lambda_2+1\cdot\lambda_3=x\\
0\cdot\lambda_1+2\cdot\lambda_2+1\cdot\lambda_3=y\\
2\cdot\lambda_1+1\cdot\lambda_2+1\cdot\lambda_3=z\end{vmatrix}\\
\mathbb{L}=\left\lbrace\frac{x-2y+z}{2},\frac{2x-y-z}{3},\frac{-4x+5y+2z}{3}\right\rbrace
\end{gather*}
$$

Da das Gleichungssystem eine eindeutige Lösung (lösbar & keine Parameter) hat, ist $B$ eine **Basis**.