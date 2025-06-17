from ..locator import LoginPageLocator
from playwright.sync_api import expect


class LoginPage(LoginPageLocator):

    def __init__(self, page):
        self.page = page

    def enter_login_username_and_password(self, username, password):
        self.page.locator(LoginPageLocator.username_input_field).fill(username)
        self.page.locator(LoginPageLocator.password_input_field).fill(password)

    def click_login_button(self):
        self.page.locator(LoginPageLocator.login_button).click()

    def verify_page_title(self, text):
        expect(self.page).to_have_title(text)

    def verify_error_heading_is_shown(self, text):
        element = self.page.locator(LoginPageLocator.error_container)
        expect(element).to_be_visible()
        expect(element).to_have_text(text)
