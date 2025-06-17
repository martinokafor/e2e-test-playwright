from ..base import Base
from ..locator import InventoryItemPageLocator
from playwright.sync_api import expect


class InventoryItemPage(Base, InventoryItemPageLocator):

    def __init__(self, page):
        self.page = page

    def verify_inventory_item_is_opened(self):
        expect(
            self.page.locator(
                InventoryItemPageLocator.inventory_details)).to_be_visible()
        self.verify_url_change("**/inventory-item.html?id=*")

    def click_add_to_cart_button(self):
        self.page.wait_for_selector(
            InventoryItemPageLocator.add_to_cart_button).click()

    def click_remove_button(self):
        self.page.locator(InventoryItemPageLocator.remove_button).click()

    def verify_item_in_shopping_cart(self, number_of_item=None):
        assert self.page.locator(
            InventoryItemPageLocator.shopping_cart_badge).inner_text() == \
            number_of_item
