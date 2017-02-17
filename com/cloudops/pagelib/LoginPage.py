from com.cloudops.genericlib.SolventSelenium import SolventSelenium

class LoginPage(SolventSelenium):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _username_field = "//input[@id='user_email']"
    _password_field = "//input[@id='user_password']"
    _login_button = "//button[text()='Login']"
    _login_link = "//a[@href='/login']"
    _userid_on_homepage = "//button[@class='dropdown-toggle']//div[@class='label']//span[@class='wel']"


    def enterUsername(self, username):
        self.sendKeys(username, self._username_field, locatorType="xpath")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, locatorType="xpath")

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def click_on_loginlink(self):
        self.elementClick(self._login_link, locatorType="xpath")

    def get_userid_on_homepage(self):
        return self.getElement(self._userid_on_homepage, locatorType="xpath")

    def login(self, username, password):
        #self.waitForElement(SignupPage.login_link, locatorType="xpath")
        #SignupPage.click_on_loginlink()
        self.waitForElement(self._login_link, locatorType="xpath")
        self.click_on_loginlink()
        self.waitForElement(self._login_button, locatorType="xpath")
        self.enterUsername(username)
        self.enterPassword(password)
        self.clickLoginButton()
        self.waitForElement(self._userid_on_homepage, locatorType="xpath")

