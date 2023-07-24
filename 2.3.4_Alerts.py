import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://suninjuly.github.io/alert_accept.html")
time.sleep(2)

try:
    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    driver.switch_to.alert.accept()
    time.sleep(1)
    


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    num = driver.find_element(By.ID, "input_value")
    x = num.text
    res = calc(x)
    driver.find_element(By.ID, "answer").send_keys(res)
    driver.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(2)

    print(driver.switch_to.alert.text.split() [-1])
finally:
    time.sleep(2)
    driver.quit()
