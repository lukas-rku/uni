---
title: Rekursion in Racket
description: Lernzettel - funktionale und objektorientierte Programmierung
draft: false
date: 2025-02-08
tags:
---
## Fakultät in `Racket` rekursiv berechnen
```java
public static int factorial (int n) {
	return == 0 ? 1 : n * factorial(n - 1);
}
```
```racket
;; Type: natural -> natural
(define (factorial n)
	(if (= n 0) 1 (* n (factorial (- n 1)))))
```
An sich ist die Überschneidung zwischen `Java` und `Racket` hier tatsächlich sehr hoch. In `Java` wird hier allerdings zur Veranschaulichung ein ternärer Ausdruck genutzt.

```racket
(factorial 4)
(* 4 (factorial 3))
(* 4 (* 3 (factorial 2)))
(* 4 (* 3 (* 2 (factorial 1))))
(* 4 (* 3 (* 2 (* 1 (factorial 0)))))
(* 4 (* 3 (* 2 (* 1 1))))
(* 4 (* 3 (* 2 1)))
(* 4 (* 3 2))
(* 4 6) ; 24
```

## Implementation von [[Basics von Racket#Laufzeitchecks|Checks]]
```racket
;; Type: natural -> natural
;; Returns: the factorial n! of n, that is, 1 if n = 0 and n * (n-1)! otherwise
(define (factorial n)
	(if (= 0 n) 1 (* n (factorial (- n 1)))))

(check-expect (factorial 0) 1)
(check-expect (factorial 5) 120)
```
Man sollte auch immer Checks zur Prüfung der Korrektheit einer Funktion einsetzen. Wichtig dabei ist, dass man immer auch die Randfälle dabei prüft. Hier ist der Randfall, dass der Parameter den Wert `0` hat.

## Rekursive Berechnung des Binomialkoeffizienten in Racket
```racket
(define (binom n k)
	(if (or (= k 0) (= k n))
	  (+ (binom (- n 1) (- k 1))
		 (binom (- n 1) k))))

;; Beispielaufruf:
(define n 5)
(define k 2)
```
Siehe [[Rekursion in Java#Rekursive Berechnung des Binomialkoeffizienten in Java|hier]].