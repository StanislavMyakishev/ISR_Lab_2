#class Writer
# __init__ - gets numerical result and boolean if there is error 
# printResult - prints result if there is no error message
class Writer:
    """"[summary]
    
    Returns:
        [type] -- [description]
    """
    result = 0
    err = True
    message = True
    errorMessage = '*** The expression was not calculated succsesfully'
    def __init__(self, result, message):
        self.result = result
        self.message = message
    def printResult(self):
        if (self.message == False):
            print('%s\n*** %d' % ('*** The result is:', self.result))
            return True
        else:
            print(self.errorMessage)
            return self.errorMessage