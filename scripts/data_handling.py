#tratando a string com o numero de sequencias baixadas
def get_num_seq(string_seq_num):
    numseq = ""
    for i in string_seq_num:
        if i in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            numseq += i
    return numseq 

#a antiga função arbov time foi retirada porque não precisava de tempo específico para cada arbovírus
