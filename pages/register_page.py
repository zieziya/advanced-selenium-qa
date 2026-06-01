from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegisterPage(BasePage):

    URL = "https://demoqa.com/register"

    FIRST_NAME = (By.ID, "firstname")
    LAST_NAME = (By.ID, "lastname")
    USERNAME = (By.ID, "userName")
    PASSWORD = (By.ID, "password")
    REGISTER_BUTTON = (By.ID, "register")

    def navigate(self):
        self.open(self.URL)

    def fill_form(
        self,
        firstname,
        lastname,
        username,
        password
    ):
        self.type(self.FIRST_NAME, firstname)
        self.type(self.LAST_NAME, lastname)
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)

    def click_register(self):
        self.click(self.REGISTER_BUTTON)

    def register(
        self,
        firstname,
        lastname,
        username,
        password
    ):
        self.navigate()

        self.fill_form(
            firstname,
            lastname,
            username,
            password
        )

        self.click_register()