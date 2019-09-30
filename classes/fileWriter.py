import os

class filewriter:
    """Writes the result into file
    """
    InitMessage = '*** Write output file name'
    FilePath = ''
    message = True
    errorMessage = '*** The expression was not calculated succsesfully'
    def __init__(self, result, message, filePath):
        self.result = result
        self.message = message
        self.FilePath = filePath
    def openFile(self):
        print(self.InitMessage)
        print('>>> ', end='')
        self.FilePath = input()
        if (self.FilePath == ''):
            self.FilePath = 'output.txt'
        return self.FilePath
    def printResult(self):
        if (not os.path.isfile(self.FilePath)):
            f = open(self.FilePath, 'w+')
        f = open(self.FilePath, 'a')
        if (self.message == False):
            f.write('%s %d\n' % ('*** The result is:', self.result))
        else:
            print(self.errorMessage + '\n')
        f.close()