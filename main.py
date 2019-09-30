from classes.calculator import Calculator
from classes.reader import Reader
from classes.writer import Writer
from classes.fileReader import fileReader
from classes.fileWriter import filewriter

fr = fileReader()
fr.readInPath()
fr.doMath()