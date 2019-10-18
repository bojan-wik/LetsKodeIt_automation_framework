import os
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginTests():

    def test_validLogin(self):
        baseUrl = "https://learn.letskodeit.com"
        driverLocation = "C:/Webdrivers/Chrome/77/chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseUrl)

        loginLink = driver.find_element(By.LINK_TEXT, "Login")
        loginLink.click()