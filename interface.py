import streamlit as st
import time
from scripts.setup import arbovirus_search
from scripts.files_config import prepare_directories, prepare_files_for_user_download

def set_confirmed():
    st.session_state.confirmed = True

arbovirus_list = ['dengue virus type 1', 'dengue virus type 2', 'dengue virus type 3', 'dengue virus type 4', 'chikungunya virus', 'zika virus', "oropouche virus"]

if 'confirmed' not in st.session_state:
    st.session_state.confirmed = False

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
    if not st.session_state.confirmed:
        st.button("Confirmar seleção", on_click=set_confirmed)

    if st.session_state.confirmed:
        st.success(f"iniciando download para o {chosen_virus}")

        arbovirus = chosen_virus.replace(' ', '+')
        absolute_path = prepare_directories()

        begin_time = time.time()
        amount = arbovirus_search(arbovirus, absolute_path)
                        
        end_time = time.time()
        st.success("download concluido")

        xml_data = prepare_files_for_user_download(arbovirus_name=chosen_virus, file_type="xml")
        st.download_button(
            label=xml_data["label"],
            data=xml_data["data"],
            file_name=xml_data["file_name"],
            mime=xml_data["mime"],
            icon="📥"
        )

        downloads_duration = end_time - begin_time

        if amount != -1:
            txt_data = prepare_files_for_user_download(arbovirus_name=chosen_virus, file_type="txt", amount=amount, downloads_duration=downloads_duration)
            st.download_button(
                label=txt_data["label"],
                data=txt_data["data"],
                file_name=txt_data["file_name"],
                mime=txt_data["mime"],
                icon="📥"
            )

        #talvez algo pra joogar fora os 2 arquivos baixados do output
        #fechar
        #botao de pedir outro dowload = limpa os dados

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


