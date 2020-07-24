import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from credentials import alert_addr, gmail_user, gmail_app_pass


def send_email(message_body):
    fromaddr = "joshsisto@gmail.com"  # from email address
    toaddr = alert_addr  # destination email address
    smtp_user = gmail_user
    smtp_pass = gmail_app_pass
    # print('smtp_pass' + smtp_pass)
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    # msg['Subject'] = subject  # subject

    body = message_body  # body
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)  # e.g. ('in-v3.mailjet.com', 587)
    server.starttls()
    server.login(smtp_user, smtp_pass)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
