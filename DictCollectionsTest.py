from collections import defaultdict

list_id = [12123434,55466576,23178976,95032543]
list_area = [50,60,70,80]
list_tipo = ["Apartamento","Casa","Escritorio","Fazenda"]
list_aluguel = [500,700,1700,2000]

dict_master = defaultdict(dict)

for i in range(0,len(list_id)):

    dict_master[list_id[i]]["tipo"] = list_tipo[i]
    dict_master[list_id[i]]["area"] = list_area[i]
    dict_master[list_id[i]]["aluguel"] = list_aluguel[i]

print(dict_master)
