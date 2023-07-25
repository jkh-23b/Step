import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

welc = "Congratulations! You have successfully registred!"
def reg(link):
    with webdriver.Chrome() as driver:
        driver.get(link)

        