import sys
import string
import time
from extender import *

# ----------------------------------------------
from randomArray import GenerateArray

if __name__ == '__main__':
    inputFileName = "input.txt"
    outputFileName = "output.txt"
    sortOutputFileName = "sortOutput.txt"
    start_time = time.time()
    if len(sys.argv) == 5:
        inputFileName = sys.argv[2]
        outputFileName = sys.argv[3]
        sortOutputFileName = sys.argv[4]
    elif len(sys.argv) == 4:
        inputFileName = sys.argv[2]
        outputFileName = sys.argv[3]
        sortOutputFileName = "sortOutput.txt"
    elif len(sys.argv) == 3:
        inputFileName = sys.argv[2]
        outputFileName = "output.txt"
        sortOutputFileName = "sortOutput.txt"
    elif len(sys.argv) <= 2:
        print(
            "Incorrect command line! You must write: python main <inputFileName> [<outputFileName>, <sortOutputFileName>]")
        exit()
    else:
        exit()

    print('==> Start')

    container = Container()
    if sys.argv[1] == "-f":
        # Чтение исходного файла, содержащего данные, разделенные пробелами и переводами строки
        ifile = open(inputFileName)
        str = ifile.read()
        ifile.close()
        # Формирование массива строк, содержащего чистые данные в виде массива строк символов.
        strArray = str.replace("\n", " ").split(" ")
        figNum = ReadStrArray(container, strArray)
    elif sys.argv[1] == "-n":
        figNum = GenerateArray(container, int(inputFileName))
    ofile = open(outputFileName, 'w')
    container.Write(ofile)
    # Сортировка вызывается в методе Print(), либо отдельно в методе ShakerSort;
    # container.Print()
    container.ShakerSort();
    ofile = open(sortOutputFileName, 'w')
    container.Write(ofile)
    ofile.close()

    print('==> Finish')
    print("time: %s seconds" % (time.time() - start_time))
