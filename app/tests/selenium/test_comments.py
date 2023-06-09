from selenium import webdriver
from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.set_window_size(1776, 945)

    def click_sign_up_link(self):
        self.driver.find_element(By.LINK_TEXT, "Sign Up").click()


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


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        email_field = self.driver.find_element(By.ID, "email")
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.driver.find_element(By.ID, "password")
        password_field.click()
        password_field.send_keys(password)

    def click_button(self):
        self.driver.find_element(By.CSS_SELECTOR, ".button").click()


class PostPage:
    def __init__(self, driver):
        self.driver = driver

    def click_create_new_post(self):
        self.driver.find_element(By.LINK_TEXT, "Create New Post").click()

    def enter_title(self, title):
        title_field = self.driver.find_element(By.ID, "title")
        title_field.click()
        title_field.send_keys(title)

    def enter_content(self, content):
        content_field = self.driver.find_element(By.ID, "content")
        content_field.click()
        content_field.send_keys(content)

    def click_button(self):
        self.driver.find_element(By.CSS_SELECTOR, ".button").click()


class CommentPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_comment(self, comment):
        comment_field = self.driver.find_element(By.CSS_SELECTOR, "form #content")
        comment_field.click()
        comment_field.send_keys(comment)

    def click_button(self):
        self.driver.find_element(By.CSS_SELECTOR, ".button").click()


class TestComments:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.home_page = HomePage(self.driver)
        self.sign_up_page = SignUpPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.post_page = PostPage(self.driver)
        self.comment_page = CommentPage(self.driver)

    def teardown_method(self, method):
        self.driver.quit()

    def test_comments(self):
        self.home_page.open()
        self.home_page.click_sign_up_link()

        self.sign_up_page.enter_email("test.comments@gmail.com")
        self.sign_up_page.enter_name("test comments")
        self.sign_up_page.enter_password("12345678")
        self.sign_up_page.enter_confirm_password("12345678")
        self.sign_up_page.click_button()

        self.login_page.enter_email("test.comments@gmail.com")
        self.login_page.enter_password("12345678")
        self.login_page.click_button()

        self.post_page.click_create_new_post()
        self.post_page.enter_title("test comment title")
        self.post_page.enter_content("test comment content")
        self.post_page.click_button()

        self.driver.find_element(By.LINK_TEXT, "test comment title").click()

        self.comment_page.enter_comment("test comment comment")
        self.comment_page.click_button()
