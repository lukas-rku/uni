---
title: (In)korrektheit auf den einzelnen Abstraktionsebenen
description: Lernzettel - funktionale und objektorientierte Programmierung
draft: false
date: 2025-02-03
tags:
 - incomplete
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
### Logische Ebene
### Spezifikatorische Ebene