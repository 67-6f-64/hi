import requests
import re
import time
import json
import random
import urllib3
import random
import string
import useful_shit
from useful_shit import gename,genemail,genum
urllib3.disable_warnings()
r = requests.Session()
domain = 'aqueefdd.host'
password = 'arifasim123'
ref_link = 'https://www.doordash.com/consumer/referred/Pamela-Brooks-876654/?utm_source=copy'

def start(reflink, email, name, lastname, password, phone_number):
    csrf = ''
    url = r.get(reflink, verify=False)
    location = url.url
    locationsplit = location.split('/')
    token = locationsplit[5]
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36 OPR/64.0.3417.73',
               'Accept': 'application/json', 'Content-Type': 'application/json', 'Referer': 'https://www.doordash.com/consumer/referred/' + token + '/?utm_source=copy'}
    print(location)
    time.sleep(.2)
    text = r.post('https://api.doordash.com/v2/consumer/', '{"country":"US","email":"' + email + '","first_name":"' + name + '","is_group_order":false,"last_name":"' + lastname +
                  '","password":"' + password + '","phone_number":"' + phone_number + '","enable_password_security":false,"referral_token":"'+token+'"}', verify=False, headers=headers)
    time.sleep(.3)
    code = text.text
    json_parsed = json.loads(code)
    # print(json_parsed['id'])
    id_xd = json_parsed['id']
    for c in r.cookies:
        if(c.name == 'csrf_token'):
            print(c.value)
            csrf = c.value
    r.post('https://api.doordash.com/v2/consumers/' + str(id_xd) + '/verification_code/', '{"verification_type":"email"}', verify=False, headers={'Accept': 'application/json', 'X-CSRFToken': csrf, 'Client-Version': 'web version 2.0', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36 OPR/64.0.3417.73',
                                                                                                                                                  'Sec-Fetch-Mode': 'cors', 'Content-Type': 'application/json', 'Origin': 'https://www.doordash.com', 'Sec-Fetch-Site': 'same-site', 'Referer': 'https://www.doordash.com/consumer/referred/' + token + '/?utm_source=copy', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9'})
    time.sleep(0.2)
    code = input('whats the code?')
    text = r.post('https://api.doordash.com/v2/consumers/' + str(id_xd) + '/verify/', '{"verification_type":"email","code":"' + code + '","referral_code":"' + token + '"}', verify=False, headers={'Accept': 'application/json', 'X-CSRFToken': csrf, 'Client-Version': 'web version 2.0', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36 OPR/64.0.3417.73',
                                                                                                                                                                                                    'Sec-Fetch-Mode': 'cors', 'Content-Type': 'application/json', 'Origin': 'https://www.doordash.com', 'Sec-Fetch-Site': 'same-site', 'Referer': 'https://www.doordash.com/consumer/referred/' + token + '/?utm_source=copy', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9'})
    print(text.text)
    if text.text == '{"is_phone_number_unique":true,"is_verified":true}':
        f = open('logins.txt', 'a')
        f.write(email + ":" + password + " " + text.text + '\n')
        f.close()
        print('Everything gucci')
    if text.text == '{"non_field_errors":"Provided code did not match."}':
        print("Wrong code retard, fuckin idiot")
    if text.text == '{"is_phone_number_unique":false,"is_verified":true}':
        print("Phone number used try again!")

def ref():
    genemail()
    print(genemail.email)
    gename()
    print(f'{gename.fname},{gename.lname}')
    genum()
    print(genum.num)
    start(ref_link, genemail.email, gename.fname,
          gename.lname, password, genum.num)

def multref(times):
    for a in range(0, times, 1):
        ref()