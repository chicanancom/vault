import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy_splash import SplashRequest


def remove_items(lst, item):
    return


class VxspiderSpider(scrapy.Spider):
    name = "VXspider"
    allowed_domains = ["vxvault.net"]
    start_urls = ["https://vxvault.net"]
    custom_settings = {
        'FEEDS': {'vxvault.json': {'format': 'json', }}
    }
    def start_requests(self):
        for i in range(0, 44707, 40):
            yield SplashRequest(f'https://vxvault.net/ViriList.php?s={i}&m=40', endpoint="render.html",
                                callback=self.parse)

    def parse(self, response):
        a = response.xpath("//tr//td//a/text()").getall()
        item = ["VT","PED"]
        b = [x for x in a if x not in item]
        date = b[::3]
        md5 = b[1::3]
        ip = b[2::3]
        data = zip(date,md5,ip)
        for i in tuple(data):
            yield {'date':i[0],
                   'md5':i[1],
                   'ip':i[2]}


process = CrawlerProcess()
process.crawl(VxspiderSpider)
process.start()
