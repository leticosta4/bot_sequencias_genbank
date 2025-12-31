import streamlit as st
import time
from scripts.setup import arbovirus_search
from scripts.files_config import prepare_directories, gerar_txt_content, download_verification

def prepare_files_for_user_download(virus_name: str, file_type: str, **kwargs):
    prefix = virus_name.replace(' ', '-')
    
    match(file_type.lower()):
        case "xml":
            kwargs.clear() # ver como limpar

            with open("output/sequence.gbc.xml", "r") as file:
                xml_content = file.read()
                st.download_button(
                    label="Faça o download da sequência viral XML",
                    data=xml_content,
                    file_name=f"{prefix}-sequence.xml",
                    mime="application/xml",
                    type="primary",
                    icon="📥"
                )
        case "txt":
            content = gerar_txt_content(virus_name, kwargs.get("downloaded_sequences"), kwargs.get("downloads_duration"))
            st.download_button(
                label="Faça o download de um arquivo txt com as informações gerais sobre sua busca",
                data=content,
                file_name=f"{prefix}-seq-download-info.txt",
                mime="text/plain"
            )
        case _:
            pass
    
    

arbovirus_list = ['dengue virus type 1', 'dengue virus type 2', 'dengue virus type 3', 'dengue virus type 4', 'chikungunya virus', 'zika virus', "oropouche virus"]

st.set_page_config(
    page_title="bot download XML",
    layout="wide"
)

st.title("Bot de Downlaod de Sequências Virais XML de Arboviroses")


chosen_virus = st.selectbox(
    'Escolha o arbovírus cujas sequencias deseja fazer o download',
    options=arbovirus_list,
    index=None)

if chosen_virus:
    if st.button("Confirmar seleção"):
        st.success(f"iniciando download para o {chosen_virus}")

        arbovirus = chosen_virus.replace(' ', '+')
        absolute_path = prepare_directories()

        begin_time = time.time()
        seq_num = arbovirus_search(arbovirus, absolute_path)

        while(True):
            # a cada 3 segundos vai verificar se o download dos arquivos encerrou ('sequence.gbc.xml' no output)
            time.sleep(3)
            if download_verification():
                st.success("download concluido")
                #acabou
                #exibe arquivo para download
                downloaded_sequences = ''.join([c for c in seq_num if c.isdigit()])
                break
                        
        end_time = time.time()

        prepare_files_for_user_download(chosen_virus, "xml")

        downloads_duration = end_time - begin_time

        if downloaded_sequences != -1:
            prepare_files_for_user_download(chosen_virus, "txt", downloaded_sequences, downloads_duration)

        else: 
            #talvez fazer uma verificação de timeout ou colocar em um try-catch
            st.write("Arquivo de informações não gerado devido a problema no download da sequência")


#carregamento
#associar opção escolhida para a logica de download
#coisa de arquivo gerado do xml
#printar informações 



#coisa do tempo
# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#   # Update the progress bar with each iteration.
#   latest_iteration.text(f'Iteration {i+1}')
#   bar.progress(i + 1)
#   time.sleep(0.1)

# '...and now we\'re done!'


