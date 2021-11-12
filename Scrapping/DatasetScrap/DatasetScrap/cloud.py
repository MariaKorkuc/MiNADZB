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

    # table = Selector(response).xpath("table[@class='js-csv-data csv-data js-file-line-container']")
    rows = Selector(response).xpath("//table[@class='js-csv-data csv-data js-file-line-container']//tbody//tr")
    for row in rows:
        print('int(n) is:', int(n))
        new_item = {
            'date': row.xpath('td[2]//text()').extract_first(),
            'state': row.xpath('td[4]//text()').extract_first(),
            'cases': row.xpath('td[6]//text()').extract_first(),
            'deaths': row.xpath('td[7]//text()').extract_first(),
            'confirmed_cases': row.xpath('td[8]//text()').extract_first(),
            'confirmed_deaths': row.xpath('td[9]//text()').extract_first()
        }
        records.insert_one(new_item)
        n = n + 1


class cloud:
    client = MongoClient(
        "mongodb+srv://admin:Password123@covid.7imo3.mongodb.net/MINADZB_cloud?retryWrites=true&w=majority")
    db = client.get_default_database('MINADZB_cloud')
    records = db.covid_records

    def input_item(records):
        new_item = {
            'date': 'na',
            'roll_no': 321,
            'name2': 'me'
        }
        records.insert_one(new_item)
        return new_item

    req = requests.get('https://github.com/nytimes/covid-19-data/blob/master/live/us-counties.csv')
    parse(req)

