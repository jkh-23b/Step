import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/selects1.html")
driver.maximize_window()
time.sleep(1)

def sums(x, y):
    return str(x + y)

a1 = driver.find_element(By.ID, "num1")
a = a1.text
x = int(a)

b1 = driver.find_element(By.ID, "num2")
b = b1.text
y = int(b)

res = sums(x, y)
print (res)

element = Select(driver.find_element(By.ID, "dropdown"))
element.select_by_visible_text(res)
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
time.sleep(1)
#     ловим алерт и забираем из него ответ
print(driver.switch_to.alert.text.split()[-1])

driver.quit()