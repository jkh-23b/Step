import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://suninjuly.github.io/get_attribute.html")
time.sleep(1)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

element = driver.find_element(By.ID, "treasure")
x = element.get_attribute('valuex')
res = calc(x)


try:
    driver.find_element(By.ID, "answer").send_keys(res)
    time.sleep(1)

    driver.find_element(By.ID, "robotCheckbox").click()
    time.sleep(1)

    driver.find_element(By.ID, "robotsRule").click()
    time.sleep(1)

    driver.find_element(By.CSS_SELECTOR, "button.btn-default").click()
    time.sleep(3)

finally:
    time.sleep(2)
    driver.quit()