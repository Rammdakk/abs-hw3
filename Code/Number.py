import sys

from cyphers import *
from random import randint


# ----------------------------------------------
class Number(Cyphers):
    def __init__(self):
        self.length = 0
        self.cypher = [[], []]
        self.ciphered_text = []
        self.deciphered_text = ""

    def cipheredTextToString(self=None):
        str1 = " "
        for x in self.ciphered_text:
            str1 += str(x)
        return str1

    def ReadStrArray(self, strArray, i):
        # должно быть как минимум три непрочитанных значения в массиве
        if i >= len(strArray) - 2:
            return 0
        self.length = int(strArray[i])
        i += 1
        x = 0
        while x < self.length:
            self.ciphered_text.append(int(strArray[i]))
            i += 1
            x += 1
        x = 0
        while x < self.length:
            self.cypher[0].append(ord(strArray[i]))
            self.cypher[1].append(int(strArray[i + 1]))
            i += 2
            x += 1
        for x in self.ciphered_text:
            for j in range(self.length):
                if x == self.cypher[1][j]:
                    self.deciphered_text += chr(self.cypher[0][j])
        return i

    def RandomGenerate(self):
        self.length = randint(12, 20)
        for i in range(self.length):
            k = randint(1, 10) * randint(1, 10)
            self.ciphered_text.append(k)
            self.cypher[1].append(k)
            k = randint(97, 122)
            self.deciphered_text += chr(k)
            self.cypher[0].append(k)

    def Print(self):
        print("It Number cipher: ciphered_text = ", self.cipheredTextToString(), ", deciphered_text = ",
              self.deciphered_text,
              ". Function_result = ", self.Division())
        pass

    def Write(self, ostream):
        ostream.write("It Number cipher: ciphered_text = {}, deciphered_text = {}, function_result = {}".format(
            self.cipheredTextToString(), self.deciphered_text, self.Division()))
        pass

    def Division(self):
        res = 0
        for x in self.deciphered_text:
            res += ord(x)
        return res / len(self.deciphered_text)
        pass
