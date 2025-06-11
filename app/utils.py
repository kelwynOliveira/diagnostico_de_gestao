import streamlit as st
import gspread
from google.oauth2 import service_account
import pandas as pd
from googleapiclient.discovery import build
import ssl
import re
from email.message import EmailMessage
import smtplib
import json
import os
from dotenv import load_dotenv
load_dotenv()

# User data validation functions
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        return False, "Por favor, insira um e-mail válido."
    return True, ""

def validate_phone(phone):
    # Accepts formats like:
    # (11) 91234-5678, 11912345678, 11 91234 5678, 91234-5678, 912345678
    pattern = r'^(\(?\d{2}\)?\s?)?9\d{4}[- ]?\d{4}$'
    if not re.match(pattern, phone):
        return False, "Por favor, insira um número de telefone válido (ex: (92) 98471-8481)"
    return True, ""

# Save user data to Google Sheets
def get_spreadsheet():
    gcp_service_account_info = json.loads(os.getenv("gcp_service_account"))

    creds = service_account.Credentials.from_service_account_info(
        gcp_service_account_info,
        scopes=[
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]
    )
    client = gspread.authorize(creds)

    folder_id = os.getenv("folder_id")
    sheet_name = os.getenv('sheet_name')

    try:
        spreadsheet = client.open(sheet_name, folder_id=folder_id)
    except gspread.exceptions.SpreadsheetNotFound:
        spreadsheet = client.create(sheet_name)
        drive_service = creds.with_scopes(['https://www.googleapis.com/auth/drive'])
        file_id = spreadsheet.id

        drive = build('drive', 'v3', credentials=drive_service)
        
        file = drive.files().get(fileId=file_id, fields='parents').execute()
        previous_parents = ",".join(file.get('parents'))
        
        drive.files().update(
            fileId=file_id,
            addParents=folder_id,
            removeParents=previous_parents,
            fields='id, parents'
        ).execute()
    
    try:
        worksheet = spreadsheet.worksheet(os.getenv('spreadsheet_name'))
    except gspread.exceptions.WorksheetNotFound:
        worksheet = spreadsheet.add_worksheet(title=os.getenv('spreadsheet_name'), rows=100, cols=20)

    return worksheet

def save_on_spreadsheet(data):
    worksheet = get_spreadsheet()
    df = pd.DataFrame([data])
    existing_data = worksheet.get_all_values()
    next_row = len(existing_data) + 1
    worksheet.insert_rows(df.values.tolist(), row=next_row)


# Send email with user data and results
def send_email(email_to, subject, body, host_email=os.getenv("EMAIL_HOST"), user_password=os.getenv("EMAIL_APP_PASSWORD"),):
    message = EmailMessage()
    message['From'] = host_email
    message['To'] = email_to
    message['Subject'] = subject
    message.set_content(body, subtype='html')

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(host_email, user_password)
        smtp.send_message(message)


def email_body(name, subject, body):
    return f'''
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{subject}</title>
    </head>
    <body>
    <p>Olá, {name}!\n\n{body}</p>
    </body>
    </html>
    '''

# Get file content for results
def get_result_markdown(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text_content = file.read()
            return text_content
    except FileNotFoundError:
        print(f"Error: File not found at path: {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
def get_result_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: File not found at path: {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

