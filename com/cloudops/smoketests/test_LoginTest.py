from com.cloudops.pagelib.LoginPage import LoginPage
from selenium import webdriver
import unittest

class LoginTests(unittest.TestCase):

    def test_Login(self):
        baseURL = "https://staging.cloudops.ai/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        lp = LoginPage(driver)
        lp.login("hemant.singh@sd2labs.com", "password")

        actual_user_id = lp.get_userid_on_homepage().text
        expected_id = "Hemant Uncle"
        if actual_user_id == expected_id:
            print("Login is successful")
        else:
            print("Login failed")


