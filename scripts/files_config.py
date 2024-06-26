import os

def download_verification():
    expected_file = "sequence.gbc.xml"
    if os.path.exists(os.path.join("downloaded_sequences/", expected_file)):
        print(f"Arquivo '{expected_file}' baixado com sucesso!")
    else:
        print(f"Erro: Arquivo '{expected_file}' não encontrado no diretório de download.")


def prepare_directories():
    path = 'downloaded_sequences/'
    
    try:
        os.makedirs(path)
        print(f"O diretório {path} foi criado com sucesso.")
    except FileExistsError:
        print(f"O diretório {path} já existe!")
    except Exception as err:
        print(f"Erro ao criar o diretório {path}: {err}")