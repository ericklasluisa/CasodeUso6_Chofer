import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import os

# Configuración del navegador
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--disable-extensions')
options.add_argument('--no-sandbox')
options.add_argument('--disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-browser-side-navigation')
options.add_argument('--disable-gpu')

def take_screenshot(context, step_name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_dir = "screenshots"
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    screenshot_name = os.path.join(screenshot_dir, f"{step_name}_{timestamp}.png")
    context.driver.save_screenshot(screenshot_name)
    context.pdf.add_screenshot(screenshot_name, step_name)
    print(f"Screenshot taken: {screenshot_name}")
    return screenshot_name

def mark_step_as_failed(context, step_name, exception):
    print(f"Error in '{step_name}': {exception}")
    raise Exception(f"Step failed: {step_name}. Error: {exception}")

def mark_step_as_passed(context, step_name):
    print(f"Step passed: {step_name}")

@given('Se inicia el navegador actualizar chofer')
def iniciarNavegador(context):
    context.driver = webdriver.Chrome(options=options)
    context.failed_steps = []
    print("Browser started")

@when('Entra a la seccion actualizar chofer')
def asignar(context):
    try:
        context.driver.maximize_window()
        context.driver.get("C:\\Users\\erick\\Desktop\\ESPE\\QUINTO SEMESTRE\\REQUISITOS\\PRUEBAS-RF\\CU6\\Chofer\\ActualizarChofer.html")
        take_screenshot(context, '1. Entra a la seccion actualizar chofer')
        print("Entered 'Chofer' section")
    except Exception as e:
        mark_step_as_failed(context, 'entra_seccion_chofer', e)

@when('Aplasta el icono de editar chofer')
def aplastar_boton_editar(context):
    try:
        editar_button = context.driver.find_element(By.XPATH, '//*[@id="editar-0"]')
        editar_button.click()
        take_screenshot(context, '2. Clickar el boton editar')
    except Exception as e:
        mark_step_as_failed(context, 'aplastar_boton_editar', e)

@when('Actualizar en chofer el campo Nombre {nombre}')
def actualizar_nombre(context, nombre):
    try:
        nombre_field = context.driver.find_element(By.XPATH, '//*[@id="choferNombre"]')
        nombre_field.clear()
        nombre_field.send_keys(nombre)
        take_screenshot(context, '3. Actualizar en chofer el campo Nombre')
    except Exception as e:
        mark_step_as_failed(context, 'actualizar_nombre', e)

@when('Actualizar en chofer el campo Apellido {apellido}')
def actualizar_apellido(context, apellido):
    try:
        apellido_field = context.driver.find_element(By.XPATH, '//*[@id="choferApellido"]')
        apellido_field.clear()
        apellido_field.send_keys(apellido)
        take_screenshot(context, '4. Actualizar en chofer el campo Apellido')
    except Exception as e:
        mark_step_as_failed(context, 'actualizar_apellido', e)

@when('Actualizar en chofer el campo Numero {numero}')
def actualizar_numero(context, numero):
    try:
        numero_field = context.driver.find_element(By.XPATH, '//*[@id="choferNumero"]')
        numero_field.clear()
        numero_field.send_keys(numero)
        take_screenshot(context, '7. Actualizar el campo Número')
    except Exception as e:
        mark_step_as_failed(context, 'actualizar_numero', e)

@when('Seleccionar en chofer el tipo de licencia {licencia}')
def seleccionar_licencia(context, licencia):
    try:
        licencia_dropdown = Select(context.driver.find_element(By.XPATH, '//*[@id="choferLicencia"]'))
        licencia_dropdown.select_by_visible_text(licencia)
        take_screenshot(context, '8. Seleccionar en chofer el tipo de licencia')
    except Exception as e:
        mark_step_as_failed(context, 'seleccionar_licencia', e)

@when('Seleccionar en chofer el tipo de sangre {sangre}')
def seleccionar_sangre(context, sangre):
    try:
        sangre_dropdown = Select(context.driver.find_element(By.XPATH, '//*[@id="choferSangre"]'))
        sangre_dropdown.select_by_visible_text(sangre)
        take_screenshot(context, '8. Seleccionar en chofer el tipo de sangre')
    except Exception as e:
        mark_step_as_failed(context, 'seleccionar_sangre', e)

@then('Aplastar el boton para editar chofer')
def aplastar_editar_chofer(context):
    try:
        guardar_button = context.driver.find_element(By.XPATH, '//*[@id="editChoferForm"]/button')
        time.sleep(1)
        guardar_button.click()
        time.sleep(1)
        take_screenshot(context, '11. Aplastar el boton para editar chofer')
        print("Chofer editado")
    except Exception as e:
        mark_step_as_failed(context, 'aplastar_guardar_chofer', e)

@then('Visualizar alerta confirmacion actualizar chofer')
def verificarMensaje(context):
    try:
        # Esperar a que el modal de confirmación aparezca
        WebDriverWait(context.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div'))
        )
        confirmation_message = context.driver.find_element(By.XPATH, '/html/body/div[7]/div')
        # Si el elemento se encuentra, el paso es exitoso
        time.sleep(1)
        take_screenshot(context, '5. Observar el mensaje de confirmacion')
        mark_step_as_passed(context, 'verificar_mensaje')
    except Exception as e:
        # Si ocurre una excepción, el paso falla
        mark_step_as_failed(context, 'verificar_mensaje', e)
