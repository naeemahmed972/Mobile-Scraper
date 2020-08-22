from locators.mobile_locators import MobileLocators

class MobileParser:

    def __init__(self, parent):
        self.parent = parent

    @property
    def name(self):
        locator = MobileLocators.mobile_name
        item_link = self.parent.select_one(locator)
        item_name = item_link.attrs['title']
        item_name = item_name.replace(' price', '')
        return item_name

    @property
    def link(self):
        locator = MobileLocators.mobile_link
        item_link = self.parent.select_one(locator).attrs['href']
        return item_link

    @property
    def price(self):
        locator = MobileLocators.mobile_price
        item_price = self.parent.select_one(locator).string
        if item_price is not None:
            if 'N/A' not in item_price:
                item_price = item_price.strip()
                item_price = item_price[4:]
                item_price = int(item_price.replace(',', ''))
                return item_price
            else:
                return None

    def __repr__(self):
        return f'<Mobile: {self.name}, Price: {self.price}PKR'