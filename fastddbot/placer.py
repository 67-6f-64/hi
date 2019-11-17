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
from selenium.webdriver.chrome.options import Options
import random
# options = Options()
# options.set_headless(headless=True)
global lemail
global lpass
def quantity(xpath,times):
    thing = browser.find_element_by_css_selector(xpath)
    for a in range(0,times-1,1):
        time.sleep(0.1)
        thing.click()
def awaitt(css_selector):
    element = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
    browser.execute_script("arguments[0].click();", element)
def newquantity(selector,times):
    for a in range(0,times-1,1):
        awaitt(selector)
        time.sleep(0.1)
def sendkeys(selector,keys):
    element = WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
    browser.execute_script("arguments[0].click();", element)
    global inputtt
    inputtt = browser.find_element_by_css_selector(selector)
    inputtt.send_keys(keys)
def atc():
    getinfo()
    global browser
    browser = webdriver.Chrome(getinfo.webdriver)
    browser.set_window_size(800,900)
    #get store detail
    browser.get('https://www.doordash.com/store/la-barca-restaurant-new-york-133934/?pickup=true&true=') 
    time.sleep(2)
    awaitt('#root > div > div.sc-bwzfXH.eOmgCJ > div.sc-kvZOFW.xcnRO > div > div > div.sc-gUlUPW.loQmCT > div:nth-child(8) > div > div:nth-child(4) > button')
    time.sleep(2)
    thing = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div[3]/div/div[2]/div/div/div[2]/div[1]/div/div/div/h2/span')))
    print(thing.text)
    if thing.text == 'Carrot (Zanahoria)':
        #close button
        awaitt('#root > div > div:nth-child(3) > div > div:nth-child(2) > div > div > div.sc-dxgOiQ.knXTJr > button')
        #soda 
        awaitt('#root > div > div.sc-bwzfXH.eOmgCJ > div.sc-kvZOFW.xcnRO > div > div > div.sc-gUlUPW.loQmCT > div:nth-child(7) > div > div:nth-child(1) > button')
        #some soda 
        awaitt(f'#Toggle-{random.randint(5,10)}')
        #for homeless
        sendkeys("#FieldWrapper-7","dar a las personas sin hogar y marcar como recogido")
        #10 times
        newquantity('#root > div > div:nth-child(3) > div > div:nth-child(2) > div > div > div.sc-kgoBCf.fadSlv > div > div > div > div > div > div.sc-dnqmqq.ibsFAU > div:nth-child(3) > button',10)
        #atc
        awaitt('#root > div > div:nth-child(3) > div > div:nth-child(2) > div > div > div.sc-kgoBCf.fadSlv > div > div > div > div > div > div.sc-hfLElm.VdQyN > button')
        #5$ thing
        awaitt('#root > div > div.sc-bwzfXH.eOmgCJ > div.sc-kvZOFW.xcnRO > div > div > div.sc-gUlUPW.loQmCT > div:nth-child(8) > div > div:nth-child(6) > button')
        #random option
        awaitt(f'#Toggle-{random.randint(14,15)}')
        #atc button
        #awaitt("#root > div > div.sc-bwzfXH.eOmgCJ > div.sc-hrWEMg.glaAdg > div.sc-eTuwsz.bZiLVd > div:nth-child(3) > div.sc-cMhqgX.eDFKnr > button")
    if thing.text == 'Water':
        #close 
        awaitt('#root > div > div:nth-child(3) > div > div:nth-child(2) > div > div > div.sc-dxgOiQ.knXTJr > button')
        #soda
        awaitt('#root > div > div.sc-bwzfXH.eOmgCJ > div.sc-kvZOFW.xcnRO > div > div > div.sc-gUlUPW.loQmCT > div:nth-child(8) > div > div:nth-child(1) > button')
        #some soda 
        awaitt(f'#Toggle-{random.randint(5,10)}')
        #for homeless
        sendkeys("#FieldWrapper-7","dar a las personas sin hogar y marcar como recogido")
        #10 times
        newquantity('#root > div > div:nth-child(3) > div > div:nth-child(2) > div > div > div.sc-kgoBCf.fadSlv > div > div > div > div > div > div.sc-dnqmqq.ibsFAU > div:nth-child(3) > button',10)
        #atc
        awaitt('#root > div > div:nth-child(3) > div > div:nth-child(2) > div > div > div.sc-kgoBCf.fadSlv > div > div > div > div > div > div.sc-hfLElm.VdQyN > button')
        #5$ thing
        awaitt('#root > div > div.sc-bwzfXH.eOmgCJ > div.sc-kvZOFW.xcnRO > div > div > div.sc-gUlUPW.loQmCT > div:nth-child(9) > div > div:nth-child(6) > button')
        #random option
        #{random.randint(13,14)}
        try:
            awaitt(f'#Toggle-{random.randint(13,14)}')
        except selenium.common.exceptions.TimeoutException:
            awaitt(f'#Toggle-{random.randint(14,15)}')
        #atc
        awaitt('#root > div > div:nth-child(3) > div > div:nth-child(2) > div > div > div.sc-kgoBCf.fadSlv > div > div > div > div > div > div.sc-hfLElm.VdQyN > button')
        #atc button
        awaitt("#root > div > div.sc-bwzfXH.eOmgCJ > div.sc-hrWEMg.glaAdg > div.sc-eTuwsz.bZiLVd > div:nth-child(3) > div.sc-cMhqgX.eDFKnr > button")
        pass
    time.sleep(5)
    browser.get('https://www.doordash.com/consumer/login/?next=/consumer/checkout/')
    time.sleep(3)
    if "https://identity.doordash.com/" in browser.current_url:
        browser.close()
        atc()
    else:
        atc.lemail = '#login-form > label:nth-child(1) > input'
        atc.lpass = '#login-form > label:nth-child(2) > div.Input_passwordHolder___15rJ5 > input'
        pass
def applypromo():
    awaitt('#root > div > div.sc-bwzfXH.eOmgCJ > div.sc-kvZOFW.xcnRO > div > div > div > div.sc-jdeSqf.cwHJIq > div:nth-child(4) > div.sc-fkyLDJ.dETZFY > div > button')
    sendkeys('#FieldWrapper-1','TRUMPCAST')
    awaitt('#root > div > div:nth-child(3) > div > div:nth-child(2) > div > div > div.sc-jzJRlG.bfjQBc > div.sc-cSHVUG.lmJbiU.sc-gZMcBi.NSlDj.sc-gzVnrw.hcQgsZ > div > div.sc-lnmtFM.fcBbLI.sc-dnqmqq.ibsFAU > div.sc-FQuPU.lkZlGn > button')
    try:
        awaitt('#root > div > div.sc-bwzfXH.eOmgCJ > div.sc-kvZOFW.xcnRO > div > div > div > div.sc-jdeSqf.cwHJIq > div:nth-child(4) > div.sc-fkyLDJ.dETZFY > div > button')
    except selenium.common.exceptions.TimeoutException:
        browser.refresh()
    awaitt('#root > div > div:nth-child(3) > div > div:nth-child(2) > div > div > div.sc-jzJRlG.bfjQBc > div.sc-cSHVUG.lmJbiU.sc-gZMcBi.NSlDj.sc-gzVnrw.hcQgsZ > div > div:nth-child(5) > div.sc-hSdWYo.cRKNjR > div')
    awaitt('#root > div > div:nth-child(3) > div > div:nth-child(2) > div > div > div.sc-jzJRlG.bfjQBc > div.sc-cSHVUG.lmJbiU.sc-gZMcBi.NSlDj.sc-gzVnrw.hcQgsZ > div > div:nth-child(4) > div.sc-hSdWYo.cRKNjR > div')
def rape(email,password):
    atc()
    sendkeys(atc.lemail,email)
    sendkeys(atc.lpass,password)
    inputtt.send_keys(Keys.ENTER)
    applypromo()
    # time.sleep(4)
    # browser.close()
# filepath = 'emails.txt'
# with open(filepath) as fp:
#    line = fp.readline()
#    cnt = 1
#    while line:
#        print('Line {}: {}'.format(cnt, line.strip()))
#        rape(line.strip(),'doordash')
#        line = fp.readline()
#        cnt += 1
rape('ickeido@aqueefdd.host','doordash')
# rape('MarianneGeorgia6@crackedaio.xyz','doordash')



#root > div > div.sc-bwzfXH.eOmgCJ > div.sc-kvZOFW.xcnRO > div > div > div.sc-gUlUPW.loQmCT > div:nth-child(8) > div > div:nth-child(4) > button
#root > div > div.sc-bwzfXH.eOmgCJ > div.sc-kvZOFW.xcnRO > div.sc-uJMKN.jhUCHQ > div > div.sc-gkfylT.jCZgxc > div:nth-child(7) > div > div:nth-child(4) > button > div > div > span > div > div > div > div > span


# thing = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#root > div > div.sc-bwzfXH.eOmgCJ > div.sc-kvZOFW.xcnRO > div.sc-uJMKN.jhUCHQ > div > div.sc-gkfylT.jCZgxc > div:nth-child(7) > div > div:nth-child(4) > button > div > div > span > div > div > div > div > span")))
#     # thing = browser.find_element_by_css_selector('#root > div > div.sc-bwzfXH.eOmgCJ > div.sc-kvZOFW.xcnRO > div.sc-uJMKN.jhUCHQ > div > div.sc-gkfylT.jCZgxc > div:nth-child(7) > div > div:nth-child(4) > button > div > div > span > div > div > div > div > span')
#     print(thing.text)
#     if thing.text == "Sweet Plantain (Platano Maduro)":
#         awaitt('#root > div > div.sc-bwzfXH.eOmgCJ > div.sc-kvZOFW.xcnRO > div > div > div.sc-gkfylT.jCZgxc > div:nth-child(8) > div > div:nth-child(4) > button')
#         #click the water
#         # awaitt('#root > div > div.sc-bwzfXH.eOmgCJ > div.sc-kvZOFW.xcnRO > div > div > div.sc-gkfylT.jCZgxc > div:nth-child(7) > div > div:nth-child(4) > button')
#         #say its for the homeless
#         sendkeys("#FieldWrapper-4","dar a las personas sin hogar y marcar como recogido")
#         #put 10 waters
#         newquantity('#root > div > div:nth-child(3) > div > div:nth-child(2) > div > div > div.sc-kgoBCf.fadSlv > div > div > div > div > div > div.sc-dnqmqq.ibsFAU > div:nth-child(3) > button',10)
#         #add to cart
#         awaitt('#root > div > div:nth-child(3) > div > div:nth-child(2) > div > div > div.sc-kgoBCf.fadSlv > div > div > div > div > div > div.sc-fguZLD.fzgXRK > button')
#         #cart button
#         awaitt("#root > div > div.sc-bwzfXH.eOmgCJ > div.sc-hrWEMg.glaAdg > div.sc-eTuwsz.bZiLVd > div:nth-child(3) > div.sc-cMhqgX.eDFKnr > button")
#         time.sleep(8)
#         browser.get('https://www.doordash.com/consumer/login/?next=/consumer/checkout/')
#         time.sleep(3)
#     else:
#         #click the water
#         awaitt('#root > div > div.sc-bwzfXH.eOmgCJ > div.sc-kvZOFW.xcnRO > div > div > div.sc-gkfylT.jCZgxc > div:nth-child(7) > div > div:nth-child(4) > button')
#         #say its for the homeless
#         sendkeys("#FieldWrapper-4","dar a las personas sin hogar y marcar como recogido")
#         #put 10 waters
#         newquantity('#root > div > div:nth-child(3) > div > div:nth-child(2) > div > div > div.sc-kgoBCf.fadSlv > div > div > div > div > div > div.sc-dnqmqq.ibsFAU > div:nth-child(3) > button',10)
#         #add to cart
#         awaitt('#root > div > div:nth-child(3) > div > div:nth-child(2) > div > div > div.sc-kgoBCf.fadSlv > div > div > div > div > div > div.sc-fguZLD.fzgXRK > button')
#         #cart button
#         awaitt("#root > div > div.sc-bwzfXH.eOmgCJ > div.sc-hrWEMg.glaAdg > div.sc-eTuwsz.bZiLVd > div:nth-child(3) > div.sc-cMhqgX.eDFKnr > button")
#         time.sleep(8)
#         browser.get('https://www.doordash.com/consumer/login/?next=/consumer/checkout/')
#         time.sleep(3)



