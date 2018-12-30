# -*- coding: utf-8 -*-

# Scrapy settings for doubanallmovie project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'doubanallmovie'

SPIDER_MODULES = ['doubanallmovie.spiders']
NEWSPIDER_MODULE = 'doubanallmovie.spiders'
MONGO_URI='localhost'
MONGO_DATABASE='douban3'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'doubanallmovie (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,und;q=0.7',
    'Referer': 'https://movie.douban.com/',
    'Host': 'movie.douban.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
    'Cookie':'__yadk_uid=q4E9fEOZxeIqqqNp5CbR6wlj1eOLZ8i8; ll="118295"; bid=8c1x2gUeAWg; _vwo_uuid_v2=D408E86B80FF97F3EB80BEA544703E694|df2c31e4f140ab11f65ef45ed02ed26e; gr_user_id=183a09ad-2131-472a-972d-0fbbf917845b; _ga=GA1.2.738094072.1534322196; __utmv=30149280.4874; viewed="26838150_1230154_1257113_25910544"; __utma=30149280.738094072.1534322196.1542116582.1542370031.32; __utmc=30149280; __utmz=30149280.1542370031.32.14.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; __utmb=30149280.1.10.1542370031; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1542370033%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=223695111.251246016.1534238193.1536111112.1542370033.29; __utmb=223695111.0.10.1542370033; __utmc=223695111; __utmz=223695111.1542370033.29.20.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ps=y; dbcl2="48746302:3+yAHCiKacA"; ck=wM9r; push_noty_num=0; push_doumail_num=0; _pk_id.100001.4cf6=9a2a17a00778cbb1.1534238193.35.1542370583.1537521595.',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'doubanallmovie.middlewares.DoubanallmovieSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    #'doubanallmovie.middlewares.RandomUserAgent':542,
    #'doubanallmovie.middlewares.DoubanDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'doubanallmovie.pipelines.DoubanallmoviePipeline': 300,
    'doubanallmovie.pipelines.MongoPipeline': 301,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
