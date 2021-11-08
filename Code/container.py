# ----------------------------------------------
class Container:
    def __init__(self):
        self.store = []

    # def ReadStrArray(self, strArray):

    def Print(self):
        print("Container is store", len(self.store), "elements:")
        i = 0
        for shape in self.store:
            print(i, sep='', end=': ')
            i += 1
            shape.Print()
        print()
        print("Sorted Version:")
        self.ShakerSort()
        i = 0
        for shape in self.store:
            print(i, sep='', end=': ')
            i += 1
            shape.Print()
        pass

    def Write(self, ostream):
        ostream.write("Container is store {} elements:\n".format(len(self.store)))
        i = 0
        for shape in self.store:
            ostream.write(str(i) + ": ")
            shape.Write(ostream)
            ostream.write("\n")
            i += 1
        pass

    def ShakerSort(self):
        control = len(self.store) - 1
        left = 0
        right = control
        while True:
            for x in range(left, right):
                if self.store[x].Division() > self.store[x + 1].Division():
                    ch = self.store[x + 1]
                    self.store[x + 1] = self.store[x]
                    self.store[x] = ch
                    control = x
            right = control
            for x in range(right, left, -1):
                if self.store[x].Division() < self.store[x - 1].Division():
                    ch = self.store[x - 1]
                    self.store[x - 1] = self.store[x]
                    self.store[x] = ch
                    control = x
            left = control
            if left >= right:
                break
