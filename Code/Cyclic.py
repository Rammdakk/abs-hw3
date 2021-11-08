import sys

from cyphers import *
from random import randint


# ----------------------------------------------
class Cyclic(Cyphers):
    def __init__(self):
        self.cypher = 0
        self.ciphered_text = ""
        self.deciphered_text = ""

    def ReadStrArray(self, strArray, i):
        # должно быт как минимум три непрочитанных значения в массиве
        if i >= len(strArray) - 1:
            return 0
        self.ciphered_text = strArray[i]
        self.cypher = int(strArray[i + 1])
        for x in self.ciphered_text:
            self.deciphered_text += chr(ord(x) + self.cypher)
        i += 2
        # print("Rectangle: x = ", self.x, " y = ", self.y)
        return i

    def RandomGenerate(self):
        self.cypher = randint(1, 10)
        length = randint(1, 10)
        for i in range(length):
            symb = chr(randint(97, 122))
            self.ciphered_text += symb
            self.deciphered_text += chr((ord(symb) + self.cypher - 97) % 26 + 97)

    def Print(self):
        print("It Cyclic cipher: ciphered_text = ", self.ciphered_text, ", deciphered_text = ", self.deciphered_text,
              ". function_result = ", self.Division())
        pass

    def Write(self, ostream):
        ostream.write("It Cyclic cipher: ciphered_text = {}, deciphered_text = {}, "
                      "Division = {}".format(self.ciphered_text, self.deciphered_text, self.Division()))
        pass

    def Division(self):
        res = 0
        for x in self.deciphered_text:
            res += ord(x)
        return res / len(self.deciphered_text)
        pass
