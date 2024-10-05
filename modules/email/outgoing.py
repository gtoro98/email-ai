# Import smtplib for the actual sending function
import smtplib
from env import email, emailPassword

# Import the email modules we'll need
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate, COMMASPACE
from os.path import basename
from email.mime.application import MIMEApplication

def sendEmail(toEmails, message):
  me = email

  msg = MIMEMultipart()
  msg['From'] = me
  msg['To'] = toEmails
  msg['Date'] = formatdate(localtime=True)
  msg['Subject'] = 'Automated AI Response'

  msg.attach(MIMEText(message))

  s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
  s.ehlo()

  s.login(me, emailPassword)
  s.sendmail(me, toEmails, msg.as_string())
  s.quit()
  s.close()
