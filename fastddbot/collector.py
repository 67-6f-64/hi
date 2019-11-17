import time
import threading
import requests
import names
import random
import json
from multiprocessing.dummy import Pool as ThreadPool 
import urllib3
from useful_shit import getinfo,gename,genemail,genum
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from get_short_link import getlink


def speed():
    getinfo()
    r1 = requests.Session()
    r1.get('https://www.doordash.com', verify=False)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36 OPR/64.0.3417.73','Accept':'application/json','Content-Type':'application/json'}
    password = getinfo.password
    print('Made first request')
    genum()
    phone_number = genum.num
    gename()
    name = gename.fname 
    lastname = gename.lname 
    print(lastname)
    genemail()
    email = genemail.email
    print(email)
    text = r1.post('https://api.doordash.com/v2/consumer/', '{"country":"US","email":"' + email + '","first_name":"' + name + '","is_group_order":false,"last_name":"' + lastname +'","password":"' + password + '","phone_number":"' + phone_number + '","enable_password_security":false}', verify=False, headers=headers)
    time.sleep(1) 
    code = text.text
    time.sleep(1) 
    json_parsed = json.loads(code)
    print(json_parsed['referral_code'])
    id_xd = json_parsed['referral_code']
    print(id_xd)
    getlink(email,password)
    # print('https://www.doordash.com/consumer/referred/' + id_xd + '/?utm_source=copy' + '\nEmail:Password: ' + email + ":" + password)
    # # global broswer
    # # broswer = webdriver.Chrome(getinfo.webdriver)
    # # broswer.get('https://www.doordash.com/consumer/login/?next=/consumer/invite/')
    # # sendkeys('#login-form > label:nth-child(1) > input',email)
    # # sendkeys('#login-form > label:nth-child(2) > div.Input_passwordHolder___15rJ5 > input',password)
    # # inputtt.send_keys(Keys.ENTER)
    # # awaitt('#root > div > div.sc-bwzfXH.eOmgCJ > div.sc-kvZOFW.xcnRO > div > div > div > div.sc-bOxvsH.kHpZnA.sc-EHOje.epRhHG > div > div.sc-dnqmqq.iANAm > button')
    # # print(pyperclip.paste())
    # f = open('logins.txt', 'a')
    # f.write('https://www.doordash.com/consumer/referred/' + id_xd + '/?utm_source=copy' + ' Email:Password: ' + email + ":" + password + '\n')
    # f.close()
# request.post({
#                     url: 'https://api-consumer-client.doordash.com/graphql',
#                     jar: j,
#                     headers: {
#                         'Accept': 'application/json',
#                         'accept-language': 'en-US',
#                         'Client-Version': 'web version 2.0',
#                         'Content-Type': 'application/json;charset=UTF-8',
#                         'Origin': 'https://www.doordash.com',
#                         'Referer': 'https://www.doordash.com/consumer/invite/',
#                         'Sec-Fetch-Mode': 'cors',
#                         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
#                     },
#                     json:{"operationName":"referralDetail","variables":{},"query":"query referralDetail {\n  referralDetail {\n    referralUrl\n    inviteTitle\n    inviteSubtitle\n    __typename\n  }\n}\n"}
#                 }, function(err,res){
#                     let link = (res.body.data.referralDetail.referralUrl)

#                 })
# r1 = requests.Session()
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36 OPR/64.0.3417.73','Accept':'application/json','Content-Type':'application/json'}
# r1.get('https://api-consumer-client.doordash.com/graphql')
speed()
