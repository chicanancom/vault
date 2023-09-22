import scrapy
from scrapy.crawler import CrawlerProcess


class blocklistSpider(scrapy.Spider):
    name = "block-list"
    # allowed_domains = ["lists.blocklist.de"]
    start_urls = ["https://lists.blocklist.de/lists/all.txt"]
    custom_settings = {
        'FEEDS': {'blocklist.json': {'format': 'json', }}
    }
    def parse(self, response):
        ip = response.xpath("//text()").getall()
        ips = [i.split("\n") for i in ip]
        for i in ips[0]:
            yield {"ip": i}

process = CrawlerProcess()
process.crawl(blocklistSpider)
process.start()
