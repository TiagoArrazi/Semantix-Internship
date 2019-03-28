# Feito em Python 3 e ambiente Linux Ubuntu 18.04 LTS
# Autores: Tiago Costa Arrazi & Guilherme Coelho Small Zicari

from os import path


def convert(target, _format='bin'):  # conversor de binário para char
    if _format == 'bin':
        return str(chr(int(target, 2)))
    else:
        return target


def insert():

    user_input = input('VHD> Insert data type (bin/char/string): ')  # pede pela entrada do usuário (binário ou caracter)

    if user_input == 'bin':
        bin_input = input('VHD> Insert bit sequence: ')  # inserção da sequência de bits
        block = int(input('VHD> Choose block (0 - 1023): '))  # inserção do bloco no qual deve ser salvo
        byte = int(input('VHD> Choose byte (0 - 31): '))  # inserção do byte no qual deve ser salvo

        Matrix[block][byte] = convert(bin_input)  # a matriz recebe o valor inserido pelo usuário

        with open('VHD.txt', 'w+') as f:

            for i in range(1024):
                for j in range(32):
                    f.write(Matrix[i][j])  # atualiza o arquivo
                f.write('\n')

    elif user_input == 'char':
        char_input = input('VHD> Insert character: ')  # inserção do caracter
        block = int(input('VHD> Choose block (0 - 1023): '))  # inserção do bloco no qual deve ser salvo
        byte = int(input('VHD> Choose byte (0 - 31): '))  # inserção do byte no qual deve ser salvo

        Matrix[block][byte] = convert(char_input, 'char')  # a matriz recebe o valor inserido pelo usuário

        with open('VHD.txt', 'w+') as f:

            for i in range(1024):
                for j in range(32):
                    f.write(Matrix[i][j])  # atualiza o arquivo
                f.write('\n')

    elif user_input == 'string':
        str_input = input('VHD> Insert string: ')
        block = int(input('VHD> Choose block (0 - 1023): '))
        byte = int(input('VHD> Choose starting byte (0 - 31): '))

        for i in range(len(str_input)):
            if byte <= 31:
                Matrix[block][byte] = str_input[i]
                byte += 1
            else:
                byte = 0
                block += 1

        with open('VHD.txt', 'w+') as f:

            for i in range(1024):
                for j in range(32):
                    f.write(Matrix[i][j])  # atualiza o arquivo
                f.write('\n')


def delete():
    block = int(input('VHD> Choose block (0 - 1023): '))  # inserção do bloco no qual deve ser salvo
    byte = int(input('VHD> Choose byte (0 - 31): '))  # inserção do byte no qual deve ser salvo

    Matrix[block][byte] = '_'  # a matriz recebe o valor inserido pelo usuário

    with open('VHD.txt', 'w+') as f:

        for i in range(1024):
            for j in range(32):
                f.write(Matrix[i][j])  # atualiza o arquivo
            f.write('\n')


def typehd():
    # [[print([f'Block {Matrix.index(row)}', f'Byte {row.index(element)}', element, f"0x{element.encode('utf-8').hex()}"])
    #  for element in row if element not in [' ', '_', '\n']]
    #  for row in Matrix]

    for row in Matrix:
        print(Matrix.index(row))
        _data = [element for element in row]
        _hex = [element.encode('utf-8').hex() for element in row]
        print(' '.join(_data))
        print(' '.join(_hex))



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
    while 1:

        shell = input('VHD> ')

        if shell == 'insert':
            insert()
        elif shell == 'delete':
            delete()
        elif shell == 'typehd':
            typehd()
        else:
            print('Invalid command!')





    

            




            

