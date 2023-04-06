import urllib.request
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
import time

service = Service('./chromedriver.exe')

def civil(pessoa):
    driver = webdriver.Chrome(service=service)
    driver.get('https://www.tjrs.jus.br/novo/processos-e-servicos/servicos-processuais/emissao-de-antecedentes-e-certidoes/')

    driver.switch_to.frame(0)

    tipoDocumento_select = driver.find_element(By.ID,'tipoDocumento')
    select = Select(tipoDocumento_select)
    select.select_by_visible_text('Certidão Judicial Cível Negativa de 1º Grau')

    if pessoa == '0' :
        radio = driver.find_element(By.XPATH,'/html/body/div[1]/form/div[3]/input[1]')
        radio.click()
        fillFormSimples(driver)
    else :
        fillFormJuridica(driver)


    driver.switch_to.default_content()

    main_window_handle = driver.current_window_handle
    all_window_handles = driver.window_handles

    for window_handle in all_window_handles:
        if window_handle != main_window_handle:
            driver.switch_to.window(window_handle)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.number_of_windows_to_be(2))


    urllib.request.urlretrieve(driver.current_url, 'civil.pdf')

    driver.close()

def criminal() :
    driver = webdriver.Chrome(service=service)
    driver.get('https://www.tjrs.jus.br/novo/processos-e-servicos/servicos-processuais/emissao-de-antecedentes-e-certidoes/')

    driver.switch_to.frame(0)

    tipoDocumento_select = driver.find_element(By.ID,'tipoDocumento')
    select = Select(tipoDocumento_select)
    select.select_by_visible_text('Certidão Judicial Criminal Negativa')

    fillFormSimples(driver)

    driver.switch_to.default_content()

    main_window_handle = driver.current_window_handle
    all_window_handles = driver.window_handles

    for window_handle in all_window_handles:
        if window_handle != main_window_handle:
            driver.switch_to.window(window_handle)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.number_of_windows_to_be(2))


    urllib.request.urlretrieve(driver.current_url, 'criminal.pdf')

    driver.close()

def fillFormJuridica(driver):
    radio = driver.find_element(By.XPATH,'/html/body/div[1]/form/div[3]/input[2]')
    radio.click()

    name_input = driver.find_element(By.ID,'nome')
    name_input.send_keys('John Doe')

    endereco_input = driver.find_element(By.ID,'cnpj')
    endereco_input.send_keys('77566535000159')

    endereco_input = driver.find_element(By.ID,'endereco')
    endereco_input.send_keys('felipe cortez')

    submit_button = driver.find_element(By.ID,'gerarDocumento')
    submit_button.click()

def fillFormSimples(driver):
    name_input = driver.find_element(By.ID,'nome')
    name_input.send_keys('John Doe')

    sexo_select = driver.find_element(By.NAME,'sexo')
    select = Select(sexo_select)
    select.select_by_value('F')

    cpf_input = driver.find_element(By.ID,'cpf')
    cpf_input.send_keys('08564547457')

    nomeMae_input = driver.find_element(By.ID,'nomeMae')
    nomeMae_input.send_keys('Fulana de Tal')

    nomePai_input = driver.find_element(By.ID,'nomePai')
    nomePai_input.send_keys('Fulano de Tal')

    dataNascimento_input = driver.find_element(By.ID,'dataNascimento')
    dataNascimento_input.send_keys('12/08/1999')

    nacionalidade_select = driver.find_element(By.NAME,'nacionalidade')
    select = Select(nacionalidade_select)
    select.select_by_visible_text('Brasileiro')

    rg_input = driver.find_element(By.ID,'rg')
    rg_input.send_keys('265410010')

    orgao_input = driver.find_element(By.ID,'orgaoExpedidor')
    orgao_input.send_keys('ssp')

    ufrg_select = driver.find_element(By.ID,'ufRg')
    select = Select(ufrg_select)
    select.select_by_value('SP')

    endereco_input = driver.find_element(By.ID,'endereco')
    endereco_input.send_keys('felipe cortez')

    submit_button = driver.find_element(By.ID,'gerarDocumento')
    submit_button.click()

if __name__ == "__main__":
    # script bem simples, com preenchimento de form com dados fixos... mas facilmente escalonavel. 
    tipoCertificado = input('escolha o certificado: negativa cível de 1° grau(0) ou criminal negativa(1)' )
    if tipoCertificado == '1' :
        criminal()
    else :
        tipoPessoa = input('escolha: Pessoa Física(0) ou Pessoa Jurídica(1)' )
        if tipoPessoa == '0' :
            civil(0)
        else : 
            civil(1)
