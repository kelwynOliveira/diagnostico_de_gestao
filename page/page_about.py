import streamlit as st

def about_page() -> (str, str, str):
    st.subheader("Sobre você")
    st.write("Seus dados para envio do Diagnóstico")
    st.divider()

    name = st.text_input("1. Qual é o seu nome?")
    email = st.text_input("2. Qual é o seu melhor e-mail?", placeholder="seuemail@exemplo.com")
    phone = st.text_input("3. Qual é o seu número de telefone?", placeholder="(92) 98471-8481")

    return name, email,phone