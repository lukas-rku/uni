---
title: Korrektheit von Subroutinen
description: Lernzettel - funktionale und objektorientierte Programmierung
draft: false
date: 2025-02-06
tags:
---
## Subroutinen als "Vertrag"
Eine **Subroutine** stellt eine Art **Vertrag** zwischen dem Entwickler und dem Nutzer dar. Dieser Vertrag besteht aus **Vorbedingungen** und **Nachbedingungen**. Vorbedingungen definieren die Voraussetzungen, die vor dem Aufruf einer Subroutine erfüllt sein müssen, damit sie korrekt funktioniert. Nachbedingungen beschreiben das erwartete Ergebnis nach der Ausführung der Subroutine, falls alle Vorbedingungen eingehalten wurden. Dies gilt insbesondere für Objektmethoden, die innerhalb einer Klasse definiert sind und auf nichtöffentliche Klassenelemente zugreifen können.
### Vorbedingungen
Zu den Vorbedingungen gehören mehrere Aspekte:
- Die **Implementationsinvariante** einer Objektmethode muss vor dem Aufruf der Methode eingehalten sein. Das bedeutet, dass sich das Objekt in einem gültigen Zustand befinden muss.
- **Parameter** müssen vor der Übergabe an die Methode bestimmte Anforderungen erfüllen, beispielsweise bestimmte Wertebereiche einhalten.
- Methoden können auf **Variablen und Konstanten außerhalb der Klasse** zugreifen, wobei auch hier Vorbedingungen gelten.
- Falls externe **Datenquellen** (z. B. Dateien) genutzt werden, müssen diese vorhanden und zugänglich sein.
### Nachbedingungen
Nach der Ausführung einer Methode müssen folgende Bedingungen sichergestellt sein:
- Die **Implementationsinvariante** der Methode muss weiterhin erfüllt sein, damit das Objekt weiterhin in einem gültigen Zustand bleibt.
- Der **Rückgabewert** muss genau den spezifizierten Anforderungen entsprechen.
- Falls eine Methode schreibend auf **Variablen außerhalb der Klasse** zugreift, müssen diese nach der Ausführung einen erwarteten Zustand haben.
- Falls externe **Daten gespeichert** werden (z. B. in Dateien), muss sichergestellt sein, dass sie korrekt geschrieben wurden.
### Methoden als Teil einer Klasse
Methoden sind spezielle Subroutinen, die zu einer Klasse gehören und Zugriff auf deren nichtöffentliche Attribute und Methoden haben. Deshalb müssen sie sicherstellen, dass sie die **Implementationsinvariante** vor und nach ihrer Ausführung einhalten. Das bedeutet, dass das Objekt vor dem Methodenaufruf in einem gültigen Zustand sein muss und nach der Ausführung weiterhin konsistent bleibt.
### Parameter und Rückgabewerte
Für eine Methode ist es essenziell, dass ihre Parameter vor dem Aufruf gültige Werte haben, da sonst Fehler auftreten können. Ebenso muss die Methode einen definierten Rückgabewert liefern, der exakt der Spezifikation entspricht. In Java übernimmt der Compiler eine **statische Typprüfung**, wodurch sichergestellt wird, dass die Typen der Parameter und Rückgabewerte korrekt sind. In Programmiersprachen wie **Racket** hingegen müssen Typen explizit in den Vertrag zwischen Entwickler und Nutzer aufgenommen werden.
### Zugriff auf externe Variablen und Konstanten
In Java können Methoden nicht nur mit Variablen innerhalb ihrer Klasse arbeiten, sondern auch auf **öffentliche Attribute anderer Klassen** zugreifen. Dies bedeutet, dass eine Methode sowohl **lesend** als auch **schreibend** auf externe Variablen zugreifen kann, was in der Entwicklung berücksichtigt werden muss, um ungewollte Seiteneffekte zu vermeiden.
## Vertrag zusammengefasst
- Type
	- Da der Java-Compiler die Typen prüft, gehören diese in Java nicht zum Vertrag, in Racket aber schon
	- Nicht bei expliziter statischer Typisierung
- Preconditions
- Returns
	- Man könnte auch den Rückgabewert unter den Nachbedingungen (`Postconditions`) subsumieren. Traditionell unterscheidet man hier aber.
- Postconditions
	- Neben der Rückgabe kann eine Subroutine auch Seiteneffekte haben, sofern nicht referntielle Transparenz eingehalten wird.
## Vor-/Nachbedingungen von Methoden bei Ableitung von Basisklasse oder Implementation von Interface
Wenn die abgeleitete / implementierende Klasse logisch konform zur Basisklasse / zum Interface sein soll, dann müssen wir auch die Methoden ihren Teil dazu beitragen

Wird eine Methode von der Basisklasse an eine abgeleitete Klasse vererb, dann erfüllt sie natürlich automatisch das [[Korrektheit von Klassen#^c47010|Liskov Substitution Principle]] (kurz LSP). Problematisch kann es nur werden, wenn die Methode in der abgeleiteten Klasse überschrieben / in der ein Interface implementierenden Klasse implementiert wird. %%????%%
### Vorbedingung
- darf nur abgeschwächt, nicht (teilweise) verschärft oder ersetzt werden
- Dann ist gewährleistet, dass der Nutzer der Methode den Vertrag vollständig einhält und nicht aus Versehen verletzt, wenn er die Methode nur über eine Referenz der Basisklasse beziehungsweise des Interface sieht und guten Glaubens den Vertrag gemäß Basisklasse / Interface einhält.
- Beispiel: Das Interface `java.util.List` hat eine Version der Methode `add`, die neben dem einzufügenden Wert noch den Index als Parameter hat, an dem der Wert einzufügen ist. In einer das Interface List implementierenden Klasse darf es keine zusätzlichen Bedingungen an den Index geben, etwas dass der Index nur gradzahlig sein darf o.ä.
### Nachbedingung
- darf nur verschärft, nicht (teilweise) abgeschwächt oder ersetzt werden
- Damit ist gewährleistet, dass der Nutzer nach Aufruf der Methode über eine Referenz der Basisklasse / des Interface keine Überraschungen bei der Rückgabe oder den Seiteneffekten erlebt. Sonst dürfte die Methode ja Effekte haben, die nicht dem Vertrag gemäß Basisklasse / Interface entsprechen
- Beispiel: Methode `add` von Interface `java.util.list` muss die Methode den neuen Wert an dem Index einfügen, an dem er gemäß Vertrag in Interface `List` einzufügen ist. Sie darf weder dieses Einfügen unterlassen noch den Wert an einem anderen Index einfügen oder andere Effekte haben.