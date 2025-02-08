---
title: Definitionen verstecken
description: Lernzettel - funktionale und objektorientierte Programmierung
draft: false
date: 2025-02-08
tags:
---
## Definitionen "verstecken" in `Java`
```java
public class {
	private int n;
	private void m1() {...}
	public void m2() {...}
	public void m3() {...}
}
```
Attribute `n` und Methode `m1` sind nur in `m1`, `m2` und `m3` sichtbar, also innerhalb der Klasse.
## Definitionen "verstecken" in `Racket`
```racket
;; fct: number -> number
(define (fct x)
	(local
		((define const 10)
		(define (mult-const y) (* const y)))
		(+ const (mult-const x))))

; Konstante const und Funktion mult-const sind nur im local-Ausdruck sichtbar
```
Zwischen dem Schlüsselwort `local` und dem abschließenden Ausdruck können beliebig viele Definitionen eingefügt werden, die ausschließlich innerhalb dieses Ausdrucks gültig sind. Der abschließende Ausdruck – dessen Länge und Komplexität variieren kann – bestimmt den Wert des gesamten `local`-Ausdrucks.

Ganz am Ende des `local`-Ausdrucks steht eine beliebige Art von Ausdruck. Meist ist dieser Ausdruck recht kurz wie hier, aber das muss nicht sein. Der Wert dieses Ausdrucks ist der Wert des gesamten `local`-Ausdrucks.