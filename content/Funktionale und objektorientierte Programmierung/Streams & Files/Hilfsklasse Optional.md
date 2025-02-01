---
title: Die Hilfsklasse Optional
description: Lernzettel - funktionale und objektorientierte Programmierung
draft: false
date: 2025-02-01
tags:
  - incomplete
---
## Illustratives Beispiel
```java
Optional<Number> opt1 = Optional.ofNullable(new Integer(123));
Optional<Number> opt2 = Optional.ofNullable(null);

Number n1 = opt1.get(); // n == 123
Number n2 = opt2.get(); // NoSuchElementException
Number n3 = opt1.orElseGet(() -> 0);
Number n4 = opt2.orElseGet(() -> 0);
```
Zunächst werden zwei Variablen vom Typ Optional eingerichtet, bei denen der [[Generische Klassen|generische]] Typparameter mit Number instanziiert ist. Die Klasse `ofNullable` erzeugt ein Objekt von Klasse `Optional` und liefert einen Verweiß darauf zurück.