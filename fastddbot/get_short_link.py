import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import useful_shit
from useful_shit import getinfo
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import pyperclip
from selenium.webdriver.chrome.options import Options
# oppptions = Options()
# oppptions.set_headless(headless=True)
def sendkeys(selector,keys):
    element = WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
    browser.execute_script("arguments[0].click();", element)
    global inputtt
    inputtt = browser.find_element_by_css_selector(selector)
    inputtt.send_keys(keys)
def awaitt(css_selector):
    element = WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
    browser.execute_script("arguments[0].click();", element)
def getthing():
    global browser
    getinfo()

    browser = webdriver.Chrome(getinfo.webdriver)
    browser.get('https://www.doordash.com/consumer/login/?next=/consumer/invite/')
    if 'https://identity.doordash.com/' in browser.current_url:
        browser.close()
        getthing()
    time.sleep(2)
def getlink(email, password):
    getthing()
    sendkeys('#login-form > label:nth-child(1) > input',email)
    sendkeys('#login-form > label:nth-child(2) > div.Input_passwordHolder___15rJ5 > input',password)
    inputtt.send_keys(Keys.ENTER)
    awaitt('#root > div > div.sc-bwzfXH.eOmgCJ > div.sc-kvZOFW.xcnRO > div > div > div > div.sc-bOxvsH.kHpZnA.sc-EHOje.epRhHG > div > div.sc-dnqmqq.iANAm > button')
    time.sleep(2)
    short_link = pyperclip.paste()
    print(short_link)
    browser.close()
    f = open('logins.txt', 'a')
    f.write(f'{email}:{password} {short_link}\n')
    f.close()
getlink('BrianIvie55917@aqueefdd.host','arifasim123')
