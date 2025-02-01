---
title: Kurzform der for-Schleife bei Collections
description:
draft: false
date: 2025-01-31
tags:
---
## `for`-Schleifen mit Collections
```java
public void writeAllElements(Collection<String> coll) {
	for(String str:coll) {
		System.out.print(str);
	}
}
```
Wie bei der Kurzform von Arrays kann man auch [[Collection|Collections]] mit `for`-Schleifen durchlaufen. %%ggf. Kurzform von Arrays anhängen%%