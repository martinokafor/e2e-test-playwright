from base_test import BaseTest
from frontend.page_object.inventoryPage import InventoryPage
from frontend.page_object.inventoryItemPage import InventoryItemPage
from frontend.page_object.loginPage import LoginPage


class TestInventory(BaseTest):

    def setup_method(self):
        self.import_testdata()
        self.set_up()

    def teardown_method(self):
        self.tear_down()

    def test_open_an_inventory_item(self):
        login_page = LoginPage(self.page)
        login_page.enter_login_username_and_password(
            self.testdata["STANDARD_USER"],
            self.testdata["PASSWORD"]
        )
        login_page.click_login_button()
        inventory_page = InventoryPage(self.page)
        inventory_page.verify_inventory_list_is_shown()
        inventory_page.click_an_inventory_item(inventory_index=1)
        inventory_item_page = InventoryItemPage(self.page)
        inventory_item_page.verify_inventory_item_is_opened()

    def test_add_and_remove_item_from_the_cart(self):
        login_page = LoginPage(self.page)
        login_page.enter_login_username_and_password(
            self.testdata["STANDARD_USER"],
            self.testdata["PASSWORD"]
        )
        login_page.click_login_button()
        self.page.goto(self.testdata["URL"] + "inventory-item.html?id=0")

