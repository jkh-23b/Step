import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://suninjuly.github.io/redirect_accept.html")

driver.implicitly_wait(3)

try:
    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    driver.switch_to.window(driver.window_handles[1])
    
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    elem = driver.find_element(By.ID, "input_value")
    x = elem.text
    res = calc(x)

    driver.find_element(By.ID, "answer").send_keys(res)
    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    print(driver.switch_to.alert.text.split() [-1])

finally:
    driver.quit()