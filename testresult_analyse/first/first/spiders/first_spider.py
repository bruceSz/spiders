from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.selector import Selector

from first.items import TestItem
    
class FirstSpider(Spider):
    name = "testresult"
    allowed_domains = []
    start_urls = [
        "http://9.111.114.58:8080/job/OSP4.1_OS_Test_BD_PowerVC/9/testReport/"
    ]

    def parse(self,response):
        self.filename = "test_report_error"
        self.f_handler = open(self.filename,'wb')


        sel = Selector(response)
        sites = sel.xpath('//body/table[@id="main-table"]/tr/td[@id="main-panel"]/table/tr/td[1]/a[@class="model-link inside"]/@href').extract()
        reqs = []
        
        for site in sites:
            item = TestItem()

            item['link'] = self.start_urls[0]+site
            #print item['link']
            #print item['link']
            reqs.append(Request(item['link'],callback=self.parse_error))

        return reqs

    def parse_error(self,response):
        sel = Selector(response)
        #print response.body
        errors = sel.xpath('//body/table/tr/td/pre[1]').extract()
        #print type(errors)
        #print errors

        self.f_handler.write("\n\n")
        self.f_handler.write(str(errors))
        self.f_handler.write("="*20)
        self.f_handler.write("="*20)

