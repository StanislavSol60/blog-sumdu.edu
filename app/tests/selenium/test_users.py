from selenium import webdriver
from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.set_window_size(1776, 945)

    def click_login_link(self):
        self.driver.find_element(By.LINK_TEXT, "Login").click()

    def click_sign_up_link(self):
        self.driver.find_element(By.LINK_TEXT, "Sign Up").click()

    def click_profile_link(self):
        self.driver.find_element(By.LINK_TEXT, "Profile").click()

    def click_logout_link(self):
        self.driver.find_element(By.LINK_TEXT, "Logout").click()


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        email_field = self.driver.find_element(By.ID, "email")
        email_field.click()
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.driver.find_element(By.ID, "password")
        password_field.click()
        password_field.send_keys(password)

    def click_button(self):
        self.driver.find_element(By.CSS_SELECTOR, ".button").click()

    def click_forgot_password_link(self):
        self.driver.find_element(By.LINK_TEXT, "Forgot Password?").click()


class SignUpPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        email_field = self.driver.find_element(By.ID, "email")
        email_field.click()
        email_field.send_keys(email)

    def enter_name(self, name):
        name_field = self.driver.find_element(By.ID, "name")
        name_field.click()
        name_field.send_keys(name)

    def enter_password(self, password):
        password_field = self.driver.find_element(By.ID, "password")
        password_field.click()
        password_field.send_keys(password)

    def enter_confirm_password(self, confirm_password):
        confirm_password_field = self.driver.find_element(By.ID, "confirm_password")
        confirm_password_field.click()
        confirm_password_field.send_keys(confirm_password)

    def click_button(self):
        self.driver.find_element(By.CSS_SELECTOR, ".button").click()


class ProfilePage:
    def __init__(self, driver):
        self.driver = driver

    def enter_name(self, name):
        name_field = self.driver.find_element(By.ID, "name")
        name_field.click()
        name_field.send_keys(name)

    def enter_date_of_birth(self, date_of_birth):
        date_of_birth_field = self.driver.find_element(By.ID, "date_of_birth")
        date_of_birth_field.click()
        date_of_birth_field.send_keys(date_of_birth)

    def click_button(self):
        self.driver.find_element(By.CSS_SELECTOR, ".button").click()

    def select_interest(self):
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) > label").click()


class ForgotPasswordPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        email_field = self.driver.find_element(By.ID, "email")
        email_field.click()
        email_field.send_keys(email)

    def click_button(self):
        self.driver.find_element(By.CSS_SELECTOR, ".button").click()


class TestUsers:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.sign_up_page = SignUpPage(self.driver)
        self.profile_page = ProfilePage(self.driver)
        self.forgot_password_page = ForgotPasswordPage(self.driver)

    def teardown_method(self, method):
        self.driver.quit()

    def test_users(self):
        self.home_page.open()
        self.home_page.click_login_link()

        self.login_page.enter_email("test.users@gmail.com")
        self.login_page.enter_password("12345678")
        self.login_page.click_button()

        self.login_page.enter_password("12345678")
        self.login_page.click_button()

        self.home_page.click_sign_up_link()

        self.sign_up_page.enter_email("test.users@gmail.com")
        self.sign_up_page.enter_name("test users")
        self.sign_up_page.click_button()

        self.sign_up_page.enter_password("12345678")
        self.sign_up_page.enter_confirm_password("12345678")
        self.sign_up_page.click_button()

        self.login_page.enter_email("test.users@gmail.com")
        self.login_page.enter_password("12345678")
        self.login_page.click_button()

        self.home_page.click_profile_link()

        self.profile_page.enter_name("Test Users")
        self.profile_page.enter_date_of_birth("2023-05-26")
        self.profile_page.click_button()

        self.profile_page.enter_date_of_birth("2023-05-18")
        self.profile_page.click_button()

        self.profile_page.enter_name("Test Users")
        self.profile_page.click_button()

        self.profile_page.select_interest()
        self.profile_page.click_button()

        self.home_page.click_logout_link()
        self.home_page.click_login_link()
        self.login_page.click_forgot_password_link()
        self.forgot_password_page.enter_email("test.users@gmail.com")
        self.forgot_password_page.click_button()
