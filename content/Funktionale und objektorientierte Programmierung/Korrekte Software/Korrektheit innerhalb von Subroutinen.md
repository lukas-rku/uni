---
title: Korrektheit innerhalb von Subroutinen
description: Lernzettel - funktionale und objektorientierte Programmierung
draft: false
date: 2025-02-06
tags:
---
## Korrektheit von Ausdrücken
Völlig analog zu [[Korrektheit von Subroutinen|Subroutinen mit Rückgabe]].
## Korrektheit bei Verzweigungen (`if`,`cond`,`switch`)
Genau dann, wenn jede Alternative korrekt ist.
## Korrektheit von Schleifen
Invariante (Schleifeninvariante)
- Die Schleifen-*in*-variante beinhaltet Aussagen darüber, was sich während der Schleife *nicht* ändert.
Variante (Schleifenvariante)
- Die Schleifenvariante beinhaltet Aussagen darüber, was sich in jedem Schleifendurchlauf ändert
## Beispiel: Summe im Array
```java
public static double sum(double[] a) {}
	double result = 0;
	for(int i = 0; i < a.length; i++) {
		result += a[i];
	}
	return result;
}
```
- Invariante: Nach $h \ge 0$ Schritten ist `result == a[0] + ... + a[h - 1]`
- Variante: `h` steigt um `1`
-> Nach Schleifenende ist `result == a[0] + ... + a[a.length - 1]`.
## Theoretische Einordnung
- Invariante = Induktionsbehauptung: "Nach $h \ge 0$ Schleifendurchläufen gilt..."
- Induktionsanfang, also $h=0$: Die Initialisierung vor der Schleife sorft dafür, dass die Invariante unmittelbar vor dem ersten Schleifendurchlauf erfüllt ist.
- Induktionsvoraussetzung für $h>0$: Die Invariante gelte für $h-1$ (also unmittelbar vor dem $h$-ten Durchlauf).
- Induktionsschritt: Unter der Voraussetzung, dass die Invariante nach $h-1$ Durchläufen gilt, sorgt der `Body` der Schleife dafür, dass die Invariante auch nach $h$ Durchläufen weiterhin gilt.