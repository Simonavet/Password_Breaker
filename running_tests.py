import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Login(unittest.TestCase):
    form = (By.LINK_TEXT, 'Form Authentication')

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.get('https://the-internet.herokuapp.com/')
        self.chrome.maximize_window()
        self.chrome.find_element(*self.form).click()

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_password_hacking(self):

        possibile_password = self.chrome.find_element(By.XPATH, '//h4').text
        pasword = possibile_password.split()

        for elem in pasword:
            self.chrome.find_element(By.ID, 'username').send_keys('tomsmith')
            self.chrome.find_element(By.ID, 'password').send_keys(elem)
            self.chrome.find_element(By.TAG_NAME, 'button').click()
            time.sleep(2)
            if self.chrome.current_url != 'https://the-internet.herokuapp.com/secure':
                print('I could not find the password')
            else:
                print(f'The password is:', [elem])
                break
            self.chrome.find_element(By.ID, 'password').clear()