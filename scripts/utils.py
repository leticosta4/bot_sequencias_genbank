import os
import shutil
from datetime import date, datetime
from constants import TEMP_OUTPUT_PATH

def download_verification():
    expected_file = "sequence.gbc.xml"
    if os.path.exists(os.path.join("output/", expected_file)):
        print(f"Arquivo '{expected_file}' baixado com sucesso!")
        return True


def prepare_directories():
    try:
        os.makedirs(TEMP_OUTPUT_PATH)
        print(f"O diretório {TEMP_OUTPUT_PATH} foi criado com sucesso.")
    
    except FileExistsError:
        print(f"O diretório {TEMP_OUTPUT_PATH} já existe!")
    except Exception as err:
        print(f"Erro ao criar o diretório {TEMP_OUTPUT_PATH}: {err}")

    return os.path.abspath(TEMP_OUTPUT_PATH)


def clean_temp_output_folder():
    if os.path.exists(TEMP_OUTPUT_PATH):
        shutil.rmtree(TEMP_OUTPUT_PATH)
        print(f"Pasta '{TEMP_OUTPUT_PATH}' e todo o seu conteúdo deletados.")
    else:
        print(f"A pasta '{TEMP_OUTPUT_PATH}' não foi encontrada.")



def gerar_txt_content(arbovirus, seq_amount, duration):
    header = "Informações gerais do download\n"
    today = date.today().strftime('%d/%m/%Y')
    day_time = f"Dia de download das sequências: {today}\n"
    moment = f"Horário: {datetime.now().strftime('%H:%M:%S')}\n"
    duration_downloads = f"Duração dos downloads: {duration:.0f} segundos\n"
    query = f"Arbovírus selecionado pelo usuário para download das sequências: {arbovirus}\n"
    num = f"Número de sequências encontradas para {arbovirus}: {seq_amount}\n"
    source = f"Fonte: Genbank, Nucleotide database"

    info_summarized = header + day_time + moment + duration_downloads + query + num + source

    return info_summarized


def prepare_files_for_user_download(arbovirus_name: str, file_type: str, **kwargs):
    prefix = arbovirus_name.replace(' ', '-')
    
    match(file_type.lower()):
        case "xml":
            kwargs.clear() # ver como limpar

            with open("output/sequence.gbc.xml", "r") as file:
                content = file.read()

                return {
                    "label": "Faça o download da sequência viral XML",
                    "data": content,
                    "file_name":f"{prefix}-sequence.xml",
                    "mime":"application/xml",
                }

        case "txt":
            content = gerar_txt_content(arbovirus_name, kwargs.get("amount", 0), kwargs.get("download_duration", 0.0))
           
            return {
                "label": "Faça o download de um arquivo txt com as informações gerais sobre sua busca",
                "data": content,
                "file_name":f"{prefix}-seq-info.txt",
                "mime":"text/plain",
            }
        case _:
            return None
            