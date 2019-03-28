#Feito em Python 3 e ambiente Linux Ubuntu 18.04 LTS
# Autores: Tiago Costa Arrazi & Guilherme Coelho Small Zicari

from os import path


def convert(target, _format='bin'):  # conversor de binário para char
    if _format == 'bin':
        return str(chr(int(target, 2)))
    else:
        return target


if __name__ == '__main__':

    Matrix = [['_' for x in range(32)] for y in range(1024)]  # cria matriz que armazenará o estado inicial do HD

    if path.isfile('VHD.txt'):  # verifica se o arquivo VHD.txt já existe
        with open('VHD.txt', 'r') as f:
            Matrix = [[element for element in list(line)] for line in f]  # atualiza a matriz de acordo com o arquivo
            
    else:  # se não existir
        with open('VHD.txt', 'w+') as f:
            for i in range(1024):
                for j in range(32):
                    f.write(Matrix[i][j])  # preenche o arquivo com a matriz inicial
                f.write('\n')  # quebra de linha para melhor visualização dos blocos

    user_input = input('Insert data type (bin/char): ')  # pede pela entrada do usuário (binário ou caracter)

    if user_input == 'bin':
        bin_input = input('Insert bit sequence: ')  # inserção da sequência de bits
        block = int(input('Choose block (1 - 1024): '))  # inserção do bloco no qual deve ser salvo
        byte = int(input('Choose byte (1 - 32): '))  # inserção do byte no qual deve ser salvo

        Matrix[block - 1][byte - 1] = convert(bin_input)  # a matriz recebe o valor inserido pelo usuário

        with open('VHD.txt', 'w+') as f:
    
            for i in range(1024):
                for j in range(32):
                    f.write(Matrix[i][j])  # atualiza o arquivo
                f.write('\n')

    elif user_input == 'char':
        char_input = input('Insert character: ')  # inserção do caracter
        block = int(input('Choose block (1 - 1024): '))  # inserção do bloco no qual deve ser salvo
        byte = int(input('Choose byte (1 - 32): '))  # inserção do byte no qual deve ser salvo

        Matrix[block - 1][byte - 1] = convert(char_input, 'char')  # a matriz recebe o valor inserido pelo usuário

        with open('VHD.txt', 'w+') as f:

            for i in range(1024):
                for j in range(32):
                    f.write(Matrix[i][j])  # atualiza o arquivo
                f.write('\n')

    else:
        print('Invalid input!')
        exit(-1)



    

            




            

