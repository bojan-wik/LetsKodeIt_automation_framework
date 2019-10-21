import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.Home.LoginPage import LoginPage
import unittest

class LoginTests(unittest.TestCase):

    def test_validLogin(self):
        baseUrl = "https://learn.letskodeit.com"
        driverLocation = "C:/Webdrivers/Chrome/77/chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseUrl)

        lp = LoginPage(driver)
        lp.login("test@email.com", "abcabc")

        userIcon = driver.find_element(By.XPATH, "//*[@id='navbar']/div/div/div/ul/li[4]/a/img")
        if userIcon is not None:
            print("Login successful")
        else:
            print("Login failed")

        # self.assertIsNotNone(userIcon, "Login failed")

chrome = LoginTests()
chrome.test_validLogin()