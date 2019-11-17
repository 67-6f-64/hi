import requests
import re
import time
import json
import random
import urllib3
import random
import string
import useful_shit
from useful_shit import genum,genemail,gename,getinfo
urllib3.disable_warnings()
r = requests.Session()

def accref():
    genemail()
    print(genemail.email)
    gename()
    print(f'{gename.fname},{gename.lname}')
    genum()
    print(genum.num)
    csrf = ''
    getinfo()
    url = r.get(getinfo.ref_link, verify=False)
    location = url.url
    locationsplit = location.split('/')
    try:
        token = locationsplit[5]
    except IndexError:
        print('Something went wrong with getting the token out of your ref link try this again please')
    headers = {f'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36 OPR/64.0.3417.73',
               'Accept': 'application/json', 'Content-Type': 'application/json', 'Referer': 'https://www.doordash.com/consumer/referred/{token}/?utm_source=copy'}
    print(location)
    time.sleep(.2)
    text = r.post(f'https://api.doordash.com/v2/consumer/', '{"country":"US","email":"' + genemail.email + '","first_name":"' + gename.fname + '","is_group_order":false,"last_name":"' + gename.lname +
                  '","password":"' + getinfo.password + '","phone_number":"' + genum.num + '","enable_password_security":false,"referral_token":"'+token+'"}', verify=False, headers=headers)
    time.sleep(.3)
    code = text.text
    json_parsed = json.loads(code)
    # print(json_parsed)
    print(json_parsed['id'])
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
        f.write(genemail.email + ":" + getinfo.password + " " + text.text + '\n')
        f.close()
        print('Everything gucci')
    if text.text == '{"non_field_errors":"Provided code did not match."}':
        print("Wrong code retard, fuckin idiot")
    if text.text == '{"is_phone_number_unique":false,"is_verified":true}':
        print("Phone number used try again!")