from base_test import BaseTest
from frontend.page_object.inventoryPage import InventoryPage
from frontend.page_object.loginPage import LoginPage
from testdata.texts import Texts


class TestLogin(BaseTest):

    def setup_method(self):
        self.import_testdata()
        self.set_up()

    def teardown_method(self):
        self.tear_down()

    def test_login_with_standard_user(self):
        login_page = LoginPage(self.page)
        login_page.verify_page_title(Texts.page_title)
        login_page.enter_login_username_and_password(
            self.testdata["STANDARD_USER"],
            self.testdata["PASSWORD"]
        )
        login_page.click_login_button()
        inventory_page = InventoryPage(self.page)
        inventory_page.verify_inventory_list_is_shown()

    def test_login_with_locked_out_user(self):
        login_page = LoginPage(self.page)
        login_page.enter_login_username_and_password(
            self.testdata["LOCKED_OUT_USER"],
            self.testdata["PASSWORD"]
        )
        login_page.click_login_button()
        login_page.verify_error_heading_is_shown(Texts.error_text)
