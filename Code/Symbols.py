import sys

from cyphers import *
from random import randint


# ----------------------------------------------
class Symbols(Cyphers):
    def __init__(self):
        self.length = 0
        self.cypher = [[], []]
        self.ciphered_text = ""
        self.deciphered_text = ""

    def ReadStrArray(self, strArray, i):
        # должно быт как минимум три непрочитанных значения в массиве
        if i >= len(strArray) - 2:
            return 0
        self.ciphered_text = strArray[i]
        i += 1
        self.length = len(self.ciphered_text)
        for x in range(self.length):
            self.cypher[0].append(strArray[i])
            self.cypher[1].append(strArray[i + 1])
            i += 2
        for x in range(self.length):
            res = ""
            for j in range(self.length):
                if self.ciphered_text[x] == self.cypher[0][j]:
                    res = self.cypher[1][j]
            self.deciphered_text += res
        # print("Rectangle: x = ", self.x, " y = ", self.y)
        return i

    def RandomGenerate(self):
        self.length = randint(3, 10)
        for i in range(self.length):
            k = chr(randint(97, 122))
            self.ciphered_text += k
            self.cypher[0].append(k)
            k = chr(randint(97, 122))
            self.deciphered_text += k
            self.cypher[1].append(k)

    def Print(self):
        print("It Symbols cipher: ciphered_text = ", self.ciphered_text, ", deciphered_text = ", self.deciphered_text,
              ". Function_result = ", self.Division())
        pass

    def Write(self, ostream):
        ostream.write("It Symbols cipher: ciphered_text = {}, deciphered_text = {}, "
                      "function_result = {}".format(self.ciphered_text, self.deciphered_text, self.Division()))
        pass

    def Division(self):
        res = 0
        for x in self.deciphered_text:
            res += ord(x)
        return res / len(self.deciphered_text)
        pass
