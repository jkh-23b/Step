import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

class TestA(unittest.TestCase):
    def test_page1(self):
        driver.get("http://suninjuly.github.io/registration1.html")
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, "//input[@placeholder='Input your first name']").send_keys("Jasur")
        driver.find_element(By.XPATH, "//input[@placeholder='Input your last name']").send_keys("Khabibullaev")
        driver.find_element(By.XPATH, "//input[@placeholder='Input your email']").send_keys("test@gmail.com")
        driver.find_element(By.CSS_SELECTOR, ".second_block input.first").send_keys("+998991122233")
        driver.find_element(By.CSS_SELECTOR, ".second_block input.second").send_keys("Tashkent")
        driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        time.sleep(2)

        adding = driver.find_element(By.TAG_NAME, "h1").text
        adds = "Congratulations! You have successfully registered!"
        self.assertEqual(adding, adds, "Registration is failed")

    def test_page2(self):
        driver.get("http://suninjuly.github.io/registration2.html")
        driver.implicitly_wait(5)
        driver.find_element(By.CSS_SELECTOR, ".first_block input.second").send_keys("Khabibullaev")
        driver.find_element(By.CSS_SELECTOR, "[type='text'].third").send_keys("test@gmail.com")
        driver.find_element(By.CSS_SELECTOR, ".second_block input.first").send_keys("+998991122233")
        driver.find_element(By.CSS_SELECTOR, ".second_block input.second").send_keys("Tashkent")
        driver.find_element(By.CSS_SELECTOR, "button.btn").click()

        adding2 = driver.find_element(By.TAG_NAME, "h1").text
        adds2 = "Congratulations! You have successfully registered!"
        self.assertEqual(adding2, adds2, "Registration is failed")
        


if __name__ == "__main__":
    unittest.main()

driver.quit()
