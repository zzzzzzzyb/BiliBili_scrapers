import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class LinksSpider(CrawlSpider):
    name = "links"
    allowed_domains = []
    start_urls = ["https://www.bilibili.com/read/cv30820561"]

    rules = (Rule(LinkExtractor(allow=r"space.bilibili.com/.+"), callback="parse_item", follow=True),)

    def parse_item(self, response):
        with open("links_3.txt", "a") as f:
            f.write(response.url+'\n')
        #item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        #item["name"] = response.xpath('//div[@id="name"]').get()
        #item["description"] = response.xpath('//div[@id="description"]').get()
        pass
