from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from captchaSolver import solveCaptcha
import time
import requests

service = Service('./chromedriver.exe')

captchaAPIkey = 'fe2c5765edde2868be261a83c635a416'

driver = webdriver.Chrome(service=service)
driver.get('https://pje.trt4.jus.br/certidoes/trabalhista/emissao')



result = solveCaptcha('6LeFj3QaAAAAAIhQt27bGh0XQks00PmVXz_kYQRN', 'https://pje.trt4.jus.br/certidoes/trabalhista/emissao', captchaAPIkey)
print(result)
code = result['code']

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,'/html/body/pje-root/main/pje-emissor-certidao-trabalhista/section/form/mat-card/mat-card-content/ngx-recaptcha2/div/div/div/textarea'))
)
driver.execute_script("document.getElementById('g-recaptcha-response').innerHTML = " + "'" +  code + "'")

# response = requests.get('https://www.google.com/recaptcha/api2/userverify', params={'k': '6LeFj3QaAAAAAIhQt27bGh0XQks00PmVXz_kYQRN', 'response': code})


radio_nome = driver.find_element(By.XPATH,'/html/body/pje-root/main/pje-emissor-certidao-trabalhista/section/form/mat-card/mat-card-content/p[1]/mat-radio-group/mat-radio-button[3]/label/div[1]/input')
driver.execute_script("arguments[0].click();", radio_nome)

name_input = driver.find_element(By.XPATH,'/html/body/pje-root/main/pje-emissor-certidao-trabalhista/section/form/mat-card/mat-card-content/p[2]/mat-form-field/div/div[1]/div/input')
name_input.send_keys('teste')


time.sleep(10)

# if response.status_code == 200 and response.json().get('success'):
#Resolução do captcha feita, mas não consigo enviar o form(Bloqueado a não ser que clique no captcha)
form = driver.find_element(By.XPATH,'/html/body/pje-root/main/pje-emissor-certidao-trabalhista/section/form')
form.submit()









