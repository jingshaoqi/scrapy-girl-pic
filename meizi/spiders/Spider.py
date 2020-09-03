from scrapy import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from meizi.items import MeiziItem

class Meizi(CrawlSpider):
    name = 'meizi'
    allowed_domains = ['mzitu.com']
    start_urls = ['https://www.mzitu.com/']
    img_urls = []
    rules = (
        Rule(LinkExtractor(allow=('https://www.mzitu.com/')), callback='parse_item', follow=False),
    )

    def parse_item(self,response):
        print('enter parse_item-----------')
        with open('res.html','w') as f:
            f.write(response.text)
        imgs = response.xpath('//div[@class="main-content"]/div[@class="postlist"]/ul/li/a/img')
        for i in imgs:
            next_src = i.xpath('//@data-original').extract_first()
            alt = i.xpath('//@alt').extract_first()
            item = MeiziItem()
            item['name'] = alt
            item['url'] = response.url
            item['images_urls'] = next_src
            print(item)
            yield item
            break
