import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def sendEmail(subject, message_body):
    fromaddr = "Pi_Weather_Station@joshsisto.com"  # from email address
    toaddr = "joshsisto@gmail.com"  # destination email address
    smtp_user = ""  # SMTP username used for authentication
    smtp_pass = ""  # SMTP password used for authentication
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject  # subject

    body = message_body  # body
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('in-v3.mailjet.com', 587)  # e.g. ('in-v3.mailjet.com', 587)
    server.starttls()
    server.login(smtp_user, smtp_pass)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
