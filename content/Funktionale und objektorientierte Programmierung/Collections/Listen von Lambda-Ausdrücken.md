## Lambda-Ausdrücke in einer `List`
```java
List<IntPredicate>  predicates = new ...();
predicates.add(n -> n % 2 == 1);
predicates.add(n -> n > 0);
predicates.add(n -> n * n < 100);
predicates.add(predicates.get(0).negate());
predicates.add(predicates.get(1).and(predicates.get(2)));
predicates.add(predicates.get(3).or(predicates.get(4)));
```
%%Hier Link zu Array IntPredicate aus 04c%%
Die von [[Collection|Collection]] ererbte Methode [[Methoden von Collection#`add`|add]] hat keinen Index als Parameter. Stattdessen wird das neue Element einfach an die Liste angehängt. Die Methode [[Zusätzliche Methoden von List#`get`|get]] wird benötigt um auf ein Listenelement zuzugreifen. Natürlich kann man Lambda-Ausdrücke nicht nur in Listen, sondern auch in beliebige Collections einfügen.