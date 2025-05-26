import streamlit as st
from utils import get_result_markdown
from pathlib import Path

current_folder = Path(__file__).parent
TEMPLATES_FOLDER = current_folder / 'result'

def page_result(categoria, perfil):
  st.title("🧠 Diagnóstico de Gestão")

  result_files = {
        "Validação": {
            "Perfil Executor": TEMPLATES_FOLDER / "executor_validacao.md",
            "Perfil Gestor":  TEMPLATES_FOLDER / "gestor_validacao.md",
            "Perfil Estrategista":  TEMPLATES_FOLDER / "estrategista_validacao.md"
        },
        "Início da Escala": {
            "Perfil Executor":  TEMPLATES_FOLDER / "executor_iniciando.md",
            "Perfil Gestor":  TEMPLATES_FOLDER / "gestor_iniciando.md",
            "Perfil Estrategista":  TEMPLATES_FOLDER / "estrategista_iniciando.md"
        },
        "Escala com Liberdade": {
            "Perfil Executor":  TEMPLATES_FOLDER / "executor_escala.md",
            "Perfil Gestor":  TEMPLATES_FOLDER / "gestor_escala.md",
            "Perfil Estrategista":  TEMPLATES_FOLDER / "estrategista_escala.md"
        }
    }

  st.markdown(get_result_markdown(result_files[categoria][perfil]))

  st.markdown("💡 *Lembrete:* essas ações são só o começo. Se fizer sentido, posso te convidar para um **Check-up de Gestão Escalável**, onde destravamos os gargalos estruturais da sua operação e desenhamos juntos o caminho real para crescer com liberdade.")