from bs4 import BeautifulSoup
from locators.links_locator import LinksLocator


class AllLinks:
    def __init__(self, page_content):
        self.soup = BeautifulSoup(page_content, 'html.parser')
        self.links_href = []

    @property
    def get_links(self):
        links_menu = self.soup.select(LinksLocator.menu)[1]
        links = links_menu.select(LinksLocator.links)
        for link in links:
            href = link.attrs['href']
            self.links_href.append(href)
        return self.links_href