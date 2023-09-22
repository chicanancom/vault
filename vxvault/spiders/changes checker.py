import time
import hashlib
from urllib.request import urlopen, Request
import requests
# from blocklist import blocklistSpider
# from VXspider import VxspiderSpider
# from scrapy.crawler import CrawlerProcess


url = Request('https://bazaar.abuse.ch/',
              headers={'User-Agent': 'Mozilla/5.0'})
url1 = Request('https://lists.blocklist.de/lists/all.txt',
              headers={'User-Agent': 'Mozilla/5.0'})

currentHash = hashlib.sha224(urlopen(url).read()).hexdigest()
currentHash1 = hashlib.sha224(urlopen(url1).read()).hexdigest()
print("running")
time.sleep(10)
while True:
    try:
        currentHash = hashlib.sha224(urlopen(url).read()).hexdigest()
        currentHash1 = hashlib.sha224(urlopen(url1).read()).hexdigest()

        time.sleep(30)

        newHash = hashlib.sha224(urlopen(url).read()).hexdigest()
        newHash1 = hashlib.sha224(urlopen(url1).read()).hexdigest()

        if newHash == currentHash :
            continue

        else:
            # notify
            print("something changed")

            text = 'something changed'
            base_url = f"https://api.telegram.org/bot6422096295:AAGvVKjNGh7t9UsDB73hG3kYg_YnSLzwj4k/sendMessage?chat_id=-4002102545&text={text}"
            requests.get(base_url)

            newHash = hashlib.sha224(urlopen(url).read()).hexdigest()
            newHash1 = hashlib.sha224(urlopen(url1).read()).hexdigest()

            time.sleep(30)
            continue

    except Exception as e:
        print("error")