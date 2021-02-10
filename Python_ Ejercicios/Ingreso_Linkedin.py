#Login con usuario y contraseña en Linkedin

import xlrd                   #Para leer archivos excel
import pandas
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait    #Llama a un subpaquete dentro de selenium , es para esperar
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException

excel_credenciales = 'C:\\Users\\silvina\\Documents\\Datos_Linkedin.xlsx'
df = pandas.read_excel(excel_credenciales)
user = df['usuario'][0]
psw = df['contraseña'][0]
url = 'https://www.linkedin.com/'

#Selectores
boton_iniciar_sesion = 'body > nav > div > a.nav__button-secondary'
ingreso_usuario = '#username'
ingreso_contrasenia = '#password'
boton_login = '#app__container > main > div:nth-child(2) > form > div.login__form_action_container > button'
error_contrasenia ='#error-for-password'
xpath_error_psw = '//*[@id="error-for-password"]'

#Abrir navegador
driver = webdriver.Chrome("C:\\chromedriver_win32\\chromedriver.exe")

#Maximizar pantalla
driver.maximize_window()
driver.get(url)

#Busco el elemento de Iniciar Sesion
driver.find_element_by_css_selector(boton_iniciar_sesion).click()

#Ahora nos logueamos, utilizo un bloque try-except para atrapar excepciones
try:
    driver.find_element_by_css_selector(ingreso_usuario).send_keys(user)
    driver.find_element_by_css_selector(ingreso_contrasenia).send_keys(psw)
    driver.find_element_by_css_selector(boton_login).click()
    driver.find_element_by_xpath(xpath_error_psw)
         
except Exception as ex:                     
    print(ex)
    print("Ingreso correcto a la página")
else:
    print("La contrasenia ingresada es incorrecta")     
 
#Le damos un tiempo de 3 segundos para que cargue la página
time.sleep(3)

#Cerramos el driver
driver.quit()
