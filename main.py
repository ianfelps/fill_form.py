from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import openpyxl

# navegar ate o site
driver = webdriver.Chrome()
driver.get('http://127.0.0.1:8000/')
sleep(3)

# extrair dados da planilha
dados = openpyxl.load_workbook('./dados.xlsx')
pagina_dados =dados['sheet1']

for linha in pagina_dados.iter_rows(min_row=2, values_only=True):
    nome, cpf, email, plano, adesao = linha

    # buscar elemento e preencher
    driver.find_element(By.ID, 'name').send_keys(nome)
    sleep(2)
    driver.find_element(By.ID, 'cpf').send_keys(cpf)
    sleep(2)
    driver.find_element(By.ID, 'e-mail').send_keys(email)
    sleep(2)
    driver.find_element(By.ID, 'inputState').send_keys(plano)
    sleep(2)
    driver.find_element(By.ID, 'data').send_keys(adesao)
    sleep(2)

    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    sleep(3)
    driver.find_element(By.XPATH, '//a[@href="/"]').click()
    sleep(3)

# site utilizado: https://github.com/ianfelps/sistema_academia