from analyticalStatistics import print_statistics
from spiders.dataset_spider import DatasetSpider
from pymongo import MongoClient
from scrapy.selector import Selector
import requests as requests
from getpass import getpass
import os
from scrapy.crawler import CrawlerProcess
# def scrap():



def set_local_db(username, password):
    local = MongoClient("mongodb://localhost:27017/")
    db_name = 'MINADZB'
    coll_name = 'covid'
    database_list = local.list_database_names()

    if db_name not in database_list:
        db_local = local[db_name]
        records = db_local[coll_name]
        # process = CrawlerProcess()
        # process.crawl(DatasetSpider)
        # process.start()
        #1
        response = requests.get('https://github.com/nytimes/covid-19-data/blob/master/live/us-counties.csv')
        rows = Selector(response).xpath("//table[@class='js-csv-data csv-data js-file-line-container']//tbody//tr")
        for row in rows:
            new_item = {
                'date': row.xpath('td[2]//text()').extract_first(),
                'county': row.xpath('td[3]//text()').extract_first(),
                'state': row.xpath('td[4]//text()').extract_first(),
                'cases': row.xpath('td[6]//text()').extract_first(),
                'deaths': row.xpath('td[7]//text()').extract_first(),
                'confirmed_cases': row.xpath('td[8]//text()').extract_first(),
                'confirmed_deaths': row.xpath('td[9]//text()').extract_first()
            }
            records.insert_one(new_item)
    else:
        db_local = local[db_name]
        records = db_local[coll_name]

    set_cloud(records, coll_name, db_name, username, password)

    # db_local = local['MINADZB']
    # db_local.drop_collection(coll_name)



def set_cloud(records, coll_name, db_name, username, password):
    link = "mongodb+srv://"+username+":"+password+"@covid.7imo3.mongodb.net/MINADZB_cloud?retryWrites=true&w=majority"
    client = MongoClient(link)
    # client = MongoClient(
    #     "mongodb+srv://admin:Password123@covid.7imo3.mongodb.net/MINADZB_cloud?retryWrites=true&w=majority")
    # client = MongoClient(
    #     "mongodb://admin:Password123@covid-shard-00-00.7imo3.mongodb.net:27017,covid-shard-00-01.7imo3.mongodb.net:27017,covid-shard-00-02.7imo3.mongodb.net:27017/MINADZB_cloud?ssl=true&replicaSet=atlas-gghftr-shard-0&authSource=admin&retryWrites=true&w=majority")

    db = client[db_name]
    db.drop_collection(coll_name)
    records_cloud = db[coll_name]

    for record in records.find({}):
        records_cloud.insert_one(record)
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
    2 - Print statistics
    x - exit
    """
    states = []
    choice = input(info)
    if(choice == '1'):
        username = input('Username: ')
        password = getpass()
        set_local_db(username, password)
    elif (choice == '2'):
        n = int(input("Number of states : "))
        for i in range(0, n):
            x = input("Enter "+str(i+1)+"st state name: ")
            states.append(x)
            n = n+1
        print_statistics(states)
    elif(choice == 'x'):
        exit(0)
