import csv #módulo importado para uso de CSV

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
    
def main():

    with open('list.txt') as f: #abre arquivo list.txt

        with open('CSV_file.csv', 'w') as myCSV: #cria novo arquivo .csv

            wr = csv.writer(myCSV, delimiter = ',')
            wr.writerow(['Nome do arquivo', 'Data', 'Hora', 'Tamanho', 'permOwn', 'permGrp', 'permOth']) #escreve cabeçalho do CSV

            for line in f:

                line  = line.split() #separa linha do arquivo por espaços em branco

                if line[0][0] == '-': #lê apenas arquivos, não diretórios                

                    wr.writerow([line[8], dateParser(line[5]), line[6][:8], line[4], permParser(line[0][1:4]),
                        permParser(line[0][4:7]), permParser(line[0][7:10])]) #escreve linha no CSV


                    

main()
