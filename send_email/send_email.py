# Script for 'send_email' program in python
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""
The program sends an email from a gmail account using python
"""

import smtplib

# Asks as input the data needed for building the email:
print('')
gmail_user = input('Enter gmail user: ')
gmail_password = input('Enter gmail password: ')

print('')
print('Verify that the option "allowing less secure apps to access your account" is enabled in your gmail settings.')
print('https://myaccount.google.com/lesssecureapps')

print('')
recipient = input('Enter email recipient: ')
subject = input('Enter subject of the email: ')
body = input('Enter text of the email: ')

# Collects in email_text the data gathered for the email
email_text = "From: %s\nTo: %s\nSubject: %s\n \n%s" % (gmail_user, recipient, subject, body)

# Establishes a SSL connection and sends the email:
try:
  server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
  server.ehlo()
  server.login(gmail_user, gmail_password)
  server.sendmail(gmail_user, recipient, email_text)
  server.close()
  print('')
  print('Email sent!\n')
except:
  print('Something went wrong...')
