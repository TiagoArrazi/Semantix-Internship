import csv #módulo importado para uso de CSV

def dateParser(dateString): #conversor de formato de datas

    newDateString = dateString[8:10] + '/' + dateString[5:7] + '/' + dateString[:4] #utilza slicing para acessar partes específicas da string

    return newDateString

def permParser(permString): #conversor de nome de permissões de arquivos

    if permString == 'rwx': 

        return 'ALL' #troca nome da permissão

    elif permString == 'rws':

        return 'SUID'

    elif permString == '-wx':

        return 'WRITE_EXECUTE'

    elif permString == 'r-x':

        return 'READ_EXECUTE'

    elif permString == 'rw-':

        return 'READ_WRITE'

    elif permString == 'r--':

        return 'READ'

    elif permString == '-w-':

        return 'WRITE'

    elif permString == '--x':

        return 'EXECUTE'

    elif permString == '---':

        return 'None'

    
def main():

    with open('list.txt') as f: #abre arquivo list.txt

        with open('CSV_file.csv', 'w') as myCSV: #cria novo arquivo .csv

            wr = csv.writer(myCSV, delimiter = ',')
            wr.writerow(['Nome do arquivo', 'Data', 'Hora', 'Tamanho', 'permOwn', 'permGrp', 'permOth']) #escreve cabeçalho do CSV

            for line in f:

                line  = line.split() #separa linha do arquivo por espaços em branco

                if line[0][0] == '-': #apenas leituras de arquivos, não diretórios                

                    wr.writerow([line[8], dateParser(line[5]), line[6][:8], line[4], permParser(line[0][1:4]),
                        permParser(line[0][4:7]), permParser(line[0][7:10])]) #escreve linha no CSV


                    

main()
