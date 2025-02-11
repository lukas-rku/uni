---
title: Zahlen in SystemVerilog
description: Lernzettel - Digitaltechnik
draft: false
date: 2025-02-09
tags:
---
## Syntax für numerische Literale in SystemVerilog
- Syntax: `<N>'<B><wert>`
	- `<N>` = Bitbreite
	- `<B>` = Basis (`d,b,o,h`)
	- beide Angaben optional (default: `32'd`)
	- Werte werden mit führenden 0en  bis zur Bitbreite aufgefüllt
	- Unterstriche als optischer Trenne möglich (werden ignoriert)

| Literal        | Bitbreite | Basis       | Dezimal | **[[../Zahlensysteme/Zahlensysteme#Definition vorzeichenloses Stellenwertsystem\|binär]]** |
| -------------- | --------- | ----------- | ------- | ------------------------------------------------------------------------------------------ |
| `3'b101`       | 3         | binär       | 5       | `101`                                                                                      |
| `'b11`         | 32        | binär       | 3       | `000...0011`                                                                               |
| `8'b11`        | 8         | binär       | 3       | `00000011`                                                                                 |
| `8'b1010_1010` | 8         | binär       | 171     | `10101011`                                                                                 |
| `3d6`          | 3         | dezimal     | 6       | `110`                                                                                      |
| `6'o42`        | 6         | oktal       | 34      | `100010`                                                                                   |
| `8'hAB`        | 8         | hexadezimal | 171     | `10101011`                                                                                 |
| 42             | 32        | dezimal     | 42      | `000...0101010`                                                                            |
