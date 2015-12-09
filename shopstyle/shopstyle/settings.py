# Scrapy settings for shopstyle project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'shopstyle'

SPIDER_MODULES = ['shopstyle.spiders']
NEWSPIDER_MODULE = 'shopstyle.spiders'
DOWNLOADER_MIDDLEWARES = {'scrapyjs.SplashMiddleware' : 725,}
DUPEFILTER_CLASS = 'scrapyjs.SplashAwareDupeFilter'
SPLASH_URL = 'http://192.168.59.103:8050/'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'shopstyle (+http://www.yourdomain.com)'
