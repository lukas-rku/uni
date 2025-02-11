---
title: Rekursion in Java
description: Lernzettel - funktionale und objektorientierte Programmierung
draft: false
date: 2025-02-08
tags:
---
## Illustrative Klassenmethode
```java
// Precondition: n >= 0
public static void m(int n) {
	System.out.prinzln(n);
	if(n > 0) {
		m(n - 1);
	}
	System.out.println(n)
}
```
Die Methode `m` demonstriert, wie Rekursion funktioniert:
- Zunächst wird der aktuelle Parameter `n` ausgegeben.
- Ist `n` größer als 0, ruft sich die Methode selbst mit `n - 1` auf.
- Nach dem rekursiven Aufruf wird `n` erneut ausgegeben.

Wird `m(3)` aufgerufen, so erfolgt folgende Abfolge:
1. Ausgabe von 3, dann Aufruf von `m(2)`.
2. Ausgabe von 2, dann Aufruf von `m(1)`.
3. Ausgabe von 1, dann Aufruf von `m(0)`.
4. Bei `n = 0` wird nur 0 ausgegeben (Rekursion endet).
5. Danach gibt jeder Rücksprung den jeweiligen Parameterwert erneut aus: zuerst 0, dann 1, anschließend 2 und schließlich 3.

So entsteht die Ausgabereihenfolge: `3, 2, 1, 0, 0, 1, 2, 3.`
![[../../../assets/2_inv.png]]
Der Blick auf den Call-Stack zeigt, was dahintersteckt: In jedem Frame, am selben Offset von der Startadresse des jeweiligen Frames, ist ein Platz für den Parameter `n` reserviert. Der ist bei jedem rekursiven Aufruf ein anderer, nämlich immer um `1` kleiner. In jeder
Bildschirmausgabe wird immer der Wert von `n` im obersten Frame genommen, also in dem Frame, auf dessen Anfangsadresse der Stack-Pointer momentan verweist.
## Rekursive Berechnung des Binomialkoeffizienten in Java
Die rekursive Formel für den Binomialkoeffizienten $\binom{n}{k}$ lautet:

$$
\binom{n}{k} = \begin{cases} 1, & \text{falls } k = 0 \text{ oder } k = n \quad (\text{Rekursionsanker}) \\ \binom{n-1}{k-1} + \binom{n-1}{k}, & \text{sonst \quad (rekursiver Aufruf)} \end{cases}
$$
```java
public static long binom(int n, int k) {
	// Rekursionsanker (Basisfälle):
	// Falls k gleich 0 oder k gleich n ist, gibt es genau eine Möglichkeit, zu wählen.
	if (k == 0 || k == n) {
		return 1;
	}
	
	// Rekursionsschritt:
	// Zerlege das Problem in zwei Teilprobleme:
	// 1. Wähle ein Element aus (damit k um 1 reduziert wird) und berechne den Koeffizienten für (n-1, k-1).
	// 2. Oder ignoriere dieses Element und berechne den Koeffizienten für (n-1, k).
	return binom(n - 1, k - 1) + binom(n - 1, k);
}
```

**Rekursionsanker (Basisfälle):**  
Der **Rekursionsanker** tritt auf, wenn $k = 0$ oder $k = n$ ist. In diesen Fällen gibt es genau eine Möglichkeit, Elemente auszuwählen, weshalb die Methode direkt den Wert `1` zurückgibt. Dadurch wird verhindert, dass die Rekursion unendlich fortgesetzt wird.

**Rekursive Aufrufe (Rekursionsschritte):**  
Falls keiner der Basisfälle eintritt, wird die Berechnung in zwei rekursive Aufrufe zerlegt:
- **Erster rekursiver Aufruf:**  
	`binom(n - 1, k - 1)` 
	Hier wird ein Element ausgewählt, sodass sich die Anzahl der noch auszuwählenden Elemente um 1 verringert.

- **Zweiter rekursiver Aufruf:**  
	`binom(n - 1, k)`
	Hier wird das betrachtete Element nicht ausgewählt, sodass kk unverändert bleibt.

Die Summe dieser beiden Aufrufe entspricht der rekursiven Definition:
$$
\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}
$$
**Rekursionsbaum:**  
Jeder rekursive Aufruf entspricht einem Knoten in einem **Rekursionsbaum**. Das ursprüngliche Problem wird in kleinere Teilprobleme zerlegt, bis die Basisfälle erreicht werden. Die hierarchische Struktur des Aufrufbaums veranschaulicht, wie das Gesamtproblem schrittweise abgebaut wird.