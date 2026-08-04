import os, smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
load_dotenv(".env.mailpit")
HOST = os.getenv("SMTP_HOST")
PORT = int(os.getenv("SMTP_PORT"))

# --- Conteudo (RFC 5322) ---
msg = EmailMessage()
msg["From"] = os.getenv("SMTP_FROM")
msg["To"] = "aluno@aula.local"
msg["Subject"] = "Primeira mensagem via SMTP"
msg.set_content(
    "Mensagem enviada a partir de um programa Python, "
    "utilizando o protocolo SMTP."
)

# --- Protocolo ---
with smtplib.SMTP(HOST, PORT) as servidor:
    servidor.set_debuglevel(1)   # exibe o dialogo SMTP
    servidor.ehlo()              # identificacao
    servidor.send_message(msg)   # MAIL FROM + RCPT + DATA
print("Mensagem enviada krl.")






