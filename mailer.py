import datetime

import scraper
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def initialize_text(elements):
    time_passed,result=scraper.menu(*elements)
    text=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\n\n"
    text+="Execution Time= "+str(time_passed)+"\n\n"
    print(result)
    for i in result:
        text+=i
    return text

def send_mail(text):
    if text is None:
        elements = ["MAC", "AFT", "IPJ", "TCD", "TKF", "AEH"]
        text = initialize_text(elements)
    #_,text=scraper.menu("MAC", "AFT", "IPJ", "TCD", "TKF", "AEH", "TPC")


    # Gmail account credentials
    email_to_send = 'atahanuz1@gmail.com'
    password = 'sefkgltezwoiaxwd'

    # The receiver's email address
    email_to_receive = 'atahanuz23@gmail.com'

    # Email content
    email_subject = "Fon Fiyatları: "+ datetime.datetime.now().strftime("%d/%m/%Y")

    text=str(text)
    email_body = text
    print(email_body)

    # Setting up the MIME
    message = MIMEMultipart()
    message['From'] = email_to_send
    message['To'] = email_to_receive
    message['Subject'] = email_subject
    message.attach(MIMEText(email_body, 'plain'))

    # Create secure connection with server and send email
    context = smtplib.ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(email_to_send, password)
            server.sendmail(
                email_to_send, email_to_receive, message.as_string()
            )
        print("Email successfully sent!")
    except Exception as e:
        print(f"Error occurred: {e}")




if __name__ == '__main__':
    send_mail(None)