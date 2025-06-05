import streamlit as st

def page_management_autonomy():
    st.subheader("Gestão e Autonomia")
    # st.write("Avalia quanto a operação depende do dono")
    st.divider()

    questions = {}
    answers = []
    st.markdown("**1. Se você tirar férias de 15 dias, seu negócio continua rodando com vendas e entregas?**")
    question1 = st.radio("1. Férias de 15 dias?",
    [("Se eu parar, tudo continua rodando normalmente", 2), 
    ("Se eu parar, as vendas param - mas as entregas acontecem normalmente", 1), 
    ("Se eu parar, as entregas param - mas as vendas acontecem normalmente", 1), 
    ("Se eu parar, tudo para", 0)], 
    format_func=lambda x: x[0],
    label_visibility="collapsed")
    questions.update({"Se você tirar férias de 15 dias, seu negócio continua rodando com vendas e entregas?": question1[0]})
    answers.append(question1[1])

    st.markdown("**2. Quantas horas por dia você passa apagando incêndios ou respondendo assuntos operacionais?**")
    question2 = st.radio("2. Quantas horas apagando incêndios?", 
    [("Quase nada", 2), 
    ("Até 2 horas por dia", 1), 
    ("Mais de 3 horas por dia", 0)], 
    format_func=lambda x: x[0],
    label_visibility="collapsed")
    questions.update({"Quantas horas por dia você passa apagando incêndios ou respondendo assuntos operacionais?": question2[0]})
    answers.append(question2[1])

    st.markdown("**3. Você tem reuniões ou rituais fixos com sua equipe para acompanhar entregas?**")
    question3 = st.radio("3. Reuniões com equipe?", 
    [("Tenho, e usamos isso para fortalecer a cultura da empresa e engajar a equipe nas nossas estratégias de médio a longo prazo", 2), 
    ("Tenho, mas usamos para apagar incêndio e alinhar ações imediatas da operação", 1),
    ("Ainda não. Vamos nos falando conforme tudo acontece", 0)],
    format_func=lambda x: x[0],
    label_visibility="collapsed")
    questions.update({"Você tem reuniões ou rituais fixos com sua equipe para acompanhar entregas?": question3[0]})
    answers.append(question3[1])

    st.markdown("**4. Suas tarefas e as do time estão organizadas em um sistema com prazos, responsáveis e prioridades?**")
    question4 = st.radio("4. Tarefas organizadas?", 
    [("Não, todas as atividades são passadas em tempo real pelo WhatsApp", 0), 
    ("Sim, tenho uma lista de atividades com prazos e responsáveis bem definidos", 1), 
    ("Além do controle de atividades, tenho um sistema de gestão completo que facilita a visualização de todas as nossas metas, projetos simultâneos e toda a gestão da empresa", 2)],
    format_func=lambda x: x[0],
    label_visibility="collapsed")
    questions.update({"Suas tarefas e as do time estão organizadas em um sistema com prazos, responsáveis e prioridades?": question4[0]},)
    answers.append(question4[1])

    return questions, answers