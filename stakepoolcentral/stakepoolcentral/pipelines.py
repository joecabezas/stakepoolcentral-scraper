# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json

from scrapy.exceptions import DropItem

class StakepoolcentralPipeline:

    def process_item(self, item, spider):
        if not item:
            raise DropItem()

        with open(f"data/adalotls/{spider.number}.json", 'w') as f:
            f.write(json.dumps(item))

        return item
