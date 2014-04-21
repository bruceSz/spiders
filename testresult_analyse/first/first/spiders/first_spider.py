from scrapy.spider import Spider
from scrapy.selector import Selector
    
class FirstSpider(Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books"
    ]

    def parse(self,response):
        sel = Selector(response)
        sites = sel.xpath('//ul/li')
        for site in sites:
            title = site.xpath('a/text()').extract()
            link = site.xpath('a/@href').extract()
            desc = site.xpath('text()').extract()
            print title,link,desc
