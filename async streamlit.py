import dotenv
import streamlit as st
from openai import OpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_gigachat.chat_models import GigaChat

api_key = dotenv.get_key('./keys.env','deepseek_key')

# Установите ваш API-ключ OpenAI (или другой совместимый API)
client = OpenAI(api_key="YzJjODRlZjgtODYzNy00OWEyLTk5MGMtNThhZTlkOTkwZTI3OjljZTkwMWYzLTU1YWQtNDI0YS1iNWMyLTA0NTI4MWIwNTRiNg==",
                base_url="https://gigachat.devices.sberbank.ru/api/v1")
giga = GigaChat(
    # Для авторизации запросов используйте ключ, полученный в проекте GigaChat API
    credentials="YzJjODRlZjgtODYzNy00OWEyLTk5MGMtNThhZTlkOTkwZTI3OjljZTkwMWYzLTU1YWQtNDI0YS1iNWMyLTA0NTI4MWIwNTRiNg==",
    verify_ssl_certs=False)
st.title("💬 Чат с Gigachat")

if "messages" not in st.session_state:
    st.session_state.messages = []

if prompt := st.chat_input("Напишите сообщение..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = giga.invoke(prompt).content
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})






