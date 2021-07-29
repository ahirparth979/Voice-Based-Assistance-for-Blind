'''
Created on Sep 9, 2020

@author: Parth Ahir
'''

import smtplib

s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

s.login('ahirparth979@gmail.com', 'ajqjspnblrrgsmid')

message = 'This is a Test'

s.sendmail('ahirparth979@gmail.com', 'ahirparth979@gmail.com', message)

s.quit()
