class XShapeException(Exception): # create an exception class 
    def printError(self, errorMessage):
        print(errorMessage)
number_of_lines = int(input('Enter number of lines to print X shape: '))
try:
    if number_of_lines % 2 == 0:
        raise XShapeException  # call the exception class when try block throws error
    else:
        # Logic to draw the X shape
        print('Consider X shape is drawn')
except XShapeException as e:
    e.printError('Invalid input was given')