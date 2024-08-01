from scripts.setup import arbovirus_search
from scripts.files_config import prepare_directories, gerar_txt
from scripts.data_handling import arbov_time

seq_amount = 0
lista_arbovirus = ['dengue virus type 1', 'dengue virus type 2', 'dengue virus type 3', 'dengue virus type 4', 'chikungunya virus', 'zika virus']

for i in range(len(lista_arbovirus)): 
    print(f"{i+1} - {lista_arbovirus[i]} ")

op = 1
while(True):
    op = int(input("\nveja a lista acima e escolha o arbovírus cujas sequencias deseja fazer o download (para sair digite 7) >> "))
    if op > 7 or op < 1:
        print("o valor inserido deve ser de 1 a 7. Tente novamente\n")
    elif op == 7:
        print("\n\nvoce cancelou o funcionamento do bot.")
        break 
    else:
        arbovirus = lista_arbovirus[op-1].replace(' ', '+')
        sleep_time = arbov_time(op-1)
     
        absolute_path = prepare_directories()

        seq_amount = arbovirus_search(arbovirus, absolute_path, sleep_time)
        if(seq_amount != -1): gerar_txt(lista_arbovirus[op-1], seq_amount)
        else: print("Arquivo de informações não gerado devido a problema no download da sequência")
        break

