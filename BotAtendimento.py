
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

# Config
url_site = "https://www.atendimento.dropdesk.com.br"
email_login = "matheus.solon@izzyway.com.br"
senha_login = "matheusSC12"
analista_1 = "PEDRO HENRIQUE"

# Inicializa o navegador
driver = webdriver.Chrome()

# Abre a página
driver.get(
    url_site
    )

# Localiza os campos de email e senha e insere as informações e faz o login
campo_email = driver.find_element(
    By.XPATH,'//*[@id="root"]/div[2]/div[2]/div[2]/form/div[2]/div[1]/input'
    ).send_keys(email_login)

campo_senha = driver.find_element(
    By.XPATH,'//*[@id="root"]/div[2]/div[2]/div[2]/form/div[2]/div[2]/input'
    ).send_keys(senha_login)

login_button = driver.find_element(
    By.XPATH, '//*[@id="root"]/div[2]/div[2]/div[2]/form/div[2]/div[4]/button'
    ).click()

time.sleep(3)

#vai ate a area de atendimento > espera
atendimento_area = driver.find_element(
    By.XPATH, '//*[@id="root"]/div[2]/div[1]/div[1]/div/div[2]/nav/ul/li[3]/div'
    ).click()

atendimento_espera = driver.find_element(
    By.XPATH, '//*[@id="react-tabs-2"]'
    ).click()

atendimento_chamado = driver.find_element(
    By.XPATH, '//*[@id="react-tabs-3"]/div/div[1]'
    ).click()

atendimento_transferencia = driver.find_element(
    By.XPATH, '//*[@id="root"]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[3]/div/i[2]'
    ).click()  
#seleciona o analista pela variavel ja determinada  

campo_atendente = driver.find_element(
    By.CSS_SELECTOR, 'input.sc-pBzeH.bWPBsz'
).send_keys(analista_1)

selecionar_analista = driver.find_element(
    By.CLASS_NAME, 'select-search__select'
    ).click()

transferencia_analista = driver.find_element(
   By.CSS_SELECTOR, 'button.sc-pIWiK.jfEInO'
   ).click()


time.sleep(3)
