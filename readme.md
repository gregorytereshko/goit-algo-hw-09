# Порівняння жадібного алгоритму та алгоритму динамічного програмування для видачі решти

## Вступ

У цьому документі порівнюється ефективність двох алгоритмів для видачі решти: жадібного алгоритму та алгоритму динамічного програмування. Розглядаються їхні часові характеристики та ситуації, у яких один алгоритм може бути більш ефективним за інший.

## Часові характеристики

На прикладі видачі решти у розмірі 100 одиниць із використанням набору монет [50, 25, 10, 5, 2, 1] було проведено заміри часу виконання обох алгоритмів:

- Жадібний алгоритм: 0.00000467 секунд
- Динамічне програмування: 0.000508 секунд

## Висновки

1. **Жадібний алгоритм** виявився швидшим за алгоритм динамічного програмування у даному випадку. Це пояснюється тим, що жадібний алгоритм має меншу часову складність (O(n), де n - кількість номіналів монет) порівняно з динамічним програмуванням (O(mn), де m - сума для видачі).

2. **Динамічне програмування** забезпечує знаходження мінімальної кількості монет для будь-якої суми, але може бути повільнішим при великих сумах через більшу часову складність.

3. **Вибір алгоритму** залежить від конкретної ситуації: для швидкої видачі решти за умови, що номінали монет дозволяють досягти оптимального рішення, підходить жадібний алгоритм. Для знаходження мінімальної кількості монет у загальному випадку краще використовувати алгоритм динамічного програмування.
