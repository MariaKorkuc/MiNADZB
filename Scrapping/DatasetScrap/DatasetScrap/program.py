from spiders.dataset_spider import DatasetSpider
from pymongo import MongoClient
import os
from scrapy.crawler import CrawlerProcess

def set_local_db():
    process = CrawlerProcess()
    process.crawl(DatasetSpider)
    process.start()
    set_cloud()

def set_cloud():
    coll_name = 'covid_records'
    local = MongoClient("mongodb://localhost:27017/")
    client = MongoClient("mongodb+srv://admin2:admin@covid.7imo3.mongodb.net/MINADZB_cloud2?retryWrites=true&w=majority")
    db_local = local['MINADZB']
    # database_list = client.list_database_names()
    db = client['MINADZB_cloud']
    db.drop_collection(coll_name)
    records = db[coll_name]
    records_local = db_local.get_collection('covid')

    for record in records_local:
        records.insert_one(record)
    # db = client.get_default_database('MINADZB_cloud')
    # records = db.covid_records
    # client.admin.command('copydb',
    #                      fromdb='MINADZB',
    #                      todb='MINADZB_cloud',
    #                      fromhost="localhost:27018")


if __name__ == '__main__':
    print('COVID DATABASE\n')
    info = """
    1 - Set database from scratch
    2 - Insert data
    3 - Print statistics
    x - exit
    """
    choice = input(info)
    if(choice == '1'):
        set_local_db()
    elif(choice == 'x'):
        exit(0)
