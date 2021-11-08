from extender import *
from random import randint


def GenerateArray(container, len):
    arrayLen = len
    i = 0  # Индекс, задающий текущую строку в массиве
    figNum = 0
    while figNum < arrayLen:
        key = randint(1, 3)
        # print("key = ", key)
        if key == 1:  # признак прямоугольника
            shape = Symbols()
            shape.RandomGenerate()  # чтение прямоугольника с возвратом позиции за ним
        elif key == 2:  # признак треугольника
            shape = Cyclic()
            i = shape.RandomGenerate()  # чтение треугольника с возвратом позиции за ним
        elif key == 3:  # признак треугольника
            shape = Number()
            shape.RandomGenerate()  # чтение треугольника с возвратом позиции за ним
        else:
            # что-то пошло не так. Должен быть известный признак
            # Возврат количества прочитанных фигур
            return figNum
        container.store.append(shape)
        figNum += 1
    return figNum
