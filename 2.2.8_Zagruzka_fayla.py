import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://suninjuly.github.io/file_input.html")
time.sleep(1)

try:
    driver.find_element(By.NAME, 'firstname').send_keys("Jasur")
    driver.find_element(By.NAME, "lastname").send_keys("Khabibullaev")
    driver.find_element(By.NAME, "email").send_keys("test@gmail.com")
    time.sleep(1)

    # file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '2.1.5_Get_attribute.py')
    current_dir = os.path.abspath(os.path.dirname(__file__)) #получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, "2.1.5_Get_attribute.py") #Добавляем к этому пути имя файла
    driver.find_element(By.ID, "file").send_keys(file_path)

    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    time.sleep(2)

    print(driver.switch_to.alert.text.split()[-1])

finally:
    time.sleep(5)
    driver.quit()