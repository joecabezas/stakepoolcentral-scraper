import json
import lxml.html
import scrapy

class TxMetadataSearchresultsSpider(scrapy.Spider):
    name = 'tx_metadata_searchresults'
    allowed_domains = ['stakepoolcentral.com']
    start_urls = ['https://bi.stakepoolcentral.com/tx_metadata_searchresults?query=Adalotl%20293']

    def start_requests(self):
        yield scrapy.Request(f"https://bi.stakepoolcentral.com/tx_metadata_searchresults?query=Adalotl%20{self.number}")

    def parse(self, response):
        html = response.xpath('//pre').get()

        if not html:
            raise RuntimeError(f"metadata for {self.number} not found")

        tree = lxml.html.fromstring(html)
        json_string = tree.text_content()
        json_object = json.loads(json_string)
        return json_object

