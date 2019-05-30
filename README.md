You can find Scrapy spider example code which can help you:

1. A simple Scrapy spider shows you how to extract data from the web page.

2. How to handle pagination in Scrapy spider.

3. A simple script which can make your Scrapy shell more powerful.

4. How to define Scrapy item, and how to create a custom Item Pipeline to save the data of Item into Databases such as Mysql or PostgreSQL.

5. All the code can run without problem in Python2 and Python3


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

##### pep8
```cmd
$ pep8 --first --show-source ./
```

##### autopep8
```cmd
$ autopep8 --in-place --aggressive --aggressive scrapy_env.py
```

## Warning
Edit `CONNECTION_STRING` in `scrapy_spider/settings.py` before running spider.

##### Run the app
```bash
$ scrapy crawl jobs_spider
```