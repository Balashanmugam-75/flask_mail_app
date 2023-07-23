from email.mime.text import  MIMEText
import smtplib

def send_email(email,name,height,average_height,count):
    from_email = "ravanan.alpha@gmail.com"
    from_password = "jkuilrjspvxksnfg"
    to_email = email

    subject = "Height Data"
    message = "Hey <strong>{}</strong>! your height is <strong> {} </strong>.Average height of all is <strong>{}</strong> calculated from <strong>{}</strong>".format(name,height,average_height,count)

    msg = MIMEText(message,'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_password)
    gmail.send_message(msg)
