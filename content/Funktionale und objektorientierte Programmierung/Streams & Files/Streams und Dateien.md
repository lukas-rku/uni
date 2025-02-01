---
title: Streams & Dateien
description: Lernzettel - funktionale und objektorientierte Programmierung
draft: false
date: 2025-02-01
tags:
  - incomplete
---
## aa
```java
String homeDir = System.getProperty("user.home");
String fileSep = System.getProperty("file.separator");
Path path = Paths.get(homeDir, "fop", "streams.txt");

try (Stream<String> stream = Files.lines(path)) {
    String fileContentAsString = stream.reduce("", String::concat);
} catch (IOException exc) {
    System.out.print("Could not open file " + fileSep + homeDir + 
                     fileSep + "fop" + fileSep + "streams.txt" + "!");
}

```
[[System Properties]]
[[Streams]]
[[Optional]]