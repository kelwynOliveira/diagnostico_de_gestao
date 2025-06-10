FROM python:3.12-slim

WORKDIR /app
COPY app/ /app/
COPY .streamlit /app/.streamlit
    
# Virtual environment
RUN python3 -m venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"

# Packages installation
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["streamlit", "run", "main.py"]