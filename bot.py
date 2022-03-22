import pyautogui
from selenium import webdriver
import time

user = int(input('Insira o Número da sua Matrícula: '))
senha = input('Insira a sua Senha: ')
codigo = int(input('Insira o Códgio da Paradinha: '))

navegador = webdriver.Chrome()
navegador.maximize_window()
navegador.get("https://plugadosead.fiqueligadonews.com.br/login")
time.sleep(4)
navegador.find_element_by_xpath('//*[@id="branch"]').send_keys('Bcc - Ribeirão Preto')
navegador.find_element_by_xpath('//*[@id="username"]').send_keys(user)
navegador.find_element_by_xpath('//*[@id="app"]/ng-component/div/section/div/div/div/div[2]/form/button').click()
time.sleep(2)
navegador.find_element_by_xpath('//*[@id="password"]').send_keys(senha)
navegador.find_element_by_xpath('//*[@id="app"]/ng-component/div/section/div/div/div/div[2]/form/button').click()
time.sleep(3)
navegador.find_element_by_xpath('//*[@id="navbar-mobile"]/ul[1]/li[1]/a').click()
time.sleep(1)
navegador.find_element_by_xpath('//*[@id="nav-professor-tab"]').click()
time.sleep(2)
navegador.find_element_by_xpath('/html/body/app-root/div/div/app-nav/div/div/div/div[3]/ul/li[2]/a').click()
time.sleep(1)
navegador.find_element_by_xpath('//*[@id="app"]/app-full-template/div/div/div[2]/app-professor-meus-cursos/div[1]/div[2]/form/div[1]/fieldset/input').send_keys(codigo)
pyautogui.hotkey('enter')
time.sleep(2)
navegador.find_element_by_xpath('//*[@id="course-wrapper"]/div/div/div[1]/a/img').click()
time.sleep(1)
navegador.find_element_by_xpath('/html/body/app-root/div/div/app-instructor-template/app-nav-instructor/div/div/ul/li[4]/a').click()
time.sleep(2)
navegador.find_element_by_xpath('/html/body/app-root/div/div/app-instructor-template/div/div/div[2]/app-default-page/div/div[2]/div[2]/div[2]/div/div/div[2]/a[1]').click()
time.sleep(4)
navegador.find_element_by_xpath('/html/body/app-root/div/div/app-instructor-template/div/div/div[2]/app-default-page/div/div[2]/div[2]/div[2]/div/div/div[2]/a[2]/span').click()
time.sleep(10)
navegador.find_element_by_xpath('/html/body/app-root/div/div/app-instructor-template/div/div/div[2]/app-default-page/div/div[2]/div[1]/div/div/div/div[2]/div/table/tbody/tr[1]/td[4]/a').click()


