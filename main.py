import streamlit as st
from utils import *
from pathlib import Path
from datetime import datetime
import pytz

# Pages
from page.page_about import *
from page.page_business_phase import *
from page.page_management_autonomy import *
from page.page_business_focus import *
from page.page_result import *
from classify import *

def next_page():
    st.session_state.page += 1

def main():
    st.set_page_config(page_title="Diagnóstico de Gestão", layout="centered")
    st.title("Diagnóstico de Gestão Express")
    # st.write("Responda às perguntas e descubra seu perfil!")
    st.divider()

    if "page" not in st.session_state:
        st.session_state.page = 0 
    if "answers" not in st.session_state:
        st.session_state.answers = []

    # Página Sobre
    if st.session_state.page == 0:
        name, email, phone = about_page()
        if st.button("Próximo", key="about_next"):
            valid_email, msg_email = validate_email(email)
            valid_phone, msg_phone = validate_phone(phone)

            if not name:
                st.warning("Por favor, preencha seu nome.")
            elif not valid_email:
                st.warning(msg_email)
            elif not valid_phone:
                st.warning(msg_phone)
            else:
                st.session_state.answers.append({"name": name, "email": email, "phone": phone})
                next_page()
                st.rerun()
                

    # Página Fase do Negócio
    elif st.session_state.page == 1:
        answers = page_business_phase()
        if st.button("Próximo", key="phase_next"):
            st.session_state.answers.append(answers)
            next_page()
            st.rerun()
            

    # Página Gestão e Autonomia
    elif st.session_state.page == 2:
        answers = page_management_autonomy()
        if st.button("Próximo", key="management_next"):
            st.session_state.answers.append(answers)
            next_page()
            st.rerun()

    # Foco do Empresário
    elif st.session_state.page == 3:
        perfil, incomoda = page_business_focus()
        if st.button("Finalizar", key="focus_next"):
            st.session_state.answers.append(({"Perfil": perfil, "Incomoda": incomoda}))
            next_page()
            st.rerun()
    
    # Result
    elif st.session_state.page == 4:
        st.balloons()
        answers_data = [st.session_state.answers[1],st.session_state.answers[2]]
        categoria = result(answers_data)
        perfil_final = st.session_state.answers[3]["Perfil"]
        page_result(categoria, perfil_final)

        # Save on spreadsheet
        user_data = st.session_state.answers[0]
        user_data.update({"Categoria": categoria, "Perfil": perfil_final, "Incomoda": st.session_state.answers[3]["Incomoda"]})
        br_tz = pytz.timezone('America/Sao_Paulo')
        user_data.update({"date": datetime.now(br_tz).strftime("%Y-%m-%d %H:%M:%S")})
        # user_data.update({"date": time.strftime("%Y-%m-%d %H:%M:%S")})
        save_on_spreadsheet(user_data)

        # Send Email user
        try:
            current_folder = Path(__file__).parent
            TEMPLATES_FOLDER = current_folder / 'email'

            result_files = {
                    "Validação": {
                        "Perfil Executor": TEMPLATES_FOLDER / "executor_validacao.json",
                        "Perfil Gestor": TEMPLATES_FOLDER / "gestor_validacao.json",
                        "Perfil Estrategista": TEMPLATES_FOLDER / "estrategista_validacao.json"
                    },
                    "Início da Escala": {
                        "Perfil Executor": TEMPLATES_FOLDER / "executor_iniciando.json",
                        "Perfil Gestor": TEMPLATES_FOLDER / "gestor_iniciando.json",
                        "Perfil Estrategista": TEMPLATES_FOLDER / "estrategista_iniciando.json"
                    },
                    "Escala com Liberdade": {
                        "Perfil Executor": TEMPLATES_FOLDER / "executor_escala.json",
                        "Perfil Gestor": TEMPLATES_FOLDER / "gestor_escala.json",
                        "Perfil Estrategista": TEMPLATES_FOLDER / "estrategista_escala.json"
                    }
                }
            
            email_data = get_result_json(result_files[user_data["Categoria"]][user_data['Perfil']])

            email_to = user_data['email']
            subject = email_data['subject']
            body = email_body(user_data['name'], email_data['subject'], email_data['body'])

            send_email(email_to, subject, body)
            st.write("Sua resposta foi enviada para o seu email!")
        except Exception as e:
            # st.error(f"Failed to send email: {str(e)}")
            print(f"Failed to send email: {str(e)}")
            # pass
        
        # Send Email host
        try:
            email_to = st.secrets["EMAIL_HOST"]
            subject = 'Nova submissão de Diagnóstico de Gestão'
            body = f'''{user_data['name']} acabou de preencher o formulário de Diagnóstico de Gestão.<br>
            Email: {user_data['email']} <br>
            Telefone: {user_data['phone']} <br>
            Folder: https://drive.google.com/drive/folders/{st.secrets["folder_id"]} <br>
            '''
            send_email(email_to, subject, body)
        except Exception as e:
            # st.error(f"Failed to send email: {str(e)}")
            print(f"Failed to send email: {str(e)}")
            pass
        
if __name__ == "__main__":
    main()
