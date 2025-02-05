---
title: (In)korrektheit auf den einzelnen Abstraktionsebenen
description: Lernzettel - funktionale und objektorientierte Programmierung
draft: false
date: 2025-02-04
tags:
---
## Die Abstraktionsebenen
Bei der Entwicklung von Software sind fünf verschiedene Abstraktionsebenen wichtig, von denen man auf die Programmieraufgabe blicken kann. Im Folgenden wird betrachtet, welche typischen Fehler häufig gemacht werden.
### Lexikalische Ebene
```java
wile    ...   while
For     ...   for
stetic  ...   static
```
Auf der untersten Ebene befindet sich die lexikalische Ebene, also die Rechtschreibung.
```java
identifier            ::= <<letter-ext>> <<ident-char-list>>
identifier-char-list  ::= ε | <<ident-char>> | <<ident-char-list>>
letter-ext            ::= <<letter>> | _ | $
ident-char            ::= <<letter-ext>> | <<digit>>
letter                ::= a...z | A...Z
digit                 ::= 0...9
```
Hier eine formale Definition %%(vergleich bar mit... link Grammatik formale Sprache )%% für das Beispiel `identifier`. Die gezeigt Schreibweise ist eine gängige von vielen.

Mit dem Zeichen `:==` werden die Sprachkonstrukte formal definiert. Der Aufbau ist wie folgt: `Definiendum :== Definiens`. 

Wird ein lexikalisches oder syntaktisches Konstrukt für die Definition eines anderen syntaktischen Konstrukts verwendet, dann wird sein Name in `<<...>>`-Zeichen gesetzt. Ein verwendetes lexikalisches oder syntaktisches Konstrukt muss dann auch genau einmal links definiert sein. Ein vertikaler Strich `|` trennt die verschiedenen Alternativen, so ist beispielsweise ein `ident-char` entweder ein `<<letter-ext>`, also ein `<<letter>>` `_` oder ein `$`, oder ein `<<digit>>`. %%Link Identifier Kapitel 01a%%

Ein `ε` steht für das leere Wort, ein `<<ident-char-list>>` ist also ein syntaktisches Konstrukt, dass auch leer sein kann.

Ein korrekt gebildeter `Identifier` wäre beispielsweise `c3_Po`, da aus der gegebenen Definition zusammengebaut werden kann.
### Syntaktische Ebene
```java
(({}...)...[...]...{...[...{...}...]...})...{...[...]...(...)...}
```
Was man bei den natürlichen Sprachen unter Begriffen wie Satzlehre als Teil der Grammatik kennen, ist bei Programmiersprachen die Syntax. Zumindest so ungefähr.

Ein wichtiger Teil der Syntax bei Programmiersprachen ist die Klammersetzung. Die in dem Beispiel gezeigt ist korrekt, ob der ganze Code mit diesen Klammern allerdings Sinn macht ist auf dieser Ebene irrelevant.

Die Klammersetzung folgt zwei einfachen Regeln: Zu jeder geöffneten Klammer gehört eine nachfolgende schließende Klammer, sowie zu jeder schließenden eine öffnende gehört. Zudem sind Klammerpaare immer nacheinander oder ineinander platziert und nie teilweise überlappend.

```java
(...[...)...]...{...}...}...(...[...]
```
Hier ein Beispiel, was nicht den Regeln folgt. Es gibt hier ineinander verschränkte Klammern und Klammern, die sich schließen aber nie geöffnet wurden und sich öffnen aber nie geschlossen werden.

```java
for(...;...;...)
while(...)
do ... while(...)
```
Syntaktische Konstrukte müssen gemäß der vorgegebenen Struktur gebildet werden. Hier nur drei ausgewählte Beispiele*
- Das Schlüsselwort `for` wird zwingend von einem Klammerausdruck, in dem zwei Semikolons enthalten sein müssen, gefolgt.
- Bei der `while`-Schleife kommt ein Klammerausdruck ohne Semikolons nach dem Schlüsselwort.
- `do` wird gefolgt von einem Schleifenrumpf. Danach kommt ein `while` mit einem Klammerausdruck.

```java
statement :== <<simple-statement>>; |
	<<compund-statement>> |
	<<if-statement>> |
	<<switch-statement>> |
	<<while-loop>> |
	<<do-while-loop>> |
	<<for-loop>> |
	<<break-statement>> |
	<<continue-statement>> | ...
```

^73ff9e

Auch auf syntaktischer Ebene kann man die grundlegenden Regeln formalisieren. Hier nur ein kleiner Ausschnitt zur Bildung von Anweisungen. Da es verschiedene Arten von Anweisungen gibt, wird dies erstmal mit `statement` definiert, wonach die einzelnen Anweisungsarten aufgezählt werden.

Zu Bemerken ist, dass man in der ersten Zeile sehen kann, dass hinter jede einfache Anweisung `<<simple-statement>>` ein `;` folgen muss.

```java
compund-statement :== {<<statement-sequence>>}
statement-sequence ::= ε | <<statement>> <<statement-sequence>>
```
Danach muss jede einzelne Anwendungsart definiert werden. Eine Blockanweisung `<<compound-statement>>` ist eine Sequenz von Anweisungen in geschweiften Klammern. Eine Solche Sequenz von Anweisungen kann auch leer sein, da das Epsilon hier auch anzeigt, dass das Definiendum aus gar nicht bestehen kann. Das beantwortet die Detailfrage, ob ein `{}`-Paar leer sein kann mit ja.

Hier sieht man auch ein Beispiel einer rekursiven Definitionsregel. Eine Anweisungssequenz ist entweder leer - das ist der Rekursionsanker - oder es ist eine Anweisung gefolgt von einer Anweisungssequenz.


```java
if-statement ::= if(<<condition>>) <<statement>> |
	if(<<condition>>) <<statement>> else <<statement>>

switch-statement :== switch(<<switch-expression>>) {<<switch-list>>}
```
Im `<<if-statement>>` sieht man ein Beispiel für die indirekte Rekursion. Der Begriff [[(In)korrektheit auf den Abstraktionsebenen#^73ff9e|statement]] wird indirekt über die `if`-Anweisung wieder aufgerufen. Anders formuliert kann ein `<<statement>>` ein `<<if-statement>>` enthalten das wiederum eine oder zwei beliebiger `<<statement>>`'s enthalten kann. Hier sieht man auch, dass man bei einzelnen Anweisungen im `if`- oder `else`-Teil die geschweiften Klammern weg lassen kann, da `<<statement>>` dann zu einem `<<simple-statement>>` wird. Lässt man sie nicht weg, wird das `<<statement>>` zwangsläufig zu `<<compound-statement>> --> {<<statement-sequence>>}`.

Nach dem Schlüsselwort `switch` kommt in runden Klammern `()` ein Ausdruck mit nur sehr eingeschränkten Möglichkeiten. Daher wird spezifisch eine `<<switch-expression>>` eingeführt. In dem `{}` kommen dann die einzelnen Fälle als `<<switch-list>>`. Hier sieht man auch, dass man im Gegensatz zu `if` die geschweiften Klammern *nicht* weg lassen darf.

```java
switch-list  ::= <<case-list>> | <<case-list>> <<default-case>>
case-list    ::= ε | <<case-item>> <<case-list>>
case-item    ::= case <<case-expr>> : <<statement-sequence>>
default-case ::= default : <<statement-sequence>>
```
Hier nun den Rest zu der `<<switch-statement>>`.

```java
while-loop     ::= while(<<condition>>) <<statement>>
do-while-loop  ::= do <<statement>> while (<<condition>>);

for-loop       ::= <<long-for-loop>> | <<short-for-loop>>
long-for-loop  ::= for(<<simple-statement>>;) <<condition>>; <<expr-statement>>) <<statement>>
short-for-loop ::= for(<<type-name>> <<identifier>> : <<lvalue>>) <<statement>>

simple-statement     ::= <<variable-decision>> | <<const-declaration>> | <<expr-statement>>
variable-declaration ::= <<type-name>> <<var-list>>
var-list             ::= <<var-decl>> | <<var-decl>> , <<var-list>>
var-decl             ::= <<identifier>> | <<identifier>> = <<expr-statement>>
```

### Semantische Ebene
Syntaxfehler findet und behandelt der Compiler. Semantikfehler findet dieser in der Regel aber nicht, sondern wirken sich erst zur Laufzeit aus. Konkret heißt das, dass eine `RuntimeException` geworfen wird. Wird diese nicht gefangen, bricht das Programm ab %%Link RuntimeExceptions%%
```java
int x = 0;
int y = 1 / x;
```
Ein beliebtes Beispiel ist die Division durch `0`. In einfachen Situationen wie hier findet der Compiler diese Fehler üblicherweise. In komplexeren Situationen, wenn beispielsweise der Nutzer eine `0` für `x` wählen kann, tritt der Fehler erst zur Laufzeit auf. Daher rechnet man diesen Fehler weiterhin zu den semantischen.
```java
int[] a = new int[10];
a[0] = 2;
a[-3] = 6;
a[2012] = 11;
```
Ein weiterer beliebter Semantikfehler ist der falsche Arrayindex.  Die zweite Zeile wird problemlos ausgeführt. Die dritte und vierte allerdings nicht, da sie zu einer `ArrayIndexOutOfBoundsException` führt.
```java
String str = null;
int len = str.length();
```
Ein drittes Beispiel ist der Zugriff auf ein nichtexistierendes Objekt. So wird die Variable vom Typ `String` zwar eingerichtet, aber nicht mit einem `String`-Objekt verbunden. Da kein `String`-Objekt existiert, ist der Zugriff auf die `String`-Länge ein semantischer Fehler. Hier wird eine `NullPointerException` geworfen.
```java
int n;
n = true;

class X{...} //besitzt nicht Methode m
X a = new X();
X.m();
```
Typfehler gehören weder zur Syntax noch zur Semantik im engeren Sinne. Sie sind keine syntaktischen Fehler, weil diese nur Verstöße gegen kontextfreie Regeln betreffen, die bei Typfehlern nicht verletzt werden. In stark typisierten Sprachen wie Java werden Typfehler vom Compiler erkannt, nicht zur Laufzeit, und sind daher auch keine klassischen semantischen Fehler. Im engeren Sinn passen Typfehler nicht in die fünf Abstraktionsebenen, die in diesem Kontext behandelt werden.

Die **Syntax** regelt, ob der Quelltext formal korrekt ist und setzt eine gültige lexikalische Ebene voraus. Sie prüft nur, ob die Struktur des Programms korrekt ist, nicht jedoch die Bedeutung der verwendeten Konstrukte. Die **Semantik** hingegen beschreibt, was ein korrektes Programm tatsächlich ausführt, also seine Bedeutung und Wirkung.
### Logische Ebene
Logische Fehler sind Umsetzungsfehler. Man weiß, was das Programm eigentlich tun soll, aber durch einen Denkfehler beim Programmieren macht das Programm etwas anderes. Hier gibt es auch wieder sehr beliebte Fehler. 
![[1_inverted.png]]
Ein anschauliches Beispiel ist der sogenannte "off-by-one error". Hier wird dieses an einem Pixelraster eines Bildschirms erklärt. Nun ist die Frage, wie breit das Fenster in der Mitte ist. Die spontane Antwort ist $r-l$. Allerdings wird man feststellen, dass man sich bei der Antwort um genau eins vertut. Das Fenster ist tatsächlich $r-l+1$ breit.

Ein weiteres Problem könnte auch das Folgende sein: Sagen wir man hat sieben `Arrays` der Länge `8`. Nun befüllt man diese mit den Wochentagen auf Englisch. Für sechs von den sieben Tagen funktioniert das auch wunderbar. Am Mittwoch stürzt das Programm allerdings jede Woche ab: `Wednesday` besitzt neun Buchstaben. In der Theorie ist das Problem ganz einfach zu verstehen, allerdings ist es in der Praxis erstaunlich schwer die Quelle des Crashes zu finden. Zum einen muss man erst einmal darauf kommen, dass das Program nur Mittwochs abstürzt. Wenn die interne Fehlermeldung dem Endanwender nicht vom Programm angezeigt wird und der Fehlerfall immer erst am nächsten Tag weiterverfolgt wird, findet man den Fehler nie – und weiß noch nicht einmal warum.
### Spezifikatorische Ebene
Logikfehler waren Fehler bei der Übertragung von eigentlich richtigen Gedanken in die Progammiersprache. Spezifikatorische Fehler sind die, bei denen allein schon der Gedanke falsch ist.

Das wohl bekannteste Beispiel für Fehler der spezifikatorischen Ebene ist das Jahr-2000-Problem: In vielen Programmen wurden Jahreszahlen mit zwei statt vier Ziffern kodiert um Speicherplatz zu sparen. Bei der Jahrtausendwende war das dann natürlich ein Problem.

Ein weiteres tragisches Beispiel ist, dass ein Flugzeug nach der Landung nicht rechtzeitig abbremsen konnte, weil die Schubumkehr für einige Sekunden blockiert blieb. Der Algorithmus zur Freigabe der Schubumkehr überprüfte den Bodenkontakt der Räder anhand von Druck- und Drehgeschwindigkeitswerten. Aufgrund ungünstiger Witterungsbedingungen erkannte das System jedoch nicht, dass die Räder bereits auf dem Boden waren. Dadurch verzögerte sich die Aktivierung der Schubumkehr, sodass das Flugzeug über die Landebahn hinaus in einen Erdwall rollte.