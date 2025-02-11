---
title: Bits und Bytes
description: Lernzettel - Digitaltechnik
draft: false
date: 2025-02-09
tags:
---
## Binärsystem als [[../SystemVerilog/Sinn eines Schichtenmodells#Disziplin|Digitale Disziplin]]
- Beschränkung auf nur zwei unterschiedliche Werte
- Können unterschiedlich heißen
	- 1, WAHR, TRUE, HIGH, ...
	- 0, FALSCH, FALSE, LOW, ...
- Können unterschiedlich repräsentiert werden
	- elektronisch (Spannungspegel)
	- mechanisch (Zahnradstellungen)
	- hydraulisch (Flüssigkeitsstände)
	- aber rauch Quantenzustände, uvm.

## Bits
- Bit (Binary digit): Maßeinheit für Information (Unterscheidung zwischen zwei Zuständen)
- Antwort auf Entscheidungsfragen (bspw. "Ist die Erde eine Scheibe?") kann mit einem Bit codiert werden
- Bit ist die kleinstmöglichste Informationseinheit

- Warum ist eine solche Kodierung notwendig bzw. sinnvoll?
	- Technische Realisierung über Schwellwerte ist einfacher, bspw:
		- Elektrische Ladungen (0 = ungeladen, 1 = geladen)
		- Elektrische Spannungen (0 = 0 Volt, 1 = 5 Volt)
		- Magnetisierung (0 = unmagnetiesert, 1 = magnetisiert)

## Bitfolgen
- Meh als zwei Zustände / Antwortmöglichkeiten repräsentiert werden
- Beispiel: Aus welcher Himmelsrichtung weht der Wind
	- 0 0 = Norden
	- 0 1 = Osten
	- 1 0 = Süden
	- 1 1 = Westen
	- 2 bit für vier Zustände
- 3 bits für Kodierung für {S, SW, W, ..., O, SO}

## Zweierpotenzen
- $2^{10}=1024$ Kibi (Ki)
- $2^{20}=1048576$ Mebi (Mi)
- $2^{30}=1073741824$ Gibi (Gi)
- $2^{40}=1099511627776$ Tebi (Ti)

## Größenfaktoren in der Informatik nach IEC
| Einheit | Name | Potenz      | Wert                          |
| ------- | ---- | ----------- | ----------------------------- |
| 1 Ki    | Kibi | \(2^{10}\)  | 1024                          |
| 1 Mi    | Mebi | \(2^{20}\)  | 1024 × 1024                   |
| 1 Gi    | Gibi | \(2^{30}\)  | 1024 × 1024 × 1024            |
| 1 Ti    | Tebi | \(2^{40}\)  | 1024 × 1024 × 1024 × 1024     |
| 1 k     | Kilo | \(10^3\)    | 1000                          |
| 1 M     | Mega | \(10^6\)    | 1 000 × 1 000                 |
| 1 G     | Giga | \(10^9\)    | 1 000 × 1 000 × 1 000         |
| 1 T     | Tera | \(10^{12}\) | 1 000 × 1 000 × 1 000 × 1 000 |
- Achtung: Basis oft nicht eindeutig
- bspw. bei Festplatten: Ein GB wird als 1 000 000 000 Byte $\approx$ 0.93 GiByte verkauft

## Nomenklatur für Teile von Bitfolgen
- 32 Bits = 8 Nibble = 4 Byte = 2 Halbwörter = 1 Wort
- Größe eines (Halb-) Worts hängt vom Kontext ab (meist Registerbreite)
- Mittlerweile gibt es auch 64-Bit Systeme, wo ein Wort also 64 Bit lang ist, zwei Halbwörter aus 32 Bit und aus diese 8 Byte besteht