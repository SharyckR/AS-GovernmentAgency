import os
import smtplib
import ssl
from email.message import EmailMessage
import re
from fastapi import APIRouter, status
router = APIRouter(prefix='/send', tags=['send email'],
                   responses={status.HTTP_404_NOT_FOUND: {'message': 'Not found'}})


def is_valid_email(email):
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(email_pattern, email):
        return True
    else:
        return False


@router.post('/token')
async def send_token_authentication(email_receiver: str, access_token: str):
    email_sender = 'dcarrerotinoco74@gmail.com'
    email_password = os.getenv('PASSWORD_EMAIL')
    subject = 'TOKEN AUTHENTICATION FOR GOVERNMENT AGENCY'
    body = f"""\n\n\t\t\t\t\tAuthentication successfully, your access toke is : {access_token}"""
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
    print(f'Token Authentication sent successfully to: {email_receiver}!!')
