import sys
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def SendMail(ImgFileName):
    img_data = open(ImgFileName, 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'Leprechaun Detected'
    msg['From'] = 'FromEmail@gmail.com'
    msg['To'] = 'ToEmail@gmail.com'

    text = MIMEText("Leprechaun Detected.")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    msg.attach(image)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(msg['From'], "Your mailPassword")
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()


SendMail(sys.argv[1])
