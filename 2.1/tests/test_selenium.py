import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestYandexAuthorization(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.login = 'sdgsdgsdg@yandex.ru'
        self.pass_word = 'password'

    @unittest.expectedFailure
    def test_login_to_yandex(self):
        driver = self.driver
        driver.get("https://passport.yandex.ru/auth/")
        self.assertIn("Авторизация", driver.title)

        input_login = driver.find_element_by_name("login")
        input_login.send_keys(self.login)
        input_login.send_keys(Keys.RETURN)

        driver.implicitly_wait(30)
        input_password = driver.find_element_by_name('passwd')
        input_password.send_keys(self.pass_word)
        input_password.send_keys(Keys.RETURN)

        driver.implicitly_wait(30)
        autorization_error = driver.find_element_by_class_name('passp-form-field__error')
        self.assertNotEqual(autorization_error.text, 'Неверный пароль')
