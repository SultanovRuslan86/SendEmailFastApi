import pytest
from main import submit
from email.message import EmailMessage
import smtplib

import os
from dotenv import load_dotenv

load_dotenv()

# Тест на проверку успешной отправки письма
def test_send_email_success():
    email_address = os.getenv('EMAIL_ADDRESS')
    email_password = os.getenv('EMAIL_PASSWORD')

    data = {
        'emailAddress': 'recipient@example.com',
        'subject': 'Test Subject',
        'message': 'Test Message',
    }

    response = submit(**data)

    assert response == 'Письмо успешно отправлено!'

# Тест на обработку ошибок
def test_send_email_error():
    data = {
        'subject': 'Test Subject',
        'message': 'Test Message',
    }

    with pytest.raises(Exception):
        response = submit(**data)

# Тест для проверки отправки письма (SMTP)
def test_send_email_smtp():
    email_address = os.getenv('EMAIL_ADDRESS')
    email_password = os.getenv('EMAIL_PASSWORD')
    recipient_email = 'recipient@example.com'

    msg = EmailMessage()
    msg['Subject'] = 'Test Subject'
    msg['From'] = email_address
    msg['To'] = recipient_email
    msg.set_content('Test Message')

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_address, email_password)
            smtp.send_message(msg)
    except Exception as e:
        pytest.fail(f'Failed to send email: {e}')


# для запуска введем в консоле команду -pytest test_service.py-