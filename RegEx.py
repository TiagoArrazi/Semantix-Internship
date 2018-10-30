import re #módulo para a utilzação de expressões regulares
import sys #módulo para capturar parâmetros diretamente do terminal

regex = re.compile('.+:.(\w+).+:.(\w+).+:.(\w+).+') #compila a string para aumentar performance

with open(sys.argv[1]) as f: #abre arquivo e associa à variável f

	for line in f: #itera sobre as linhas do arquivo

		m = regex.match(line) #identifica padrões em cada linha
		print(m.group(1,2,3)) #mostra os grupos 1, 2 e 3 de cada linha

