from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import *

class SeleniumDriver():

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        if locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        if locatorType == "css":
            return By.CSS_SELECTOR
        if locatorType == "class":
            return By.CLASS_NAME
        if locatorType == "link":
            return By.LINK_TEXT
        else:
            print("Locator type {} is not correct/supported".format(locatorType))
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            print("Element found with locator: {}, locator type: {}".format(locator, locatorType))
        except:
            print("Element not found with locator: {}, locator type: {}".format(locator, locatorType))
        return element

    def elementClick(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            print("Clicked on the element with locator: {}, locator type: {}".format(locator, locatorType))
        except:
            print("Cannot click on the element with locator: {}, locator type: {}".format(locator, locatorType))
            print_stack()

    def sendKeys(self, data, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            element.click()
            print("Sent data on the element with locator: {}, locator type: {}".format(locator, locatorType))
        except:
            print("Cannot send data on the element with locator: {}, locator type: {}".format(locator, locatorType))
            print_stack()

    def isElementPresent(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                print("Element found")
                return True
            else:
                print("Element not found")
                return False
        except:
            print("Element not found")
            return False

    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                print("Element found")
                return True
            else:
                print("Element not found")
                return False
        except:
            print("Element not found")
            return False

    def waitForElement(self, locator, locatorType="id",
                       timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            print("Waiting for maximum :: {} :: seconds for element to be clickable"
                  .format(str(timeout)))
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(expected_conditions.element_to_be_clickable((byType, "stopFilter_stops-0")))
            print("Element appeared on the web page")
        except:
            print("Element not appeared on the web page")
            print_stack()
        return element