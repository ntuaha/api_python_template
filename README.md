# api_python_template

personal api server template on fastapi

## How to execute

```shell
uvicorn server:app --reload --port 5000
```

## How to test

```shell
sudo -H pip3 install -r requirement.txt 
PYTHONPATH=`pwd` pytest
```

## install docker-compose

ref: https://docs.docker.com/compose/install/

```shell
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```

## EFK

1. ref: https://blog.yowko.com/docker-efk/
2. https://blog.toright.com/posts/5133/%E7%94%A8-elasticsearch-fluentd-%E6%89%93%E9%80%A0-log-%E7%A5%9E%E5%99%A8%E8%88%87%E6%95%B8%E6%93%9A%E5%88%86%E6%9E%90%E5%B7%A5%E5%85%B7.html
2. 啟動

```shell
docker-compose -f docker-compose.yml up -d --remove-orphans
```

3. 連線到 kibana http://localhost:5601
4. 送資料到 fluend GET http://localhost:8888/aha.test1?json={"a":1}