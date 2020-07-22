#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 23:52:44 2020

@author: andynystrom
"""


import requests
import csv

url = 'https://raw.githubusercontent.com/nychealth/coronavirus-data/master/case-hosp-death.csv'
response = requests.get(url)

wrapper = csv.reader(response.text.strip().split('\n'))

for record in wrapper:
    date = (record[0])
    case_count = (record[1])
    hospitalize_count = (record[2])
    death_count = (record[3])
   
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACb9f8f0ea5dca76a66929e9cafafebe00'
auth_token = '83813f43547e94ab73ce84af5958a539'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='',
         from_='+12059227403',
         status_callback='http://postb.in/1234abcd',
         to='+15166529203'
     )

print(message.sid)




