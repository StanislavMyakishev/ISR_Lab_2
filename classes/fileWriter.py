class filewriter:
    InitMessage = '*** Write file name'
    FilePath = ''
    message = True
    errorMessage = '*** The expression was not calculated succsesfully'
    def __init__(self, result, message):
        self.result = result
        self.message = message
    def openFile(self):
        print(self.InitMessage)
        print('>>> ', end='')
        self.FilePath = input()
    def printResult(self):
        if (self.FilePath == ''):
            self.FilePath = 'output.txt'
        f = open(self.FilePath, 'w')
        if (self.message == False):
            f.write('%s %d\n' % ('*** The result is:', self.result))
        else:
            print(self.errorMessage + '\n')