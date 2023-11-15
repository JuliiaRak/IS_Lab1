# Лабораторна робота #1 "База знань"

Запускати наступним чином:

``` bash
python3 main.py <path-to-facts> <path-to-rules>
```

Після запуску програми введіть предикат у форматі рядка через stdin. Програма аналізує предикат і виводить в stdout всі можливі комбінації змінних, для яких цей предикат є вірним. Наприклад:

``` bash
python3 main.py resources/facts.txt resources/rules.txt
Child ?child ?parent
?child : jill_mother, ?parent : donald_grandfather
?child : joe_father, ?parent : stacy_grandmother
?child : karen_child, ?parent : joe_father
?child : sam_mother, ?parent : donald_grandfather
?child : alex_child, ?parent : joe_father
?child : karen_child, ?parent : jill_mother
?child : alex_child, ?parent : jill_mother
```

Можливі запити:
Siblings ?person1 ?person2 (Сестра чи брат)
Child ?child jill_mother (Діти конкретного батька чи матері)
Parent ?parent karen_child (Батьки конкретної дитини)
GrandChild ?grandchild donald_grandfather (Онуки)
SonInLaw ?soninlaw donald_grandfather (Зяті)
DaughterInLaw ?daughterinlaw stacy_grandmother (Невістки)
Married ?person1 ?person2 (Хто в шлюбі)
SiblingInLaw ?person1 ?person2 (Брати або сестри за заміжжям)


Для завершення програми введіть `exit`
