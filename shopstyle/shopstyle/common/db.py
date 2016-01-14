import pymongo
from pymongo import MongoClient
import sys
import os
working_dir = os.path.realpath(os.path.dirname(__file__) + '/../')
sys.path.append(working_dir)

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class MongoDAO(object):
    __metaclass__ = Singleton
    client = MongoClient()
    db = client['vxplore']
    
    def insert(self, table, rec):
        self.db[table].insert_one(rec)

    def find(self, table, term):
        return self.db[table].find_one(term, {"_id":0})

    def update(self, table, key, value, upsert=True):
        self.db[table].update(key, value, upsert)

    def close(self):
        self.client.close()


if __name__ == "__main__":
    dao = MongoDAO()
    table = "video_info"
    rec = {"videoid":"123", "videoname":"test"}
    dao.insert(table, rec)
    term = {"videoid":"123"}
    res = dao.find(table, term)
    print res.get("videoname")
    dao.update(table, {"videoid":"123"}, {"videoname":"testtest"})
    print dao.find(table, {"videoid":"123"})
