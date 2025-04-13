import dotenv
import streamlit as st
from langchain_gigachat.chat_models import GigaChat

api_key = dotenv.get_key('./keys.env','gigachat_key')
# Установите ваш API-ключ OpenAI (или другой совместимый API)
giga = GigaChat(
    # Для авторизации запросов используйте ключ, полученный в проекте GigaChat API
    credentials=api_key,
    verify_ssl_certs=False)
st.title("💬 Чат с Gigachat")
# создание истории сообщений
if "messages" not in st.session_state:
    st.session_state.messages = []

# создание чата
if prompt := st.chat_input("Напишите сообщение..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    #публикация вопроса от пользователя
    with st.chat_message("user"):
        st.markdown(prompt)
    #публикация ответ от нейросети
    with st.chat_message("assistant"):
        response = giga.invoke(prompt).content
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})






