import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
driver.get(link)
time.sleep(1)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

st = driver.find_element(By.ID, "input_value")
x = st.text
res = calc(x)

try:
    driver.find_element(By.ID, "answer").send_keys(res)
    chec = driver.find_element(By.ID, "robotCheckbox")

    driver.execute_script("return arguments[0].scrollIntoView(true);", chec)
    chec.click()
    driver.find_element(By.ID, "robotsRule").click()
    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    

    print(driver.switch_to.alert.text.split()[-1])

finally:
    time.sleep(3)
    driver.quit()




