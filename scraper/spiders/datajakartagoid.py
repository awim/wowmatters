import scrapy
from scraper.items.datajakartagoid import OpendatajakartaItem, DatasetItem

class DatajakartagoidSpider(scrapy.Spider):
    name = 'datajakartagoid'
    allowed_domains = ['data.jakarta.go.id']
    start_urls = ['https://data.jakarta.go.id/dataset?sort=1']
    data_file = "data/datajakartagoid/datajakarta.json"

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        dataset_path='//div[contains(@class,"rincian_info")]//a'
        datasets=response.xpath(dataset_path)
        # datajakarta = open(self.data_file, 'a')
        for dataset in datasets:
            link = dataset.xpath('./@href').get()
            title = dataset.xpath('.//h4/text()').get()

            ref = OpendatajakartaItem()
            ref['link'] = link
            ref['title'] = title

            yield ref

            # datajakarta.write(str(dict(ref)) + '\n')
        # datajakarta.close()

        # read next link and yield parse
        next_page = response.xpath('//a[contains(@class,"page-link")][@rel="next"]/@href').get()
        if next_page is not None:
            yield scrapy.Request(url=next_page, callback=self.parse)


    def parse_opendataurl(self, context):
        dataset_path='//div[contains(@class,"rincian_info")]//a'
        datasets=response.xpath(dataset_path)
        for dataset in datasets:
            dataurl = OpendatajakartaItem()
            
    def parse_datasets(self, response):
        dataset_path='//div[contains(@class,"rincian_info")]//a'
        dataset_list=response.xpath(dataset_path)
        for dataset in dataset_list:
            print(dataset.xpath('/@href'))
