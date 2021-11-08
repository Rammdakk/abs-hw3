from extender import *
from random import randint


def GenerateArray(container, len):
    arrayLen = len
    i = 0  # Индекс, задающий текущую строку в массиве
    figNum = 0
    while figNum < arrayLen:
        key = randint(1, 3)
        # print("key = ", key)
        if key == 1:  # признак символьного шифра
            shape = Symbols()
            shape.RandomGenerate()  # чтение шифра с возвратом позиции за ним
        elif key == 2:  # признак циклического шифра
            shape = Cyclic()
            i = shape.RandomGenerate()  # чтение шифра с возвратом позиции за ним
        elif key == 3:  # признак цифрового шифра
            shape = Number()
            shape.RandomGenerate()  # чтение шифра с возвратом позиции за ним
        else:
            # что-то пошло не так. Должен быть известный признак
            # Возврат количества прочитанных шифров
            return figNum
        container.store.append(shape)
        figNum += 1
    return figNum
