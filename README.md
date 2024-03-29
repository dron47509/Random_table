# Случайные Таблицы

Класс **RandomTable** предназначен для создания случайных таблиц с возможностью задания весов в различных форматах.

## Использование

Класс принимает два параметра:

1. **random_table:** Список с элементами, где элементы могут также быть случайными таблицами, и для них тоже будет выполнен бросок.
2. **weights:** Задает вероятность выпадения каждого элемента.
3. **name:** Имя таблицы.

### Допустимые форматы весов(weights):

* *Оставить пустым:* В этом случае будет просто выбран случайный элемент.
* *"2d6":* Где 2 - количество кубиков, 6 - количество граней на кубике. Количество случайных значений на кубике (в данном случае 11) должно соответствовать количеству элементов в случайной таблице.
* *[1, 3, 3]:* Обычный список весов, где количество элементов должно соответствовать количеству элементов в случайной таблице.

## Методы

* **`roll()`:** Выбрасывает случайный элемент из таблицы.
* **`dices_to_weights()`:** Возвращает веса для дайсов в случайной таблице.
