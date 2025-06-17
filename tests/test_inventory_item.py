from base_test import BaseTest
from frontend.page_object.inventoryItemPage import InventoryItemPage
from frontend.page_object.loginPage import LoginPage


class TestInventoryItem(BaseTest):

    def setup_method(self):
        self.import_testdata()
        self.set_up()

    def teardown_method(self):
        self.tear_down()

    def test_add_and_remove_item_from_the_cart(self):
        login_page = LoginPage(self.page)
        login_page.enter_login_username_and_password(
            self.testdata["STANDARD_USER"],
            self.testdata["PASSWORD"]
        )
        login_page.click_login_button()
        self.page.goto(self.testdata["URL"] + "inventory-item.html?id=0")
        inventory_item_page = InventoryItemPage(self.page)
        inventory_item_page.click_add_to_cart_button()
        inventory_item_page.verify_item_in_shopping_cart(number_of_item="1")
        inventory_item_page.click_remove_button()
