import streamlit as st

def page_business_phase() -> list:
    st.subheader("Fase do Negócio")
    # st.write("Ajuda a entender maturidade, tração e nível de complexidade atual")
    st.divider()

    questions = {}
    answers = []
    st.markdown("**1. Seu negócio já fatura, com recorrência, mais de R$ 100 mil por mês?**")
    question1 = st.radio("1. Seu negócio já fatura +R$ 100 mil/mês?", 
    [("Nunca fizemos R$ 100 mil em um mês", 0), 
    ("Já fizemos +R$ 100 mil em um mês mas ainda não é recorrente", 1), 
    ("Já fazemos +R$ 100 mil por mês há pelo menos 6 meses", 2)], 
    format_func=lambda x: x[0],
    label_visibility="collapsed")
    questions.update({"Seu negócio já fatura, com recorrência, mais de R$ 100 mil por mês?": question1[0]})
    answers.append(question1[1])

    st.markdown("**2. Sua oferta é validada e já vendeu pelo menos 3 vezes no mesmo formato?**")
    question2 = st.radio("2. Sua oferta é validada?", 
    [("Estou sempre testando algo novo e ainda não repeti uma estratégia para vender o mesmo produto", 0), 
    ("Já repeti a mesma estratégia para vender o mesmo produto mas os resultados não foram consistentes", 1), 
    ("Já vendi o mesmo produto com a mesma estratégia pelo menos 3 vezes e tive resultados consistentes. Minha oferta é validada!", 2)], 
    format_func=lambda x: x[0],
    label_visibility="collapsed")
    questions.update({"Sua oferta é validada e já vendeu pelo menos 3 vezes no mesmo formato?": question2[0]})
    answers.append(question2[1])

    st.markdown("**3. Quantas pessoas trabalham com você de maneira recorrente (mesmo que freelancer)?**")
    question3 = st.radio("3. Quantas pessoas na equipe?", 
    [("Ainda não tenho ninguém na minha equipe ", 0), 
    ("Além de mim, tenho 1 ou 2 pessoas na minha equipe", 1), 
    ("Além de mim, tenho 3 ou 4 pessoas na minha equipe", 1), 
    ("Além de mim, já tenho mais de 4 pessoas na minha equipe", 2)],
    format_func=lambda x: x[0],
    label_visibility="collapsed")
    questions.update({"Quantas pessoas trabalham com você de maneira recorrente (mesmo que freelancer)?": question3[0]})
    answers.append(question3[1])

    return questions, answers