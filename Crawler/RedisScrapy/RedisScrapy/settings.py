# -*- coding: utf-8 -*-

# Scrapy settings for novelspider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'RedisScrapy'

SPIDER_MODULES = ['RedisScrapy.spiders']
NEWSPIDER_MODULE = 'RedisScrapy.spiders'

ITEM_PIPELINES = {'RedisScrapy.pipelines.NovelspiderPipeline':300}

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5'
COOKIES_ENABLED = True

SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'
REDIS_URL = None
REDIS_HOST = '192.168.136.129'
REDIS_PORT = 6379

MONGODB_HOST = '192.168.136.129'
MONGODB_PORT = 27017
MONGODB_DBNAME = '27017'
MONGODB_DOCNAME = 'you'