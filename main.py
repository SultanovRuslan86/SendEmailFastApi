from typing import Union

from fastapi import FastAPI, Request, Form
from starlette.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import os
from dotenv import load_dotenv

import smtplib
from email.message import EmailMessage

from logger import logger

load_dotenv()

templates = Jinja2Templates(directory='templates')

app = FastAPI()

app.mount('/static', StaticFiles(directory='static', html=True), name='static')

@app.get('/')
def home(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

@app.post('/send_email')
def submit(emailAddress: str = Form(), subject: str = Form(), message: str = Form()):
    logger.info(f"Received email with address: {emailAddress}")
    logger.info(f"Subject: {subject}")
    logger.info(f"Message: {message}")

    email_address = os.getenv('EMAIL_ADDRESS')
    email_password = os.getenv('EMAIL_PASSWORD')

    # Создаем email
    msg = EmailMessage()
    msg['Subject'] = 'Email subject'
    msg['From'] = email_address
    msg['To'] = emailAddress
    msg.set_content(
        f'''\
    Email: {emailAddress}
    Subject: {subject}
    Message: {message}     
    ''',
    )

    # Отправляем письмо
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)

    return 'Письмо успешно отправлено!'