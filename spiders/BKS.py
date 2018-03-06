# -*- coding: utf-8 -*-
import scrapy
import requests,re
from BokeSpider.items import BokespiderItem
from scrapy.http import Request


class BksSpider(scrapy.Spider):
    name = 'BKS'
    allowed_domains = ['hexun.com']
    def start_requests(self):
        #重写start_url为起始爬虫爬取网页数据增加请求头
        yield Request(url='http://fjrs168.blog.hexun.com/p57/default.html',headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)"
                                 " Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"})


    def parse(self, response):
        item = BokespiderItem()
        item['name']=response.css("span.ArticleTitleText a::text").extract()
        item['url']=response.css("span.ArticleTitleText a::attr(href)").extract()
        #点击数和评论数为js动态加载，找出其内容所在url爬取并获取所需内容
        c_c_url = re.findall(r'<script type="text/javascript" src="(http://click.tool.*?)"></script>',str(response.body))[0]
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)"
                                 " Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"}
        data = requests.get(c_c_url,headers=headers).text
        item['hits']=re.findall(r"click.*?,'(.*?)'",data)
        item['comment'] = re.findall(r"comment.*?,'(.*?)'", data)
        yield item

        #获取下一页url用来爬取所有页数据
        next_url = response.css(".PageSkip_1 a[title='下一页']::attr(href)").extract_first("")
        if next_url:
            yield Request(url=next_url,callback=self.parse,headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)"
                                 " Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"})

