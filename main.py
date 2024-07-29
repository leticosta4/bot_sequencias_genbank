from scripts.setup import arbovirus_search
from scripts.files_config import prepare_directories, gerar_txt

seq_amount = 0
lista_arbovirus = ['dengue virus type 1', 'dengue virus type 2', 'dengue virus type 3', 'dengue virus type 4', 'chikungunya virus', 'zika virus']

for i in range(len(lista_arbovirus)): 
    print(f"{i+1} - {lista_arbovirus[i]} ")

op = int(input("\nveja a lista acima e escolha o arbovírus cujas sequencias deseja fazer o download >> "))
arbovirus = lista_arbovirus[op-1].replace(' ', '+')

absolute_path = prepare_directories()
seq_amount = arbovirus_search(arbovirus, absolute_path)
gerar_txt(lista_arbovirus[op-1], seq_amount)
