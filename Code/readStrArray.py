from extender import *


def ReadStrArray(container, strArray):
    arrayLen = len(strArray)
    i = 0  # Индекс, задающий текущую строку в массиве
    figNum = 0
    while i < arrayLen:
        str = strArray[i]
        key = int(str)  # преобразование в целое
        # print("key = ", key)
        if key == 1:  # признак посимвольного шифра
            i += 1
            shape = Symbols()
            i = shape.ReadStrArray(strArray, i)  # чтение шифра с возвратом позиции за ним
        elif key == 2:  # признак циклического шифра
            i += 1
            shape = Cyclic()
            i = shape.ReadStrArray(strArray, i)  # чтение шифра с возвратом позиции за ним
        elif key == 3:  # признак числового шифра
            i += 1
            shape = Number()
            i = shape.ReadStrArray(strArray, i)  # чтение шифра с возвратом позиции за ним
        else:
            # что-то пошло не так. Должен быть известный признак
            # Возврат количества прочитанных шифров
            return figNum
        # Количество шифров увеличивается на 1
        if i == 0:
            return figNum
        figNum += 1
        container.store.append(shape)
    return figNum
