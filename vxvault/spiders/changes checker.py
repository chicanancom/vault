import time
import hashlib
from urllib.request import urlopen, Request
import requests


url = Request('https://vxvault.net',
              headers={'User-Agent': 'Mozilla/5.0'})

response = urlopen(url).read()

currentHash = hashlib.sha224(response).hexdigest()
print("running")
time.sleep(10)
while True:
    try:
        response = urlopen(url).read()

        currentHash = hashlib.sha224(response).hexdigest()

        time.sleep(30)

        response = urlopen(url).read()

        newHash = hashlib.sha224(response).hexdigest()

        if newHash == currentHash:
            continue

        else:
            # notify
            print("something changed")

            text = 'something changed'
            base_url = f"https://api.telegram.org/bot6422096295:AAGvVKjNGh7t9UsDB73hG3kYg_YnSLzwj4k/sendMessage?chat_id=-4002102545&text={text}"
            requests.get(base_url)

            response = urlopen(url).read()

            currentHash = hashlib.sha224(response).hexdigest()

            time.sleep(30)
            continue

    except Exception as e:
        print("error")