import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://suninjuly.github.io/explicit_wait2.html")
driver.implicitly_wait(5)

try:
    price = WebDriverWait(driver, 13).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    driver.find_element(By.ID, "book").click()
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    num = driver.find_element(By.ID, "input_value")
    x = num.text
    res = calc(x)

    driver.find_element(By.ID, "answer").send_keys(res)
    driver.find_element(By.ID, "solve").click()
    print(driver.switch_to.alert.text.split() [-1])
    
finally:
    driver.quit()