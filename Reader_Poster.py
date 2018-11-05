import csv #módulo importado para uso de CSV
import sys #módulo para captura de parâmetros na linha de comando
import os #módulo para executar linhas de comando do Linux via Python
import re

def kiloParser(byteString):

    newByteString = byteString.replace("K","")
    floatByteString = float(newByteString)

    floatByteString *= 1024

    return floatByteString


def megaParser(byteString):

    newByteString = byteString.replace("M","")
    floatByteString = float(newByteString)

    floatByteString *= 1024**2
    
    return floatByteString


def gigaParser(byteString):

    floatByteString = byteString.replace("G","")
    floatByteString = float(newByteString)

    floatByteString *= 1024**3

    return floatByteString


def byteParser(byteString):
    
    byteString = re.sub(',' ,'.' , byteString)

    byteDict = {'K' : kiloParser,
                'M' : megaParser,
                'G' : gigaParser}

    try:
    
       newByteString = byteDict[byteString[-1]](byteString)
       return newByteString

    except KeyError:

        return byteString


def Reader_Poster(filename):

    count = 0

    with open(filename) as f: #abre arquivo com o nome em argv[1]

        with open('CSV_file.csv', 'w') as myCSV: #cria novo arquivo .csv

            wr = csv.writer(myCSV, delimiter = ',')
            wr.writerow(['Nome do arquivo', 'Data', 'Hora', 'Tamanho', 'permOwn', 'permGrp', 'permOth']) #escreve cabeçalho do CSV

            for line in f:

                line  = line.split() #separa linha do arquivo por espaços em branco

                if line[0][0] == '-': #lê apenas arquivos, não diretórios                

                    wr.writerow([line[8], dateParser(line[5]), line[6][:8], byteParser(line[4]), permParser(line[0][1:4]),
                        permParser(line[0][4:7]), permParser(line[0][7:10])]) #escreve linha no CSV

                    count += 1

            print(count)

        myCSV.close()

    f.close()


def dateParser(dateString): #conversor de formato de datas

    newDateString = dateString[8:10] + '/' + dateString[5:7] + '/' + dateString[:4] #utilza slicing para acessar partes específicas da string

    return newDateString

def permParser(permString): #conversor de nome de permissões de arquivos

    permDict = {'rwx':'ALL', #é utilizado um dicionário para acessar as devidas strings correspondentes
                '-wx':'WRITE_EXECUTE',
                'r-x':'READ_EXECUTE',
                'rw-':'READ_WRITE',
                'r--':'READ',
                '-w-':'WRITE',
                '--x':'EXECUTE',
                'rws': 'SUID'}

    return permDict[permString]
    
if __name__ == "__main__":

    Reader_Poster(sys.argv[1]) 









