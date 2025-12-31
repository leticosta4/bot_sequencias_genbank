import streamlit as st

def set_init_flags():
    if 'confirmed' not in st.session_state:
        st.session_state.confirmed = False

    if "download_done" not in st.session_state:
        st.session_state.download_done = False

    if "amount" not in st.session_state:
        st.session_state.amount = None


def set_confirmed():
    st.session_state.confirmed = True


def set_download_finished_flags(seq_amount: int, duration: float):
    st.session_state.download_done = True
    st.session_state.amount = seq_amount
    st.session_state.download_duration = duration


