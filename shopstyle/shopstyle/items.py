# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class ShopstyleItem(Item):
    # define the fields for your item here like:
    # name = Field()
    prodId = Field()
    name = Field()
    brandedName = Field()
    currency = Field()
    price = Field()
    inStock = Field()
    brand = Field()
    desc = Field()
    clickUrl = Field()
    image = Field()
    alternateImages = Field()
    colors = Field()
    categories = Field()
