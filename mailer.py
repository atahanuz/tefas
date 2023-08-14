import datetime

import scraper
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail():
    elements = ["MAC", "AFT", "IPJ", "TCD", "TKF", "AEH"]
    print("here")
    #_,text=scraper.menu("MAC", "AFT", "IPJ", "TCD", "TKF", "AEH", "TPC")


    # Gmail account credentials
    email_to_send = 'atahanuz1@gmail.com'
    password = 'sefkgltezwoiaxwd'

    # The receiver's email address
    email_to_receive = 'atahanuz23@gmail.com'

    # Email content
    email_subject = "ETF Prices" + datetime.datetime.now().strftime("%d/%m/%Y")
    text=str(text)
    email_body = text

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
    send_mail()