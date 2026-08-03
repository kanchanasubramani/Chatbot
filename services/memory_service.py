import streamlit as st

class MemoryService:

    def __init__(self):
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

    def add_message(self, role, content):
        st.session_state.chat_history.append({
            "role": role,
            "parts": [content]
        })

    def get_history(self):
        return st.session_state.chat_history

    def clear(self):
        st.session_state.chat_history = []