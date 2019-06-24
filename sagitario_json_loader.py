#!/usr/bin/env python
# coding: utf-8

# In[14]:


from json import load, JSONDecodeError
from re import sub

with open('FolhaMaio.json', 'r', encoding='utf-8-sig') as json_file:
    try:
        folha = load(json_file)
        
        for i in range(1, len(folha.keys()) + 1):
            
            for element in folha['{}'.format(i)].keys():

                if not isinstance(folha['{}'.format(i)][element], list):
                    for sec_elem in folha['{}'.format(i)]['{}'.format(element)].keys():
                        if element == 'ResumoTrabalhador':
                            if len(folha['{}'.format(i)][element][sec_elem]) > 0:
                                print('{}: {}'.format(sub(':', '', sec_elem) ,folha['{}'.format(i)][element][sec_elem]))
                        
                            else:
                                print('{}: None'.format(sub(':', '', sec_elem)))
                        
                        if element == 'ResumoHoras':
                            if len(folha['{}'.format(i)][element][sec_elem]) > 0:
                                print('{}: {}'.format(sub(':', '', sec_elem) ,folha['{}'.format(i)][element][sec_elem][0][1]))
                            
                            else:
                                print('{}: None'.format(sub(':', '', sec_elem)))
                            
                    print('\n')

                else:
                    print('Batidas\n')
                    for j in range(len(folha['{}'.format(i)][element])):
                        print('== {} =='.format(folha['{}'.format(i)][element][j]['Dia']))
                        
                        flag_1 = False
                        flag_2 = False
                        pos_1 = 0
                        pos_2 = 0
                        for k in folha['{}'.format(i)][element][j]['Batida']:
                            
                            if k == 'Trabalhadas:':
                                pos_1 = folha['{}'.format(i)][element][j]['Batida'].index(k) + 1
                                flag_1 = True
                                
                            if k == 'HORAS:':
                                pos_2 = folha['{}'.format(i)][element][j]['Batida'].index(k) + 1
                                flag_2 = True
                                
                            if not flag_1:
                                print('   {}   '.format(k))
                        
                        print('Horas Trabalhadas: {}'.format(folha['{}'.format(i)][element][j]['Batida'][pos_1]))
                        
                        if len(folha['{}'.format(i)][element][j]['Batida']) > 2 and                         'HORAS:' in folha['{}'.format(i)][element][j]['Batida']:
                            print('Banco de Horas: {}'.format(folha['{}'.format(i)][element][j]['Batida'][pos_2]))
                            
                        print('\n')


    except JSONDecodeError as e:
        print("[ERROR] JSON couldn't be loaded")
        print("        {}".format(e))

