
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field


class OpendatajakartaItem(Item):
    link = Field()
    title = Field()

class DatasetItem(OpendatajakartaItem):
    # _id=Field()
    description=Field()
    category=Field()
    metadata=Field()
    tags=Field()
    datasource_public=Field()
    datasource_csv=Field()
