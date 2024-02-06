import random
from itertools import product

class RandomTable:


    def __init__(self, random_table, weights = 1, name=None):
        self.random_table = random_table
        self.weights = weights
        self.name = name
    

    def roll(self):
        # проверка осталось ли в качестве весов дефолтное значение и создание весов на основе него
        if type(self.weights) == int:
            self.weights = [1 for x in range(len(self.random_table))]

        # проверка передали ли в качестве веса значение кубиков и создание весов на основе них
        elif type(self.weights) == str:
            weights = self.dices_to_weights(self.weights)

        # выбор случайного элемента
        element_of_table = random.choices(self.random_table, weights=weights, k=len(self.random_table))[0]

        # является ли элемен случайней таблицей и бросок по ней
        if element_of_table == RandomTable:
            element_of_table = element_of_table.roll()

        # добовление имени таблицы и возрапт значения
        if self.name != None:
            return '\t' + self.name + ': ' + str(element_of_table)
        else:
            return '\t' + str(element_of_table)

    
    def dices_to_weights(self, weights = 1):
        if weights == 1:
            weights = self.weights
        number_of_dices, number_of_sides = map(int, weights.split('d'))

        # Возможные значения для каждого кубика
        dice_value = range(1, number_of_sides + 1)

        # Все возможные комбинации бросков
        all_combinations = product(dice_value, repeat=number_of_dices)

        # Рассчитываем суммы значений для каждой комбинации
        sums = [sum(combination) for combination in all_combinations]

        # Веса для каждой суммы
        weights = [sums.count(сумма) for сумма in set(sums)]

        return weights


        
