import pytest
from playwright.sync_api import sync_playwright
from helpers.import_file import ImportFile


class BaseTest:

    def set_up(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=True)
        self.page = self.browser.new_page()
        self.page.goto(self.testdata["URL"])

    def tear_down(self):
        self.browser.close()
        self.playwright.stop()

    def import_testdata(self):
        file = "testdata.yml"
        import_file = ImportFile()
        self.testdata = import_file.import_testdata("testdata/" + file)


if __name__ == "__main__":
    pytest.main()
