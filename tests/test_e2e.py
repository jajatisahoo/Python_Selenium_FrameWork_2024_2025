import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utilities.BaseClass import BaseClass


# https://rahulshettyacademy.com/angularpractice
class TestOne(BaseClass):

    def test_e2e(self):
        self.driver.get("https://www.saucedemo.com/")
        wait = WebDriverWait(self.driver, 10)
        self.driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")

        # Find the password input and enter the password
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")

        # Click the login button
        #This is for testing purposes
        self.driver.find_element(By.XPATH, "//input[@id='login-button']").click()
