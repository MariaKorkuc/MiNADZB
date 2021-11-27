import requests as requests
from pymongo import MongoClient
from Scrapping.DatasetScrap.DatasetScrap.spiders.dataset_spider import DatasetSpider
from Scrapping.DatasetScrap.DatasetScrap.items import DatasetscrapItem

from scrapy.selector import Selector


def parse(response):
    print("pres runs")
    n = 0
    client = MongoClient(
        "mongodb+srv://admin:Password123@covid.7imo3.mongodb.net/MINADZB_cloud?retryWrites=true&w=majority")
    db = client.get_default_database('MINADZB_cloud')
    records = db.covid_records

    # client = pymongo.MongoClient(
    #     "mongodb://admin:Password123@covid-shard-00-00.7imo3.mongodb.net:27017,covid-shard-00-01.7imo3.mongodb.net:27017,covid-shard-00-02.7imo3.mongodb.net:27017/MINADZB_cloud?ssl=true&replicaSet=atlas-gghftr-shard-0&authSource=admin&retryWrites=true&w=majority")
    # db = client.test

    # table = Selector(response).xpath("table[@class='js-csv-data csv-data js-file-line-container']")
    rows = Selector(response).xpath("//table[@class='js-csv-data csv-data js-file-line-container']//tbody//tr")
    for row in rows:
        print('int(n) is:', int(n))
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
        # records.insert_one(new_item)
        n = n + 1


class cloud:

    #1
    req = requests.get('https://github.com/nytimes/covid-19-data/blob/e48f1870353cdeb4d9d6ec33bbd92c7842629e78/live/us-counties.csv')
    #req = requests.get('https://github.com/nytimes/covid-19-data/blob/master/live/us-counties.csv')
    parse(req)

    #2
    req = requests.get('https://github.com/nytimes/covid-19-data/blob/06271a728847a626f0005e5e1302e4482b6efbdf/live/us-counties.csv')
    parse(req)

    #2
    req = requests.get('https://github.com/nytimes/covid-19-data/blob/815ff7c3ce6f3a8204ebd1637223047046e68bc4/live/us-counties.csv')
    parse(req)

    #2
    req = requests.get('https://github.com/nytimes/covid-19-data/blob/06f58da4ebbd2740466ce19596ed9dbe1be77db9/live/us-counties.csv')
    parse(req)

    #2
    req = requests.get('https://github.com/nytimes/covid-19-data/blob/7ee9095deb26915c87365846d1988e53287db7c2/live/us-counties.csv')
    parse(req)

    #2
    req = requests.get('https://github.com/nytimes/covid-19-data/blob/2874bb674a0cb2a1996ae86fc0e61e00e4520be9/live/us-counties.csv')
    parse(req)

    #2
    req = requests.get('https://github.com/nytimes/covid-19-data/blob/e6738cbbd9b94626d447669070f815e9f041957a/live/us-counties.csv')
    parse(req)

