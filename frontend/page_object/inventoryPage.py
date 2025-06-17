from ..locator import InventoryPageLocator
from playwright.sync_api import expect


class InventoryPage(InventoryPageLocator):

    def __init__(self, page):
        self.page = page

    def verify_inventory_list_is_shown(self):
        expect(
            self.page.locator(
                InventoryPageLocator.inventory_list)).to_be_visible()

    def click_an_inventory_item(self, inventory_index=None):
        self.page.locator(InventoryPageLocator.inventory_item_name).nth(
            inventory_index).click()
