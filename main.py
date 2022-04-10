from time import sleep
import os
from dotenv import load_dotenv
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


def criar_navegador():
    driver_path = Service("C:/Users/sasuk/AppData/Local/Programs/Python/Python39/chromedriver.exe")
    brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

    options = Options()
    options.binary_location = brave_path

    navegador = webdriver.Chrome(service=driver_path, options=options)
    return navegador


def entrar_no_savi(navegador):
    navegador.get("https://farid.savi.cc/login.php")


def logar_no_savi(navegador):
    savi_usuario = os.getenv('savi_user')
    savi_senha = os.getenv('savi_psw')
    navegador.find_element(By.XPATH,
                           '/html/body/div[2]/div[2]/form/div[1]/input').send_keys(savi_usuario)
    navegador.find_element(By.XPATH,
                           '/html/body/div[2]/div[2]/form/div[2]/input').send_keys(savi_senha)
    navegador.find_element(By.XPATH,
                           '/html/body/div[2]/div[2]/form/div[2]/input').send_keys(Keys.ENTER)
    navegador.get('https://farid.savi.cc/usuarios')


def localizar_usuario(navegador, usuario_a_encontrar):
    navegador.find_element(By.XPATH,
                           '//*[@id="usuarios1_filter"]/label/input').send_keys(usuario_a_encontrar)


def editar_usuario(wait):
    button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="9472"]')))
    button.click()


def editar_senha(navegador, usuario_a_encontrar, wait):
    data_de_hoje = datetime.today()
    data_de_hoje_formata = data_de_hoje.strftime('%d%m%y')
    nova_senha = usuario_a_encontrar[0].upper()
    nova_senha = nova_senha + data_de_hoje_formata

    senha_preencher = wait.until(lambda navegador: navegador.find_element(By.XPATH,
                                                                          '/html/body/div[2]/div[3]/div/div/div['
                                                                          '2]/form/div/div/div[2]/div/div['
                                                                          '3]/div/input'))
    senha_preencher.send_keys(nova_senha)


def trocar_a_senha(usuario):
    load_dotenv()
    navegador = criar_navegador()
    navegador.maximize_window()
    # entra no savi
    entrar_no_savi(navegador)
    # fazer login no savi
    logar_no_savi(navegador)
    # localizar usuário
    usuario_a_encontrar = usuario
    localizar_usuario(navegador, usuario_a_encontrar)
    # editar senha
    wait = WebDriverWait(navegador, 20)
    editar_usuario(wait)
    editar_senha(navegador=navegador, wait=wait, usuario_a_encontrar=usuario_a_encontrar)
    print("editado")


#trocar_a_senha('gleiton')
usuario = 'teste da silva'
usuario = usuario.title()
email_user = 'teste@farid.com.br'
senha = '123'
load_dotenv()
navegador = criar_navegador()
navegador.maximize_window()
entrar_no_savi(navegador)
logar_no_savi(navegador)
wait = WebDriverWait(navegador, 25)
button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="conteudo"]/section[2]/div/ul/li[11]/button[2]')))
button.click()

sleep(5)
nome_field = navegador.find_element(By.XPATH, '//*[@id="cadastrar_usuario_form"]/div[1]/div/input')
nome_field.send_keys(usuario)

email_field = wait.until(lambda navegador: navegador.find_element(By.XPATH,
                                                                  '/html/body/div[2]/div[2]/div/div/div[2]/div/div[2]/div/form/div[2]/div/input'))
email_field.send_keys(email_user)

senha_field = wait.until(lambda navegador: navegador.find_element(By.XPATH,
                                                                  '/html/body/div[2]/div[2]/div/div/div[2]/div/div[2]/div/form/div[3]/div/input'))

senha_field.send_keys(senha)

select_field_unidade = navegador.find_element(By.XPATH, '//*[@id="cadastrar_usuario_form"]/div[8]/div/span/span[1]/span')
select_field_unidade.send_keys("Todas Unidades")
select_field_unidade2 = navegador.find_element(By.XPATH, '/html/body/span/span/span[1]/input')
select_field_unidade2.send_keys("Todas Unidades")
sleep(2)
select_field_unidade.send_keys(Keys.ENTER)
select_field_unidade2.send_keys(Keys.ENTER)

select_field_tipo_de_acesso = Select(navegador.find_element(By.ID, 'select2-acesso-9e-container'))
select_field_tipo_de_acesso.select_by_value('0')

