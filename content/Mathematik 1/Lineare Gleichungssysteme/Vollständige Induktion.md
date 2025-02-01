---
title: Vollständige Induktion
description:
draft: false
date: 2025-01-22
tags:
  - missingImage
---
[YouTube Link](https://www.youtube.com/watch?v=MD7U_vYaX58)
1. Induktionsanfang
	- Eine Formel oder Behauptung
	- hier $1+2+3+...+n=\frac{\left(n+1\right)\cdot n}{2}$
	 ![[Pasted image 20250106142103.png]]
	- Man weiß nicht ob das auch für $n = 4$, $n = 5$ usw. gilt.
	- Man muss aber nur für eine Zahl zeigen, dass das stimmt
2. Induktionsschritt
	1. Induktionsvoraussetzung
		- "Induktionsvoraussetzung: gilt für $n = k$"
		- n mit k ersetzen
	2. Induktionsbehauptung
		- "Induktionsbehauptung: gilt für $n = k + 1$"
		- d.h. für jeden weiteren Schritt
		- also: $1+2+3+\cdots+k+\left(k+1\right)=\frac{\left(k+1+1\right)\left(k+1\right)}{2}=\frac{\left(k+2\right)\left(k+1\right)}{2}$
3. Induktionsbeweis
	- Vorraussetzung mit $k + 1$ erweitern
	- $1+2+3+\cdots+k+\left(k+1\right)=\frac{\left(k+1\right)\cdot k}{2}+\left(k+1\right)$
	- daraus  folgt mit bisschen umstellen wieder $\frac{\left(k+2\right)\left(k+1\right)}{2}$
