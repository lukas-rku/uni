---
title: Zyklische Listen
description: Lernzettel - funktionale und objektorientierte Programmierung
draft: false
date: 2025-01-31
tags:
---
## Das Rundlaufverfahren
Bei einer zyklischen Liste zeigt das letzte Listenelement einer [[Eigene LinkedList-Klasse|LinkedList]] mit `next` auf den `head` der Liste. Diese werden unter anderem in Rundlaufverfahren (*Round Robin*) für beispielsweise die Zeitvergabe auf einem Prozessor eingesetzt. Hier bekommt jeder Prozess eine kleine Zeitscheibe die sie nutzen können bevor sie wieder suspendiert werden. Der momentan laufenden Prozess ist der, auf den `head` verweißt. Ist dessen Zeit abgelaufen so geht `head` in der Liste um einen Schritt weiter zu dem nächsten Prozess.