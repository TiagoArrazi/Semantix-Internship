#!/usr/bin/env python3

import sys #módulo para realizar captura de parâmetros na linha de comando
import re #módulo pra utilizar métodos de expressões regulares 

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

    result = re.sub('x', '*', argString) #caso um dos elementos da string capturada seja 'x', o programa irá substituir por '*' para realizar 						  uma operação válida

    try:

        if argString == "":
      
            return '------#Empty Space#------' #retorna essa mensagem se a string estiver vazia

        else:

            return eval(result) #utilizando a função 'eval(str)', é possível realizar uma operação matemática a partir de uma string

    except ZeroDivisionError:

        return 'Zero Division Error' #captura uma exceção em caso de divisão por 0

    except NameError:

        return 'Name Error' #captura uma exceção em caso de parâmetros inválidos

    except SyntaxError:

        return 'Syntax Error' #captura uma exceção em caso de síntaxe inválida

#==========================================================================

def main():

    argString = "" #essa string receberá os parâmetros do programa

    inputArgs = sys.argv[1:] #essa variável recebe diretamente uma slice da lista argv[]

    for arg in inputArgs:
        argString += arg #argString recebe um elemento de inputArgs a cada iteração

    operate(argString) 
