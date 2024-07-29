import os
from datetime import date, datetime

def download_verification():
    expected_file = "sequence.gbc.xml"
    if os.path.exists(os.path.join("output/", expected_file)):
        print(f"Arquivo '{expected_file}' baixado com sucesso!")
    else:
        print(f"Erro: Arquivo '{expected_file}' não encontrado no diretório de download.")


def prepare_directories():
    path = 'output/'
    
    try:
        os.makedirs(path)
        print(f"O diretório {path} foi criado com sucesso.")
    
    except FileExistsError:
        print(f"O diretório {path} já existe!")
    except Exception as err:
        print(f"Erro ao criar o diretório {path}: {err}")

    return os.path.abspath(path)

def gerar_txt(arbovirus, seq_amount):
    with open("output/output_info.txt", "w") as file_to_download: 
        header = "Informações gerais do download\n"
        today = date.today().strftime('%d/%m/%Y')
        day_time = f"Dia de download das sequências: {today}\n"
        moment = f"Horário: {datetime.now().strftime('%H:%M:%S')}\n"
        query = f"Arbovírus selecionado pelo usuário para download das sequências: {arbovirus}\n"
        num = f"Número de sequências encontradas para {arbovirus}: {seq_amount}\n"
        source = f"Fonte: Genbank, Nucleotide database"
        file_to_download.write(header + day_time + moment + query + num + source)
        file_to_download.close()