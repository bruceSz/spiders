from scrapy.spider import Spider
from scrapy.selector import Selector
    
class FirstSpider(Spider):
    name = "testresult"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://9.111.114.58:8080/job/OSP4.1_OS_Test_BD_PowerVC/9/testReport/"
    ]

    def parse(self,response):
        sel = Selector(response)
        sites = sel.xpath('//body/table[@id="main-table"]/tr/td[@id="main-panel"]/table/tr/td[1]/a[@class="model-link inside"]/@href').extract()
        for site in sites:
            print site
