import json
import lxml.html
import scrapy

class TxMetadataSearchresultsSpider(scrapy.Spider):
    name = 'tx_metadata_searchresults'
    allowed_domains = ['stakepoolcentral.com']
    start_urls = ['https://bi.stakepoolcentral.com/tx_metadata_searchresults?query=Adalotl%20293']

    def start_requests(self):
        yield scrapy.Request(f"https://bi.stakepoolcentral.com/tx_metadata_searchresults?query=Adalotl%20{self.adalotl_number}")

    def parse(self, response):
        html = response.xpath('//pre').get()

        if not html:
            raise RuntimeError(f"metadata for {self.adalotl_number} not found")

        tree = lxml.html.fromstring(html)
        json_string = tree.text_content()
        return json.loads(json_string)

