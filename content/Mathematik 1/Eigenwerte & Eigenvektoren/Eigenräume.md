# Eigenräume
## Definition
Ein **Eigenraum** eines linearen Operators $A$ ist der zu einem Eigenwert $\lambda$ gehörige Unterraum, der aus allen [[Eigenwerte & Eigenvektoren#Definition Eigenvektor|Eigenvektoren]] $\mathbf{v}$ sowie dem Nullvektor besteht. Formal gilt:

$$
E_\lambda = \{ \mathbf{v} \in \mathbb{R}^n \mid A \mathbf{v} = \lambda \mathbf{v} \}.
$$

Dabei ist $E_\lambda$ der Eigenraum zu $\lambda$, und $\lambda$ ist ein [[Eigenwerte & Eigenvektoren#Definition Eigenwerte|Eigenwert]] von $A$.

### Eigenschaften:
- Jeder Eigenraum $E_\lambda$ ist ein [[Untervektorräume#Definition|Untervektorraum]] von $\mathbb{R}^n$.
- Der Eigenraum zu einem Eigenwert $\lambda$ besteht aus den Lösungen des homogenen LGS:

$$
(A - \lambda I) \mathbf{v} = \mathbf{0}.
$$
### Beispiel

Gegeben sei die Matrix $A$:

$$
A = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}.
$$

#### 1. Bestimmung der Eigenwerte:
Die Eigenwerte von $A$ sind die Lösungen der **charakteristischen Gleichung**:
$$
\det(A - \lambda I) = 0.
$$
Mit 
$$
A - \lambda I = \begin{pmatrix} 2 - \lambda & 0 \\ 0 & 3 - \lambda \end{pmatrix}
$$ 
ergibt sich:
$$
\det(A - \lambda I) = (2 - \lambda)(3 - \lambda).
$$
Die Eigenwerte sind daher $\lambda_1 = 2$ und $\lambda_2 = 3$.

#### 2. Berechnung der Eigenräume:

Für $\lambda_1 = 2$:
$$
(A - 2I) = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}.
$$
Das homogene LGS $(A - 2I)\mathbf{v} = \mathbf{0}$ ergibt den Eigenraum:
$$
E_2 = \text{Span} \left( \begin{pmatrix} 1 \\ 0 \end{pmatrix} \right).
$$

Für $\lambda_2 = 3$:
$$
(A - 3I) = \begin{pmatrix} -1 & 0 \\ 0 & 0 \end{pmatrix}.
$$
Das homogene LGS $(A - 3I)\mathbf{v} = \mathbf{0}$ ergibt den Eigenraum:
$$
E_3 = \text{Span} \left( \begin{pmatrix} 0 \\ 1 \end{pmatrix} \right).
$$

#### 3. Ergebnis:
Die Eigenräume sind:
$$
E_2 = \text{Span} \left( \begin{pmatrix} 1 \\ 0 \end{pmatrix} \right), \quad 
E_3 = \text{Span} \left( \begin{pmatrix} 0 \\ 1 \end{pmatrix} \right).
$$
