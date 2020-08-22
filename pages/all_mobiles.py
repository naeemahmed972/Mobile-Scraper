from bs4 import BeautifulSoup
from locators.links_locator import LinksLocator
from parsers.mobile_parser import MobileParser


class AllMobiles:
    def __init__(self, page_content):
        self.soup = BeautifulSoup(page_content, 'html.parser')

    @property
    def mobiles(self):
        return [MobileParser(page_mobiles) for page_mobiles in self.soup.select(LinksLocator.mobiles)]