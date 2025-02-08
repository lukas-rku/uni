---
title: (Idealisiertes) Objektmodell
description: Lernzettel - funktionale und objektorientierte Programmierung
draft: false
date: 2025-02-08
tags:
---
## Grundprinzipien
Es gibt keine Objekte, nur Werte
- Werte sind immer%%link Aufweichung der reinen funktionalen Lehre in Racket%% Konstante, nie Variable
```racket
(define my-const-1 12345)
```
- Werte werden immer kopiert. niemals modifiziert
```racket
(define my-const-2 my-const-1)
(define (my-fct my-const) (...))
```

Laufzeitsystem kann intern zur Optimierung von dieser Grundlogik abweichen
- nicht sichtbar für Programmierer
