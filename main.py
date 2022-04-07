from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def criar_navegador():

    driver_path = Service("C:/Users/sasuk/AppData/Local/Programs/Python/Python39/chromedriver.exe")
    brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

    options = Options()
    options.binary_location = brave_path

    navegador = webdriver.Chrome(service=driver_path, options=options)
    return navegador


navegador = criar_navegador()
navegador.minimize_window()
navegador.get("https://www.google.com/")
# pesquisa a cotaçao no google
navegador.find_element(By.XPATH,
                       '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação do dolar')

# clica em pesquisar
navegador.find_element(By.XPATH,
                       '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

# pega a cotação do dolar
cotacao_dolar = navegador.find_element(
    By.XPATH,
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'
    ).get_attribute('data-value')


# cotação do ouro
navegador.get("https://www.melhorcambio.com/ouro-hoje")

# pegar cotação do ouro
cotacao_ouro = navegador.find_element(By.XPATH,
                       '//*[@id="comercial"]').get_attribute('value')

cotacao_ouro = cotacao_ouro.replace(',', '.')
navegador.quit()

print(f"cotação do dolar: {cotacao_dolar}")
print(f"cotação do ouro: {cotacao_ouro}")
