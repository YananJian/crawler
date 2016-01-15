# -*- coding: utf-8 -*-
import scrapy
from shopstyle.items import ShopstyleItem
from shopstyle import spiderconf as Conf
from shopstyle.common import genstarturl
import json


class ShopstylebotSpider(scrapy.Spider):
    name = "shopstylebot"
    allowed_domains = ["shopstyle.com"]
    start_urls = genstarturl.gen_urls(1, 589538)

    def parse(self, response):
        json_resp = response.body.decode(response.encoding)
        resp = json.loads(json_resp)
        items = []
        total = resp.get("metadata").get("total")
        products = resp.get("products")
        genderId = resp.get("metadata").get("category").get("id")
        gender = 'f'
        if genderId.startswith("mens"):
            gender = 'm'
        print "total:{0}".format(total)
        for prod in products:
            item = ShopstyleItem()
            item['prodId'] = prod.get('id')
            item['name'] = prod.get('name')
            item['brandedName'] = prod.get('brandedName')
            item['currency'] = prod.get('currency')
            item['price'] = prod.get('price')
            item['inStock'] = prod.get('inStock')
            if prod.get('brand') is None:
                item['brand'] = None
            else:
                item['brand'] = prod.get('brand').get('name')
            item['desc'] = prod.get('description')
            item['clickUrl'] = prod.get('clickUrl')
            item['image'] = prod.get('image').get('sizes').get('Best').get('url')
            _altImgs = []
            altImglist= prod.get('alternateImages')
            if altImglist != None:
                for img in altImglist:
                    _altImgs.append(img.get('sizes').get('Best').get('url'))
            item['alternateImages'] = _altImgs
            _colors = []
            colorlist = prod.get('colors')
            for color in colorlist:
                _colors.append(color.get('name'))
            item['colors'] =  _colors
            _cates = []
            catelist = prod.get('categories')
            for cate in catelist:
                _cates.append(cate.get('name'))
            item['categories'] = _cates
            item['gender'] = gender
            items.append(item)

        return items
