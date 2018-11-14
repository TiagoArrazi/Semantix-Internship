#!/usr/bin/env python3

import unittest #módulo para realizar teste unitário de funções
from Operators import *

class Test_Operators(unittest.TestCase):

    def test_operate(self):

        self.assertEqual(operate('1+1'), 2) # self.assertEqual() recebe 2 parâmetros, a função com os parâmetros de entrada e a saída esperada
        self.assertEqual(operate('1 +1'), 2)
        self.assertEqual(operate('1+ 1'), 2)
        self.assertEqual(operate('1 + 1'), 2)
        self.assertEqual(operate('+ 1'), 1)
        self.assertEqual(operate('+1'), 1)
        self.assertEqual(operate('2 x 2'), 4)
        self.assertEqual(operate('2 x 2 x 2'), 8)
        self.assertEqual(operate('1 + '), 'Syntax Error')
        self.assertEqual(operate('1/0'), 'Zero Division Error')
        self.assertEqual(operate('a+1'), 'Name Error')
        self.assertEqual(operate('factorial(10)'), 3628800)
        self.assertEqual(operate('factorial(a)'), 'Name Error')
        self.assertEqual(operate('fibonacci(10)'), 55)
        self.assertEqual(operate('fibonacci(a)'), 'Name Error')
        self.assertEqual(operate(''),'------#Empty Space#------' )

        
unittest.main()
