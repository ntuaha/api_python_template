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

## 安裝 docker

ref: [Ubuntu Linux 安裝 Docker 步驟與使用教學](https://blog.gtwang.org/virtualization/ubuntu-linux-install-docker-tutorial/)

```shell
# 安裝 docker 
sudo apt-get install docker.io
# 確認服務
service docker status
# 加入帳號到 docker group
sudo groupadd docker
# sudo usermod -aG docker ntuaha
sudo usermod -aG docker $USER
# 確認 docker version
docker version
```

## install docker-compose

ref: [Install Docker Compose](https://docs.docker.com/compose/install/)

```shell
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```

## EFK

1. ref: [EFK](https://blog.yowko.com/docker-efk/)
2. [用 ElasticSearch + FluentD 打造 Log 神器與數據分析工具](https://blog.toright.com/posts/5133/%E7%94%A8-elasticsearch-fluentd-%E6%89%93%E9%80%A0-log-%E7%A5%9E%E5%99%A8%E8%88%87%E6%95%B8%E6%93%9A%E5%88%86%E6%9E%90%E5%B7%A5%E5%85%B7.html)
3. 啟動

    ```shell
    docker-compose -f docker-compose.yml up -d --remove-orphans
    ```

4. 連線到 kibana [http://localhost:5601](http://localhost:5601)
5. 送資料到 fluend

    ```shell
    curl -X GET http://localhost:8888/aha.test1?json={"a":1}
    ```

## metabase

- [metabase on docker hub](https://hub.docker.com/r/metabase/metabase)
- [run metabase via docker](https://www.metabase.com/docs/latest/operations-guide/running-metabase-on-docker.html)

```shell
docker-compose -f docker-compose-metabase.yml up -d --remove-orphans
```

### connect to postgreSQL

```shell
psql -d meatabase -h localhost -p 5431 -U aha
```

## 遠端安裝

透過 ansible-playbook

```shell
ansible-playbook -i inventory install.yml
```
