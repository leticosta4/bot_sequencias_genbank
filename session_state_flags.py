import streamlit as st

def set_init_flags():
    if 'confirmed' not in st.session_state:
        st.session_state.confirmed = False

    if "download_done" not in st.session_state:
        st.session_state.download_done = False

    if "amount" not in st.session_state:
        st.session_state.amount = None

    if "download_duration" not in st.session_state:
        st.session_state.download_duration = None

    if "last_virus" not in st.session_state:
        st.session_state.last_virus = None


def set_confirmed():
    st.session_state.confirmed = True


def set_download_finished_flags(seq_amount: int, duration: float):
    st.session_state.download_done = True
    st.session_state.amount = seq_amount
    st.session_state.download_duration = duration


def reset_flags(new_virus: str):
    st.session_state.confirmed = False
    st.session_state.download_done = False
    st.session_state.amount = None
    st.session_state.download_duration = None
    st.session_state.last_virus = new_virus


