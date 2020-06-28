#!/usr/bin/env python
# coding: utf-8

# In[3]:

# In[20]:

import smtplib

# SET EMAIL LOGIN REQUIREMENTS
# REPLACE SendID, RecieveID, AppPass with your personal details

gmail_user = '<SendID>'
gmail_app_password = '<AppPass>'

# SET THE INFO ABOUT THE SAID EMAIL
sent_from = gmail_user
sent_to = ['<SendID>', '<RecieveID>']
sent_subject = "REPORITNG ISSUE"
sent_body = """ App not working \n\n """

email_text = """From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(sent_to), sent_subject, sent_body)

# Details: http://www.samlogic.net/articles/smtp-commands-reference.htm
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_app_password)
    server.sendmail(sent_from, sent_to, email_text)
    server.close()

    print('Email sent!')
except Exception as exception:
    print("Error: %s!\n\n" % exception)


# In[ ]:

