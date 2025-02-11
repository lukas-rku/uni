---
title: Basics von Racket
description: Lernzettel - funktionale und objektorientierte Programmierung
draft: false
date: 2025-02-08
tags:
---
## Funktionen definieren
```java
public class X {
	public static double add(double x, double y) {
		return x + y;
	}
}

double sum = X.add(2.71,3.14);
```
Um in `Java` eine recht einfache Funktionalität zu implementieren, muss man erst eine Klasse erstellen, dann darin eine Methode definieren und diese dann mit den richtigen Parametern und Parametertypen aufrufen. Hier stößt man auch direkt auf die Limitation, dass man sich auf Parametertypen beschränken muss. Natürlich kann man auch Umwege wie bspw. die Klasse `BigDecimal` aus dem Package `java.math` verwenden, diese Verkomplizieren den Code allerdings noch ein weiteres Stück.

```racket
(define (add x y) (+ x y))
```
Hier nun die Implementation in `Racket`.
- Zunächst definiert man die Funktion mit `(define ... )`.
- Daraufhin folgt der Aufbau `(<Name> <Parameter1> <Parameter2> <...>)`
- Als letzter Bestandteil folgt die Implementation der Funktion: `(+ x y)`. Hier kann man auch sehen, dass die Schreibweise in sogenannter Präfixnotation (`<Operator> <Operand1> <Operand2>`), im Gegensatz zur Infixnotation, ist.
- Eine weitere generelle Regel ist, dass jede syntaktische Einheit, die nicht atomar ist, die also aus mehr als einem Identifier oder Literal zusammengesetzt ist, in Klammern geschrieben wird. Zudem haben Operationen und Funktionen in `Racket` keine unterschiedlichen Bindungsstärken, sondern es müssen *immer alle* Klammern gesetzt werden.

```java
System.out.println(X.add(2.71,3.14))
```
```racket
(add 2.71 3.14)
```
Auch der Aufruf einer Funktion gestaltet sich in funktionalen Sprachen sehr viel einfacher. Im Gegensatz zu `Java` ist der Aufruf in `Racket` sehr schlicht. Wieder dasselbe Muster wie bei der Definition der Funktion: Zuerst der Name der Funktion, dann die Parameter. Alles zusammen in Klammern und ohne Trennsymbole, nur Whitespaces. Wenn wir im System `DrRacket` den Aufruf hinschreiben, dann wird das Ergebnis im Ausgabefenster auf den Bildschirm geschrieben. Das heißt, der umständliche Aufruf zum Schreiben auf den Bildschirm entfällt auch noch.

## Konstanten definieren
```java
public class Math {
	...
	public static final double PI = 3.14159;
	...
}
```
```racket
(define my-pi 3.14159)
(define my-pi (+ 3 0.14159)) ; als Addition in der Definition
```
Im Gegensatz zu `Java` ist die Definition von Konstanten auch wieder sehr kurz: Zuerst das Schlüsselwort `(define ...)`, dann der Name der Konstanten `my-pi` und dann der definierende Ausdruck `3.14159`. Besteht der definierende Ausdruck nur aus einem einzigen Identifier oder Literal wie hier, dann wird er *nicht* in Klammern gesetzt.

Der Definierende Ausdruck muss natürlich kein einfacher Ausdruck, sondern kann auch wieder ein zusammengesetzter Ausdruck sein. Allerdings muss dann ein solcher zusammengesetzter Ausdruck in `Racket` *immer* in Klammern gesetzt sein.

Der syntaktische Unterscheid zur Definition einer Funktion, die keine Parameter hat, darin, dass der Name nicht in Klammern steht:
- Konstante: `(define my-pi 3.14159)`
- Funktion ohne Parameter: `(define (my-pi))`
Außerdem wird hier die Konstante nicht `pi` sondern `my-pi` genannt, da `pi` in `Racket` schon vordefiniert ist und dieser Identifier daher nicht noch einmal für eine Definition verwendet werden kann.

Alles, was nach einem Semikolon `;` noch in derselben Zeile kommt, ist auskommentiert, so wie beim doppelten Slash `//` in `Java`.

## Identifier
Folgende Zeichen sind nicht erlaubt:
- ``( ) [ ] { } " . ` ' ; | \``
- Whitespaces ` ` sind ebenfalls nicht erlaubt
- Reine Zahlen wie `32` gehen nicht, `a32` oder `32a` allerdings schon

## Konvention
- Keine Großbuchstaben
- Bindestriche zwischen einzelnen Wörtern
	- `this-identifier-conforms`

## Zahlen in `Racket`
- Exakte Zahlen
	- ganzzahlig: `123`
	- rational: `3/5`
- Nichtexakte Zahlen
	- `(sqrt 2)`
- Komplexe Zahlen
	- `3.14159 + 3/5i`
Im Gegensatz zu Java werden auch rationale Zahlen exakt dargestellt, durch Zähler und Nenner. So auch der Zahlenwert 0.6, da er im Binärsystem nicht exakt darstellbar ist. Summe, Differenz, Produkt und Quotient zweier rationaler Zahlen werden in `Racket` wieder durch Zähler und Nenner exakt dargestellt. So werden auch nichtexakte Zahlen nichtexakt, z.b. als $\sqrt{2}$ dargestellt. Genau so auch komplexe Zahlen. Tatsächlich kann man deshalb in `Racket` auch Wurzeln aus negativen Zahlen ziehen.

## Arithmetische Operationen
```racket
(+ 2 3)         ; 5
(- 4 3)         ; 1
(* 5 2)         ; 10
(/ 37 30)       ; 1.2333...
(modulo 20 3)   ; 2

(* (+ 2 3) 4)                     ; 20
(/ 4 (- 3 2))                     ; 4
(+ (+ (* 3 5) (* 4 6)) (/ 8 3))   ; 41.66666...

(+ 3 4 5)     ; 12
(* 1 2 3 4)   ; 1 * 2 * 3 * 4 = 24
(/ 1 2 3 4)   ; 1 / (2 * 3 * 4) = 1/24

(sqrt 4)      ; 2
(sqrt 5)      ; #i2.236
pi            ; #i3.141...
(- e)         ; #i-2.718...
```
Rechenergebnisse, die in `Racket` nicht exakt darstellbar sind, da sie irrational sind, werden mit einem Hashmark `#` und einem `i` vor dem Zahlenwert dargestellt.

## Operationen mit ganzen Zahlen
```racket
(floor 3.14)       ; 3
(ceiling 3.14)     ; 4
(gcd 357 753 573)  ; größter gemeinsammer Teiler (greatest common denominator)
(modulo 753 357)   ; Rest der ganzzahligen Division 753/357
```

## Boolesche Operationen
```racket
#t     ; true
#f     ; false

(and b1 b2 b3)
(or b1 b2 b3)
(not b)
; Der Gesamtausdruck ist genau dann true,
; wenn bei "and" jeder der Parameter und bei "or" mindestens einer der
; Parameter true ist.

(= x1 x2 x3)    ; (and (= x1 x2) (= x2 x3))
(< x1 x2 x3)    ; (and (< x1 x2) (< x2 x3))
(<= x1 x2 x3)   ; (and (<= x1 x2) (<= x2 x3))
```

## Verzweigung
```racket
(define (my-abs x) (if (< 0 x) x –x))

(define (my-max x y) (if (< x y) y x))

(define (sqr-of-max x y) (if (< x y) (* y y) (* x x)))

(define (diff-is-integral x y)
	(if (integer? (– x y)) #t #f))
```
Aus `Java` kennt man die `if`-Verzweigung und den Bedingungsoperator. Auch in `Racket` gibt es eine `if`-Verzweigung. Diese wird analog zum Bedingungsoperator in `Java` gebildet.

Auch wenn es nicht ganz der Systematik hinter `Racket` entspricht:
Sie können sich die `if`-Verzweigung in `Racket` als eine boolesche Funktion mit drei Parametern vorstellen. Der Name dieser Funktion ist einfach: `if`.

Die vordefinierte boolesche Funktion `integer?` haben wir bisher noch nicht gesehen. Sie hat einen Parameter und liefert genau dann `true` zurück, wenn der Parameter eine ganze Zahl ist. 
Wichtig ist, dass es hier – anders als in `Java` – nicht um formale Typen, sondern wirklich um deren Werte geht. So könnten `x` und `y` beliebige exakt darstellbare, also rationale oder sogar komplexe Zahlen mit rationalem Real- und Imaginärteil sein: Sofern ihre Differenz eine ganze Zahl ist, wird `true` zurückgeliefert.

Der zweite Parameter der Funktion `if` ist der Rückgabewert der `if`- Funktion in dem Fall, dass der erste Parameter `true` zurückliefert. Das ist also völlig analog zum Bedingungsoperator in `Java`.

Und ebenso analog zum Bedingungsoperator in `Java` ist, dass es – im Gegensatz zur `if`-Verzweigung in Java – unbedingt eine Art `else`-Teil geben muss. Das ist der dritte Parameter: Sein Wert ist der Rückgabewert der gesamten `if`-Funktion in dem Fall, dass der erste Parameter `false` ergibt.

## Boolesche Operationen
```racket
(number? x)    ; ist x eine Zahl?
(real? x)      ; ist x eine nicht echt komplexe Zahl (Imaginärteil = 0)?
(rational? x)  ; ist x eine rationale Zahl?
(integer? x)   ; ist x eine ganze Zahl?
(natural? x)   ; ist x eine ganze positive Zahl?
(symbol? x)    ; ist x ein Symbol?
(string? x)    ; ist x ein String?
```

## Symbole
```racket
(define last-name 'Spielberg)

(if (symbol=? last-name 'Max) (...) (...))
```
Ein Symbol hat für `Racket`, im Gegensatz zu [[#Identifier|Identifier]], keinen Aussagewert. Ein Identifier hingegen ist eine Funktion oder eine Konstante.

Das Gleichheitszeichen und das Fragezeichen gehören zum Namen der vordefinierten booleschen Funktion `symbol=?`. Sie ist auf Symbole anwendbar und liefert genau dann `true`, wenn erstens beide Parameter Symbole sind und zweitens die beiden Symbole zudem gleich sind. Viel mehr als Test auf Gleichheit oder Ungleichheit kann man mit Symbolen auch nicht machen, da Symbole für Racket eben keine Bedeutung haben.

## Typ einer Funktion
```racket
;; Type: number number -> number
;;
;; Returns: the sum of the two parameters

(define (add x y) (+ x y))
```
Tatsächlich wird in `Racket` erst zur Laufzeit geprüft, ob die Typen der Operanden einer Operation zu dieser Operation passen. Und wenn das nicht der Fall ist, bricht DrRacket die Ausführung des Programms mit einer entsprechenden Fehlermeldung ab.

Für den Nutzer einer Funktion sollte man daher unbedingt etwas tun, was in `Java` nicht nötig ist: In einem Kommentar [[../../Korrekte Software/Korrektheit von Subroutinen#Subroutinen als "Vertrag"|vertraglich]] zusichern, welche Typen die Parameter haben und welcher Typ zurückgeliefert wird.

Dieses Beispiel folgt der allgemeinen Konvention für `Racket`: eine Aufzählung der Parametertypen in der selben Reihenfolge, wie sie bei der Definition und beim Aufruf der Funktion auftreten, nach einem Pfeil dann der Rückgabetyp, das alles wieder ohne Kommas oder ähnliches.

Außerdem sollte man zu jeder Funktion – und sei sie noch so einfach – in einem Kommentar dazuschreiben, was der Wert eigentlich beinhaltet, der zurückgeliefert wird. Das ist bei `Java` natürlich genauso.

## Laufzeitchecks
```racket
;; Type: number number ->
;; Precondition: the second parameter must not equal zero
;; Returns: x divided by y
(def (divide x y) (/x y))

(check-expect (divide 15 3)5)
(check-within (divide pi e)1.15 0.01)
(check-error (divide 15 0) "/: division by zero")
```
`Racket` bietet auch Möglichkeiten, die Korrektheit von Funktionen zur Laufzeit zu testen. Die vordefinierte Funktion `check-expect` bekommt zwei Ausdrücke als Parameter und liefert eine Fehlermeldung, falls die beiden Ausdrücke nicht den gleichen Wert haben. Wenn der Test gelingt, läuft die Ausführung des Programms weiter, ansonst wird sie mit einer entsprechenden Fehlermeldung abgebrochen.

Wird jedoch das Ergebnis von `divide` mit nicht exakt darstellbaren Zahlen wie `pi` und `e` mittels `check-expect` getestet, muss der zweite Parameter exakt alle Nachkommastellen des Ergebnisses enthalten, da sonst die Werte nicht übereinstimmen und der Test fehlschlägt. In der Praxis ist es selten möglich, das exakte Ergebnis einer Funktion anderweitig zu ermitteln. Stattdessen liegt meist nur ein Näherungswert vor. Mit `check-within` kann man daher überprüfen, ob zwei Zahlen innerhalb eines vorgegebenen Toleranzbereichs liegen. Überschreitet der Unterschied den dritten Parameter, liefert der Test eine Fehlermeldung und bricht die Ausführung ab.

Zur Sicherstellung der Funktionalität von `divide` gehört es, dass eine Fehlermeldung ausgegeben wird, wenn der Divisor 0 ist. Dafür verwendet man `check-error`, das dann als erfolgreich gilt, wenn der erste Parameter einen Fehler liefert, der exakt mit dem zweiten Parameter übereinstimmt. Fehlermeldungen werden als Strings in doppelten Hochkommas dargestellt – ähnlich wie in Java. Die genaue Fehlermeldung liest man in der Racket-Dokumentation nach und verwendet sie als Vergleichswert im Test.

```racket
;; Type: number number -> number
;; Precondition: the second parameter must not
;; equal zero
;; Returns: x divided by y
(define (divide x y)
	(if (= y 0) (error “Division by 0“) (/ x y)))
```
In `Racket` gibt es auch Möglichkeiten, Tests direkt in Funktionen zu integrieren. Im Gegensatz zu `check-expect`, `check-within` und `check-error`, die Tests einmalig mit vorgegebenen Parametern ausführen, wird der in die Funktion eingebaute Test bei jedem Aufruf mit den aktuellen Werten durchgeführt. Eine einfache Methode dazu ist der Einsatz der vordefinierten Funktion `error`, die einen frei wählbaren String als Parameter annimmt. Wird `error` aufgerufen – etwa wenn im Beispiel der Divisor `y` gleich 0 ist – bricht das Programm mit einer Fehlermeldung ab, in deren Wortlaut der übergebene String enthalten ist.

## Komplexere Berechnung
```java
public class X{
	public static double euclid2(double x, double y) {
		return Math.sqrt(x * x + y * y)
	}
}
```
```racket
;; Type: real real -> real
(define (euclid2 x y) (sqrt (+ (* x x) (* y y))))
```
Laut Typ erwartet die Funktion `euclid2` vom Nutzer, dass die Parameter `x` und `y` reelle Zahlen sind, und garantiert in diesem Fall, dass auch das Ergebnis eine reelle Zahl ist. Zwar könnte `euclid2` problemlos komplexe Zahlen verarbeiten, jedoch unterscheidet sich die Definition der euklidischen Norm für Vektoren auf komplexen Zahlen von jener für Vektoren auf reellen Zahlen. Um Verwirrung zu vermeiden, ist der Typ daher ausschließlich auf reelle Zahlen festgelegt.