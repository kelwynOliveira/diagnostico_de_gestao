import streamlit as st

def page_business_focus():
    st.subheader("Foco do Empresário")
    # st.write("Ajuda a personalizar a comunicação do resultado e acionar o desejo de agir")
    st.divider()

    st.markdown("**1. No seu dia a dia, onde está o seu foco?**")
    perfil = st.radio("1. No seu dia a dia, onde está o seu foco?", 
                    [("Vejo o que preciso fazer agora e faço. Não gosto de planejar demais nem sinto necessidade de inovar sempre", "Perfil Executor"),
                    ("Foco em deixar tudo estruturado e organizado. Não sinto necessidade de inovar sempre mas detesto executar sem um planejamento detalhado", "Perfil Gestor"), 
                    ("Foco em trazer o máximo de novidade e estou sempre querendo testar algo novo. Não gosto de executar sem estratégia, muito menos planejar cada detalhe", "Perfil Estrategista")],
                    format_func=lambda x: x[0],
                    label_visibility="collapsed")

    st.markdown("**2. O que mais te incomoda hoje na gestão do seu negócio?**")
    incomoda = st.text_area("2. O que mais te incomoda hoje na gestão do seu negócio?", label_visibility="collapsed")

    return perfil[1], incomoda