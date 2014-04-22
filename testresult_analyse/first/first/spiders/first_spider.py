from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.selector import Selector

from first.items import TestItem

from first.db import Manager
    
class FirstSpider(Spider):
    name = "testresult"
    allowed_domains = []
    start_urls = [
        "http://9.111.114.58:8080/job/OSP4.1_OS_Test_BD_PowerVC/9/testReport/"
    ]

    def parse(self,response):
        self.filename = "test_report_error"
        self.f_handler = open(self.filename,'wb')
        self.count = 0
        self.manager = Manager()


        sel = Selector(response)
        sites = sel.xpath('//body/table[@id="main-table"]/tr/td[@id="main-panel"]/table/tr/td[1]/a[@class="model-link inside"]/@href').extract()
        reqs = []
        print "All %d failure" %len(sites)
        
        for site in sites:
            item = TestItem()

            item['link'] = self.start_urls[0]+site
            #print item['link']
            #print item['link']
            reqs.append(Request(item['link'],meta={'link':item['link']},callback=self.parse_Details))

        return reqs

    def parse_Details(self,response):
        sel = Selector(response)
        #print response.body
        errors = sel.xpath('//body/table/tr/td/pre[1]').extract()
        #print type(errors)
        #print errors

        # there should be only one error 
        error = errors[0]
        traceback = [message for message in error.split("\n\n") if message.find('Traceback') != -1]

        self.count += 1
        #print self.count
        #print type(traceback)
        print '==========',response.meta['link']
        #print traceback[len(traceback)-1]
        self.manager.set_data(response.meta['link'],"".join(traceback))
        #for error in errors:
        #    if error.find("Details")== -1:
        #        self.count += 1
        #        print self.count
        #        print response.meta['link']
        #        print error
        #        #yield Request(response.meta['link'],callback=self.parse_error)

        #    else:
        #        pass
                
            
        #self.f_handler.write("\n\n")
        #self.f_handler.write(str(errors))
        #self.f_handler.write("="*20)
        #self.f_handler.write("="*20)


    def parse_error(self,response):
        sel = Selector(response)
        errors = sel.xpath('//body/table/tr/td/pre[1]').extract()
        for error in errors:
            print error
            #if error.find('AssertionError')== -1:
            #    print response.meta['link']
            #    print error 
