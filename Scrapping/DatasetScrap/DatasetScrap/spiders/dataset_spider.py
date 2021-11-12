from scrapy import Spider
from scrapy.selector import Selector
from Scrapping.DatasetScrap.DatasetScrap.items import DatasetscrapItem
#from DatasetScrap.items import DatasetscrapItem

class DatasetSpider(Spider):
    name = "dataset"
    allowed_domains = ["github.com"]
    start_urls = [
        "https://github.com/nytimes/covid-19-data/blob/master/live/us-counties.csv"
    ]

    def parse(self, response):
        # table = Selector(response).xpath("table[@class='js-csv-data csv-data js-file-line-container']")
        rows = Selector(response).xpath("//table[@class='js-csv-data csv-data js-file-line-container']//tbody//tr")
        for row in rows:
            item = DatasetscrapItem()
            item['date'] = row.xpath('td[2]//text()').extract_first()
            item['state'] = row.xpath('td[4]//text()').extract_first()
            item['cases'] = row.xpath('td[6]//text()').extract_first()
            item['deaths'] = row.xpath('td[7]//text()').extract_first()
            item['confirmed_cases'] = row.xpath('td[8]//text()').extract_first()
            item['confirmed_deaths'] = row.xpath('td[9]//text()').extract_first()
            yield item
