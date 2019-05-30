##### Create the virtualenv
```cmd
$ python -m venv scrapy-mysql
$ cd scrapy-mysql
$ Scripts\activate.bat
```

##### Install dependencies
```bash
$ pip install -r requirements.txt
$ pip list
```

## Pre-req & Warnings
- Run database.sql first to create database first.
- Edit `CONNECTION_STRING` in `scrapy_spider/settings.py` before running spider.

##### Run the app
```bash
$ scrapy crawl jobs_spider
```

##### pep8
```cmd
$ pep8 --first --show-source ./scrapy_spider
```

##### autopep8
```cmd
$ autopep8 --in-place --aggressive --aggressive scrapy_env.py
```