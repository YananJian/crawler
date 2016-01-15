from common import db

class ShopstylePipeline(object):


    def open_spider(self, spider):
        self.mongodao = db.MongoDAO()

    def process_item(self, item, spider):
        self.mongodao.update("shopstyle", {"prodId" : item.get('prodId'), "gender":item.get("gender")}, dict(item), upsert = True)
        return item

    def close_spider(self, spider):
        self.mongodao.close()
