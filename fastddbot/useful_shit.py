import requests
import re
import time
import json
import random
import urllib3
import random
import string
import json
import names
urllib3.disable_warnings()
r = requests.Session()

def genemail():
    getinfo()
    email = []
    acemail = ''
    name = names.get_full_name(gender='male')
    for a in range(0, random.randint(5, 10), 1):
        email.append(random.choice(string.ascii_lowercase))
    for chars in email:
        acemail = acemail + str(chars)
    genemail.email = f'{name.replace(" ","")}{random.randint(10000,99999)}@{getinfo.domain}'

def gename():
    name = names.get_first_name(gender='male')
    gename.fname = f'{name}' 
    gename.lname = f'{names.get_last_name()}'

def genum():
    ca_codes = [403, 587, 780, 825, 250, 604,
                236, 778, 204, 431, 506, 709, 867]
    genum.num = f'+1{random.choice(ca_codes)}91{random.randint(10000,99999)}'

def getinfo():
    with open('info.json') as json_file:
        data = json.load(json_file)
        for n in data["info"]:
            getinfo.domain = n["domain"]
            getinfo.password = n["password"]
            getinfo.ref_link = n['ref_link']
            getinfo.webdriver = n['webdriver_path']
