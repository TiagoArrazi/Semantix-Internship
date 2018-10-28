import re #módulo para a utilzação de expressões regulares
import sys #módulo para capturar parâmetros diretamente do terminal

regex = re.compile('.+..:.(\w+).+:.(\w+).+.:.(\w+).+')

matchString = ""

with open(sys.argv[1]) as f:

    for line in f:

        m = regex.match(line)
        print(m.group(1,2,3))



