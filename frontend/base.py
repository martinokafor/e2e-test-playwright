class Base:

    def __init__(self, page):
        self.page = page

    def verify_url_change(self, url):
        self.page.wait_for_url(url)
