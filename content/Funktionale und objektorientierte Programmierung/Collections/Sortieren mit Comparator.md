# Sortieren mit Comparator
## Sortieren einer List mit Comparator
```java
List<Student> list = new LinkedList<Student> ():

for(int i = 0; i < 100000; i++) {
	Student s = new Student();
	s.enrollmentNumber = ((5432 * i) % 4321);
	list.add(s);
}

Collections.sort(list, new EnrollmentNumberComparator());
```
Hier wird eine [[Zusätzliche Methoden von List|List]] mit der Klasse Comparator%%hier ggf Comparator aus 06 linken%% sortiert. Als Sortieralgorithmus wird der `EnrollmentNumberComparator` gewählt.