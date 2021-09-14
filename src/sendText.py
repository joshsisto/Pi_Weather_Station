import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from credentials import alert_addr, gmail_user, gmail_app_pass, mailjet_user, mailjet_pass


def send_email(message_body):
    fromaddr = "Pi_Weather_Station@sisto.xyz"  # from email address
    toaddr = alert_addr  # destination email address
    smtp_user = mailjet_user
    smtp_pass = mailjet_pass
    # print('smtp_pass' + smtp_pass)
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    # msg['Subject'] = subject  # subject

    body = message_body  # body
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('in-v3.mailjet.com', 587)  # e.g. ('in-v3.mailjet.com', 587)
    server.starttls()
    server.login(smtp_user, smtp_pass)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
