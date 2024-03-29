from selenium.webdriver.common.by import By
from Base.SeleniumDriver import SeleniumDriver

class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"
    '''
    def getLoginLink(self):
        return self.driver.find_element(By.LINK_TEXT, self._login_link)

    def getEmailField(self):
        return self.driver.find_element(By.ID, self._email_field)

    def getPasswordField(self):
        return self.driver.find_element(By.ID, self._password_field)

    def getLoginButton(self):
        return self.driver.find_element(By.NAME, self._login_button)
    '''
    def clickLoginLink(self):
        # self.getLoginLink().click()
        self.elementClick(self._login_link, locatorType="link")

    def enterEmail(self, email):
        # self.getEmailField().send_keys(email)
        self.sendKeys(email, self._email_field, locatorType="id")

    def enterPassword(self, password):
        # self.getPasswordField(self, password)
        self.sendKeys(password, self._password_field, locatorType="id")

    def clickLoginButton(self):
        # self.getLoginButton(self).click()
        self.elementClick(self._login_button, locatorType="name")

    def login(self, email, password):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()