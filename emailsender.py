import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(email, name, surname, password):
    fromaddr = "*******@*****.***"
    toaddr = email
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Successfully registered!"

    body = "Hello dear " + name + " " + surname + "\n You are successfully registered. \n Your details are: \n" + email + "\n" + name + "\n" + surname + "\n" + password
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "*********")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
