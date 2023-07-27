import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

welc = "Congratulations! You have successfully registered!"
def reg(link):
    with webdriver.Chrome() as driver:
        driver.get(link)
        driver.implicitly_wait(5)

        driver.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Jasur")
        driver.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("test@gmail.com")
        driver.find_element(By.CSS_SELECTOR, ".second_block .first").send_keys("+0048833933")
        driver.find_element(By.CSS_SELECTOR, ".second_block .second").send_keys("Tashkent")
        driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

        test_alert = driver.find_element(By.TAG_NAME, "h1")
        return test_alert.text
class TestPage(unittest.TestCase):
    def test_first_page(self):
        p1 = reg("https://suninjuly.github.io/registration1.html")
        self.assertEqual(p1, welc, "You are not registred")

    def test_second_page(self):
        p2 = reg("https://suninjuly.github.io/registration2.html")
        self.assertEqual(p2, welc, "You are not registred")
        
if __name__ == "__main__":
    unittest.main

