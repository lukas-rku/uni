---
title: Korrektheit von rekursiven Subroutinen
description: Lernzettel - funktionale und objektorientierte Programmierung
draft: false
date: 2025-02-06
tags:
---
```racket
(define (factorial n) (if (= n 0) 1 (* n (factorial (-n 1)))))

(define (sum list)
	(if (empty? list) 0 (+ (first list) (sum (rest list)))))
```
## Rekursionsabbruch
Damit die Reukursion ordentlich terminiert, muss es einen Rekursionsabruch geben. Das heißt, eine Bedingung wird abgefragt, und falls diese erfüllt ist, bricht die Rekursion ab. 
- `if(= n 0)`
- `if(empty? list)`
## Rekursionsschritt
Der wichtige Punkt hier ist, dass der rekursive Aufruf ein ausreichendes Stück näher an der Abbruchbediungung dran ist, so dass nach endlich vielen Schritten der Rekursionsabbruch erreicht ist.

Bei der Fakultätsfunktion wird `n` um `1` herunter gezählt. Vorbedingung bei der Fakultätsfunktion ist, dass der Parameter eine nichtnegative ganze Zahl sein muss. Sofern diese Vorbedingung erfüllt ist, führt Herunterzählen um `1` nach so vielen Schritten zur Abbruchbedingung, wie die Zahl `n` beim ersten rekursiven Aufruf groß ist.
- `(factorial(- n 1))`

Vergleichbar sieht das bei den typischen rekursiven Durchläufen durch Listen aus, so wie auch hier. Die Länge der Liste wird bei jedem rekursiven Aufruf um `1` kürzer und erreicht daher nach so vielen Schritten die Abbruchbedingung, wie die List ursprünglich lang war.
- `(sum (rest list))`
## Korrektheit von `find-zero`
```racket
(define find-zero f a b)
  (local
    ((define m (/ (+ a b)2 )))
      (cond
        [(< (- b a) epsilon) m]
		[(> (* (f a) (f m))0 ) (find-zero f m b)]
		[else (find-zero f a m)]))
```
### Kein Programmabbruch mit Fehlermeldung
Das einzige Kritische bei der Funktion `find-zero` ist die Anwendung von arithmetischen Operatoren und Vergleichsoperatoren. Aber nach Vorbedingung sind die Typen der Parameter Kompatibel mit den Operatoren. Es kann nichts passieren, solange der Nutzer seinen Teil des Vertrags einhält.
### Termniniert nach endlich vielen Schritten
```racket
[(< (- b a) epsilon) m]
```
In jedem rekursiven Schritt wird die Differenz zwischen `a` und `b` halbiert. Falls diese nicht um mehr als `epsilon` auseinander liegen, gibt es *null* rekursive Schritte, falls sie nicht mehr als `2 * epsilon` auseinander liegen, gibt es *einen* rekursiven Schritt, falls sie nicht mehr als `4 * epsilon` auseinander liegen, gibt es *zwei* rekursive Schritte und so weiter.

Dieses Bildungsgesetz lässt sich verallgemeinern: Falls die ursprünglichen Werte von `a` und `b` nicht um mehr als $2^n \cdot \text{epsilon}$ auseinander liegen, gibt es nur noch `n` rekursive Schritte. Also: Sei $x=\frac{b-a}{\text{epsilon}}$, dann gibt es $log_2(x)$ viele Schritte.

Insbesondere ist Termination gewährleistet, d.h. die Abbruchbedingung wird irgendwann erreicht.
### Ergebnis bei Termination ist korrekt
```racket
[(< (- b a) epsilon) m]
```
Nach Vorbedingung ist sicher, dass zwischen `a` und `b` mindestens eine Nullstelle von `f` zu finden ist. Die Funktion `find-zero` liefert bei Rekursionsabbruch einen Wert zurück, der garantiert nicht weiter als `epsilon` von jedem Punkt im Intervall von `a` nach `b` entfernt ist, also auch von mindestens einer Nullstelle der Funktion `f` nicht weiter als `epsilon` entfernt.

Man hätte sich einen rekursiven Schritt sparen können, denn tatsächlich ist der Rückgabewert höchstens $\frac{\text{epsilon}}{2}$ von einer Nullstelle entfernt.
## Theoretische Einordnung
Hinter der Korrektheit einer rekursiven Subroutine steckt grundsätzlich immer das aus der Mathematik bekannte Beweisprinzip der [[../../Mathematik 1/Lineare Gleichungssysteme/Vollständige Induktion|vollständigen Induktion]].
- Induktionsbehauptung: Für Induktionsparameter = Problemgröße $h\ge0$ erfüllt die Subroutine ihren Vertrag.
- Induktionsanfang, $h = 0$: Die Anweisungen im Rekursionsabbruch sorgen dafür, dass der Vertrag erfüllt ist.
- Induktionsvoraussetzung für $h > 0$: Der Vertrag gelte für $0,1,...,h-1$
- Induktionsschritt $h>0$: Unter der Vorraussetzung, dass der Vertrag für $0,1,...,h-1$ gilt, sorgen die Anweisungen im Rekursionsschritt dafür, dass er auch für $h$ gilt.

Siehe auch: [[Korrektheit von Subroutinen]]