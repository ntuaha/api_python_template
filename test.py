import requests
import time
import json
import random

def main():
    while True:
        data ={
            "a":1,
            "t":time.time(),
            "r":random.random()
        }
        url = f'http://localhost:8888/aha.test1?json={json.dumps(data)}'
        r = requests.get(url)
        time.sleep(random.random()/2)
    print(r.status_code)
    print(url)


if __name__=="__main__":
    main()