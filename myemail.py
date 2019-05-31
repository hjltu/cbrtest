#!/usr/bin/python3

"""
author: hjltu@ya.ru

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License as
published by the Free Software Foundation; either version 2 of
the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

Send email with attached images

usage: python3 myemail.py mail@to
"""

import os
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText


def main(arg):

    """ arg:        list of all recipients,
        mailFrom:   from email address,
        passwd:     server password,
        server:     server address,
        port:       server port (int) """

    mailFrom = ''
    passwd = ''
    server = ''
    port = None

    msg = MIMEMultipart()
    msg['Subject'] = "Test"
    msg['From'] = mailFrom
    msg['To'] = ','.join(arg)
    msg.attach(MIMEText('Test cbr.ru'))

    for f in os.listdir('img'):
        with open('img/'+f, 'rb') as fp:
            img = MIMEImage(fp.read())
        img.add_header('Content-Disposition', "attachment; filename= %s" % f)
        msg.attach(img)

    server = smtplib.SMTP_SSL(server, port)
    server.ehlo()
    server.login(mailFrom, passwd)
    print("send to:", arg)
    server.send_message(msg)
    server.quit()

if(__name__=='__main__'):
    main(sys.argv[1:])

