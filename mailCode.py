import os
import smtplib
import imghdr
from email.message import EmailMessage

#EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
#EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

#contacts = ['vikush40@gmail.com', 'vickyhlustov@gmail.com']

msg = EmailMessage()
msg['Subject'] = 'Check out this dream vacation you won!'
msg['From'] = 'vikush40@gmail.com'
msg['To'] = 'vickyhlustov@gmail.com'

msg.set_content('Image attached...')
files=['bookingMail.pdf']
for file in files:
    with open(file, 'rb') as f:
        file_data=f.read() 
        file_name=f.name
                   
msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)














with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login('vikush40@gmail.com', '123456')
    smtp.send_message(msg)