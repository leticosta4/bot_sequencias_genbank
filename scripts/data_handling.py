#tratando a string com o numero de sequencias baixadas
def get_num_seq(string_seq_num):
    numseq = ""
    for i in string_seq_num:
        if i in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            numseq += i
    return numseq

#pode mudar a lógica de divisão dos tempos se for melhor para cada arbovírus
def arbov_time(op):
    if op == 0:
        return 500 #denv1
    elif op == 1 or op == 6:
        return 400 #denv2 e zikv
    elif op == 3 or op == 4:
        return 300 #denv 3 e denv4 - esse tempo ainda tá meio grande: tentar regular entre 120 e 300
    else:
        return 200 #chikv