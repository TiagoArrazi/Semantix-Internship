#Para a geração dos arquivos com a massa de dados é necessário apenas executar este script através de 'python3 DataMassGenerator_V2.py'

import csv
import string
import random as rd
import datetime

def gera_Exame(): #gerador de nome de exame aleatorio
	letras = list(string.ascii_uppercase)
	Exame = ""
	Exame = 'Exame ' + letras[rd.randint(0,25)] + letras[rd.randint(0,25)] + letras[rd.randint(0,25)] + letras[rd.randint(0,25)]
	return Exame

def gera_Medico(Nome): #gerador de nome de medico a partir de um nome aleatoriamente gerado por 'gera_Nome()'
	return 'Dr(a). ' + Nome

def gera_Expediente_Medico(): #gerador de expediente medico, pelos horários terem sido tratados como string, 
                                #possui alguns bugs a serem corrigidos
	Expdt = ""

	hora_inicio = rd.randint(0,23)
	minuto_inicio = str(rd.randint(0,59))

	hora_final = hora_inicio + rd.randint(2,4)	

	hora_inicio = str(hora_inicio)
	hora_final = str(hora_final)

	if hora_inicio == '0':

		hora_inicio += '0'

	if minuto_inicio == '0':

		minuto_inicio += '0'
	
		

	return 'Das ' + hora_inicio + ':' + minuto_inicio + ' as ' + hora_final + ':' + minuto_inicio

def gera_Nome(): #gerador de nome aleatório a partir de dois dicionários, dict_Nome{} e dict_Sobrenome

	nomeCompleto = ""

	dict_Nome = {1 : 'Abda' , 2: 'Abigail', 3 : 'Acacia', 4 : 'Adalgisa', 5 : 'Adeilce ', 6 : 'Adelaide', 7 : 'Adelia ', 
		8 : 'Adriana ', 9 : 'Agnes' , 10 : 'Aida', 11 : 'Aidee ', 12 : 'Aime ', 13 : 'Aimee', 14 : 'Aira ', 
		15 : 'Aisla', 16 : 'Alana', 17 : 'Alanis', 18 : 'Alaide', 19 : 'Alba', 20 : 'Albertina', 21 : 'Alcina',
		22 : 'Alcione', 23 : 'Aldete', 24 : 'Alecya', 25 : 'Alessandra', 26 : 'Alberico', 27 : 'Alberto', 28 : 'Alceu', 
		29 : 'Alcir', 30 : 'Aldo', 31 : 'Alencar', 32 : 'Alessandro', 33 : 'Alessio', 34 : 'Alex', 35 : 'Alexsander', 
		36 : 'Alfredo', 37 : 'Alfeu', 38 : 'Almir', 39 : 'Aluisio', 40 : 'Alvaro', 41 : 'Altamir', 42 : 'Amadeu', 
		43 : 'Amauri', 44 : 'Americo', 45 : 'Amin', 46 : 'Amancio', 47 : 'Amilcar', 48 : 'Amir', 49 : 'Amon',
		50 : 'Anat', 51 : 'Andre', 52 : 'Andrew', 53 : 'Bartira', 54 : 'Beatriz', 55 : 'Bela', 56 : 'Belinda',
		57 : 'Ayram', 58 : 'Ayrton ', 59 : 'Badia', 60 : 'Barbara', 61 : 'Beth', 62 : 'Beverly', 63 : 'Betina', 
		64 : 'Berenice', 65 : 'Bernadete', 66 : 'Berta', 67 : 'Betânia', 68 : 'Brisa', 69 : 'Bruna', 70 : 'Baldoc',
		71 : 'Bianca', 72 : 'Blanca', 73 : 'Brenda', 74 : 'Brigida', 75 : 'Brigite', 76 : 'Basilio', 77 : 'Batista',
		78 : 'Benicio', 79 : 'Benito', 80 : 'Benjamin', 81 : 'Candida', 82 : 'Camila', 83 : 'Carla', 84 : 'Carlota', 
		85 : 'Carmela', 86 : 'Carmem', 87 : 'Carol', 88 : 'Carole', 89 : 'Carolina', 90 : 'Cassandra', 91 : 'Cassia', 
		92 : 'Cassiane', 93 : 'Catarina', 94 : 'Cecile', 95 : 'Cecília', 96 : 'Celene', 97 : 'Celeste', 98 : 'Celia',
		99 : 'Carlito', 100 : 'Carlos', 101 : 'Carmelo', 102 : 'Casimiro', 103 : 'Cassio', 104 : 'Caue', 105 : 'Cecil', 
		106 : 'Célio', 107 : 'Celso', 108 : 'Cesar', 109 : 'Charles', 110 : 'Chris', 111 : 'Evelyne', 112 : 'Ed', 113 : 'Eder',
		114 : 'Edilson', 115 : 'Ediraldo', 116 : 'Edmilson', 117 : 'Ednei', 118 : 'Edson', 119 : 'Eduardo', 120 : 'Edvaldo', 
		121 : 'Eivaldo', 122 : 'Elias', 123 : 'Eliezer', 124 : 'Eliseu', 125 : 'Eloy', 126 : 'Elton', 127 : 'Emerson',
		128 : 'Igor', 129 : 'Ilario', 130 : 'Ilton', 131 : 'Inacio', 132 : 'Irineu', 133 : 'Isaac', 134 : 'Isaias',
		135 : 'Ismael', 136 : 'Israel', 137 : 'Iuri', 138 : 'Ivan', 139 : 'Ivich', 140 : 'Ivo', 141 : 'Jacilei',
		142 : 'Jade', 143 : 'Jacqueline', 144 : 'Jaimerina', 145 : 'Janaina', 146 : 'Jandineia', 147 : 'Janete', 148 : 'Janey',
		149 : 'Jaqueline', 150 : 'Jasmim', 151 : 'Odécio', 152 : 'Odherban', 153 : 'Odilon', 154 : 'Odilson', 155 : 'Odir', 
		156 : 'Odorico', 157 : 'Oduvaldo', 158 : 'Olavo', 159 : 'Arnaldinho',  160 : 'Olegario', 161 : 'Olivier', 162 : 'Onofre', 
		163 : 'Orfeu', 164 : 'Orides', 165 : 'Orlando', 166 : 'Omar', 167 : 'Oscar', 168 : 'Osias', 169 : 'Osmar'}
    


	dict_Sobrenome = {1 : 'Chaulette' , 2: 'Chaves', 3 : 'Chenicin', 4 : 'Chestian', 5 : 'Chiarello', 6 : 'Chica', 7 : 'Chiel ', 
		8 : 'Chremerv ', 9 : 'Christ' , 10 : 'Christensen', 11 : 'Christian ', 12 : 'Christina', 13 : 'Christmann', 14 : 'Christof', 
		15 : 'Christoph', 16 : 'Christov', 17 : 'Chyssus', 18 : 'Cidade', 19 : 'Alba', 20 : 'Cimbern', 21 : 'Ciola',
		22 : 'Alcione', 23 : 'Aldete', 24 : 'Alecya', 25 : 'Alessandra', 26 : 'Alberico', 27 : 'Alberto', 28 : 'Alceu', 
		29 : 'Cipriano', 30 : 'Ciqueira', 31 : 'Cironi', 32 : 'Clairton', 33 : 'Clar', 34 : 'Clarimoundo', 35 : 'Claser', 
		36 : 'Claus', 37 : 'Clausen', 38 : 'Claussen', 39 : 'Cleber', 40 : 'Fernandes', 41 : 'de Campos', 42 : 'Ferreira', 
		43 : 'de Melo', 44 : 'Ferreira', 45 : 'Severino', 46 : 'Fonseca', 47 : 'Frazao', 48 : 'Freitas', 49 : 'Gomes',
		50 : 'Correa', 51 : 'Gomes', 52 : 'Rangel', 53 : 'Bartira', 54 : 'Gonçalves', 55 : 'Campos', 56 : 'Gouvea',
		57 : 'Leme', 58 : 'Lima ', 59 : 'Badia', 60 : 'Lopes', 61 : 'Ribeiro', 62 : 'Machado', 63 : 'Dahmer', 
		64 : 'Dahse', 65 : 'Daiber', 66 : 'Daiger', 67 : 'Dainer', 68 : 'Daladeia', 69 : 'Dalateia', 70 : 'Baldoc',
		71 : 'Dalateia', 72 : 'Dalbias', 73 : 'Dalfert', 74 : 'Dalm', 75 : 'Dalms', 76 : 'Basilio', 77 : 'Batista',
		78 : 'Dalober', 79 : 'Dalpias', 80 : 'Dalpias', 81 : 'Damaceno', 82 : 'Damann', 83 : 'Damara', 84 : 'Damasceno',
		85 : 'Damazio', 86 : 'Dambach', 87 : 'Dambacher', 88 : 'Damm', 89 : 'Dammann', 90 : 'Dams', 91 : 'Damscher', 
		92 : 'Damchen', 93 : 'Damer', 94 : 'Damert', 95 : 'Damian' , 96 : 'Damiz'}

	
	nomeCompleto = dict_Nome[rd.randint(1,169)] + ' ' + dict_Sobrenome[rd.randint(1,96)]

	return nomeCompleto

                     
def gera_Idade(): # gerador de idade aleatória
	return rd.randint(1,80) 


def gera_DataNasc(idade): # gera data de nascimento de acordo com a idade gerada
	DataNasc = datetime.datetime.now()
	idade = datetime.timedelta(days = (idade*365))	

	DataNasc = DataNasc - idade

	return DataNasc.date()	
       

def gera_Endereco(): #gerador de endereço aleatório,
                     #no qual a rua, o bairro, a cidade e UF são representados por um conjunto de letras maiúsculas de 4, 3, 2, 1 caracteres, 
                     #respectivamente, além de mais um número entre 10 e 2000 para representar o número da moradia

	letras = list(string.ascii_uppercase)
	endereco_Completo = ""

	endereco_Completo = 'Rua ' + letras[rd.randint(0,25)] + letras[rd.randint(0,25)] + letras[rd.randint(0,25)] + letras[rd.randint(0,25)] 		+ ', ' + str(rd.randint(10,2000)) + ', Bairro ' + letras[rd.randint(0,25)] + letras[rd.randint(0,25)] + letras[rd.randint(0,25)] 	 + ', Cidade ' + letras[rd.randint(0,25)] + letras[rd.randint(0,25)] + ', Unidade Federativa ' + letras[rd.randint(0,25)]

	return endereco_Completo


def gera_Tel(): #gerador de número de telefone aleatório, incluido DDD
	Tel = ""
	Tel = '(' + str(rd.randint(11,99)) + ')' + str(rd.randint(1111,9999)) + '-' + str(rd.randint(1111,9999))

	return Tel


def gera_CEP(): #gerador de CEP aleatório
	CEP = ""
	CEP = str(rd.randint(11111,99999)) + '-' + str(rd.randint(111,999))

	return CEP


def gera_Convenio(): #gerador de convênio a partir de um dicionário de convênios
	dict_Conv = {1 : 'Bradesco Saude', 
		2 : 'Amil Assistencia Medica Internacional', 
		3 : 'Unimed Belo Horizonte - Cooperativa de Trabalho Medico', 
		4 : 'Central Nacional Unimed - Cooperativa Central',
		5 : 'Amico Saude',
		6 : 'Unimed RJ - Cooperativa de Trabalho Medico do Rio de Janeiro',
		7 : 'Golden Cross'}

	return dict_Conv[rd.randint(1,7)]


def gera_Data_Entrada(): #gerador de data de entrada
	Data = datetime.date(rd.randint(2000, 2018), rd.randint(1,12), rd.randint(1,28))
	return Data
 

def gera_Data_Saida(data_entrada): #gerador de data de saída de acordo com a data de entrada gerada

	tempo_estadia = datetime.timedelta(days = 10)	
	data_saida = data_entrada + tempo_estadia
	
	return data_saida 

#THC ---> Tabela Histórico Cliente
#TP ---> Tabela Paciente
#TCID ---> Tabela CID
#TM ---> Tabela Médicos


		
if __name__ == "__main__":
	delimitador = ';'

	qt_pacientes = 100000
	qt_medicos = 50000
	qt_cid = 200
	qt_dados = 10000

	THC = open('Tabela_Historico_Cliente.csv', 'w')
	TP = open('Tabela_Paciente.csv', 'w')
	TCID = open('Tabela_CID.csv', 'w')
	TM = open('Tabela_Medicos.csv', 'w')

	wr_THC = csv.writer(THC, delimiter = delimitador)
	wr_TP = csv.writer(TP, delimiter = delimitador)
	wr_TCID = csv.writer(TCID, delimiter = delimitador)
	wr_TM = csv.writer(TM, delimiter = delimitador)

	wr_THC.writerow(['ID_Cliente','Data_Entrada_Hospital','Data_Saida','Exame_Relacionado','Medico'])
	wr_TP.writerow(['ID','Nome','Idade','Data_Nascimento','Endereco','CEP','Telefone','Convenio'])
	wr_TCID.writerow(['CID','Nome exame'])
	wr_TM.writerow(['CRM','Nome_Medico','Expediente'])

	listPac = []
	for p in range(1, qt_pacientes):
		PAC = "P%08d" % p
		listPac.append(PAC)
		idade = gera_Idade()
		nome = gera_Nome()
		wr_TP.writerow([PAC, nome, idade, gera_DataNasc(idade), gera_Endereco(), gera_CEP(), gera_Tel(), gera_Convenio()])

	listCRM = []
	for m in range(1, qt_medicos):
		CRM = "%06d" % m
		listCRM.append(CRM)
		medico = gera_Medico(gera_Nome())
		wr_TM.writerow([CRM, medico, gera_Expediente_Medico()])

	listCID = []
	for a in range(ord('A'),ord('Z')+1):
		for b in range(0,100):
			CID = str(chr(a) + "%02d" % b)
			listCID.append(CID)
			wr_TCID.writerow([CID, gera_Exame()])


	for r in range(1, qt_dados):
		k1 = rd.randint(1,len(listPac)-1)
		k2 = rd.randint(1,len(listCRM)-1)
		k3 = rd.randint(1,len(listCID)-1)
		data = gera_Data_Entrada()
		wr_THC.writerow([listPac[k1], data, gera_Data_Saida(data), listCID[k3], listCRM[k2]])

	THC.close()
	TP.close()
	TCID.close()
	TM.close()
