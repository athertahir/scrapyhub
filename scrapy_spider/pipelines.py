# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from sqlalchemy.orm import sessionmaker
from scrapy_spider.models import JobsDB, db_connect, create_table


class ScrapySpiderPipeline(object):
    def __init__(self):
        """
        Initializes database connection.
        """
        try:
            engine = db_connect()
            create_table(engine)
            self.Session = sessionmaker(bind=engine)
        except Exception as error:
            print('[Error:] Failed to connect to database: ' + repr(error))

    def process_item(self, item, spider):
        """
        This method is called for every item pipeline component.
        """
        session = self.Session()
        jobsdb = JobsDB()
        jobsdb.age = item["age"]
        jobsdb.company_name = item["company_name"]
        jobsdb.position = item["position"]
        jobsdb.location = item["location"]
        jobsdb.details = item["details"]

        try:
            session.add(jobsdb)
            session.commit()
        except Exception as error:
            session.rollback()
            print('[Error:] Failed to save data in database ' + repr(error))
            #  raise
        finally:
            session.close()

        return item
