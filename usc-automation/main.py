from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys


import os 
from dotenv import load_dotenv

import time

load_dotenv()

user = os.getenv("User")
password = os.getenv("Password")
url = os.getenv("Link")
url_calendario = os.getenv("Link_calendario")



options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

driver.get(url)


#-Login-
username_txtbox = driver.find_element(By.ID, "username").send_keys(user)
password_txtbox = driver.find_element(By.ID, "password").send_keys(password)
password_txtbox = driver.find_element(By.ID, "password").send_keys(Keys.ENTER)

time.sleep(5)

# Obtener todos los cursos
cursos = driver.find_elements(By.CLASS_NAME, "mc_content_list")

# Lista para almacenar la información
cursos_info = []

# Recorrer cada curso y extraer su información
for curso in cursos:
    try:
        titulo = curso.find_element(By.CLASS_NAME, "title").text
        departamento = curso.find_element(By.CLASS_NAME, "subtitle").text
        cursos_info.append({"titulo": titulo, "departamento": departamento})
    except Exception as e:
        print(f"Error al obtener datos de un curso: {e}")





for curso in cursos_info:
    print(f"📌 {curso['titulo']} - {curso['departamento']}")

driver.get(url_calendario)

tareas_lista = []
tareas = driver.find_elements(By.CLASS_NAME, "row event_lists p0")

for tarea in tareas:
    try:
        titulo = tarea.find_element(By.XPATH, "//*[@id=\"yui_3_18_1_1_1742487331958_24\"]/h3").text

        detalles = tarea.find_element(By.XPATH, "//*[@id=\"yui_3_18_1_1_1742487331958_24\"]/p[2]")

        fecha = tarea.find_element(By.XPATH, "//*[@id=\"yui_3_18_1_1_1742487331958_24\"]/ul/li[1]/a")

        tareas_lista.append(f"Titulo: {titulo},\nDetalles: {detalles}\nFecha: {fecha}")
    except Exception as e:
        print(f"Error al obtener datos de una tarea: {e}")
time.sleep(10)
print(tareas_lista)