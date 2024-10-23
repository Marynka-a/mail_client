import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Input of data by the user
to_email = input("Enter recipient's email address: ")
subject = input("Enter the subject of the email: ")
message = input("Enter the text of the email: ")

# Settings for connecting to Gmail
SMTP_SERVER = 'smtp.gmail.com'
EMAIL_ADDRESS = 'youre_mail@gmail.com'
PASSWORD = 'youre_password'

# Sending a letter using SMTP
smtp = smtplib.SMTP(SMTP_SERVER, 587)
smtp.starttls()
smtp.login(EMAIL_ADDRESS, PASSWORD)

msg = MIMEMultipart()
msg['From'] = EMAIL_ADDRESS
msg['To'] = to_email
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

smtp.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())

# Disconnect from the SMTP server
smtp.quit()
