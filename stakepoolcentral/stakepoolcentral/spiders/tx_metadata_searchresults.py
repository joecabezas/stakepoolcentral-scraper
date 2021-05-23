import json
import lxml.html
import scrapy

from adalotl import Adalotl

class TxMetadataSearchresultsSpider(scrapy.Spider):
    name = 'tx_metadata_searchresults'
    allowed_domains = ['stakepoolcentral.com']
    start_urls = ['https://bi.stakepoolcentral.com/tx_metadata_searchresults?query=Adalotl%20293']

    def parse(self, response):
        html = response.xpath('//pre').get()
        tree = lxml.html.fromstring(html)
        json_string = tree.text_content()
        metadata = json.loads(json_string)
        adalotl = Adalotl(metadata)
        print(adalotl)
