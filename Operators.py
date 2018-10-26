import sys
import re

#===================================================================================

def factorial(n):

    if n >= 1:

        return n * factorial(n - 1)

    else:

        return 1

def fibonacci(n):

    if n == 0:

        return 0

    elif n == 1 or n == 2:

        return 1

    else:

        return (fibonacci(n - 2) + fibonacci(n - 1))

#=====================================================================================

def operate(argString):

    result = re.sub('x', '*', argString)

    try:

        if argString == "":
      
            return '------#Empty Space#------'

        else:

            return eval(result)

    except ZeroDivisionError:

        return 'Zero Division Error'

    except NameError:

        return 'Name Error'

    except SyntaxError:

        return 'Syntax Error'

#==========================================================================

def main():

    argString = ""

    inputArgs = sys.argv[1:]

    for arg in inputArgs:
        argString += arg

    operate(argString)
