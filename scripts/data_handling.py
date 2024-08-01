#tratando a string com o numero de sequencias baixadas
def get_num_seq(string_seq_num):
    numseq = ""
    for i in string_seq_num:
        if i in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            numseq += i
    return numseq

def arbov_time(op):
    if op == 0:
        return 500 #denv1
    elif op == 1 or op == 6:
        return 200 #denv2 e zikv
    elif op == 3 or op == 4:
        return 120 #denv 3 e denv4
    else:
        return 160 #chikv