# -*- coding: utf-8 -*-
from doubanallmovie.items import movieItem, commentItem
from scrapy import Spider, Request


class MovieSpider(Spider):
    '''
        main spider using the scrapy framework
        to crawl the douban.com for the comment
    '''
    name = 'movie'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/subject/27605698']  # 从一个电影开始

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse_index)

    def parse_index(self, response):
        # list数据
        performers = response.css('#info > span.actor > span.attrs a::text').extract()
        # 单变量数据
        title = response.css('#content > h1 > span:nth-child(1)::text').extract_first()
        time = response.css('#content > h1 > span.year::text').extract_first()
        diretor = response.css('#info > span:nth-child(1) > span.attrs > a::text').extract_first()
        screen_writer = response.css('#info > span:nth-child(3) > span.attrs a::text').extract_first()
        movie_type1 = response.css('#info > span:nth-child(8)::text').extract_first()
        movie_type2 = response.css('#info > span:nth-child(9)::text').extract_first()
        movie_length = response.css('#info > span:nth-child(20)::text').extract_first()
        score = response.css(
            '#interest_sectl > div.rating_wrap.clearbox > div.rating_self.clearfix > strong::text').extract_first()
        people_num = response.css(
            '#interest_sectl > div.rating_wrap.clearbox > div.rating_self.clearfix > div > div.rating_sum > a > span::text').extract_first()
        rate5 = response.css(
            '#interest_sectl > div.rating_wrap.clearbox > div.ratings-on-weight > div:nth-child(1) > span.rating_per::text').extract_first()
        rate4 = response.css(
            '#interest_sectl > div.rating_wrap.clearbox > div.ratings-on-weight > div:nth-child(2) > span.rating_per::text').extract_first()
        rate3 = response.css(
            '#interest_sectl > div.rating_wrap.clearbox > div.ratings-on-weight > div:nth-child(3) > span.rating_per::text').extract_first()
        rate2 = response.css(
            '#interest_sectl > div.rating_wrap.clearbox > div.ratings-on-weight > div:nth-child(4) > span.rating_per::text').extract_first()
        rate1 = response.css(
            '#interest_sectl > div.rating_wrap.clearbox > div.ratings-on-weight > div:nth-child(5) > span.rating_per::text').extract_first()

        # items = movieItem() #主页面的数据结构
        # for field in items.fields:
        #    items[field]=eval(field)#动态存储
        # yield items

        comment_url = response.url + 'comments?start={start}&limit={limit}'  # 评论页面
        for start in range(0, 220, 20):  # 这是无登陆
            yield Request(url=comment_url.format(start=start, limit=20), callback=self.parse_comments,
                          meta={'title': title})
        new_urls = response.css('#recommendations > div dl dt a::attr(href)').extract()  # 推荐电影 [:-18]
        for url in new_urls:
            yield Request(url=url[:-18], callback=self.parse_index)

    def parse_comments(self, response):
        items2 = commentItem()
        temp = response.css('#comments div.comment-item div.comment h3 span.comment-info')
        usernames = temp.css('a::text').extract()
        scores = temp.css('span:nth-child(3)::attr(title)').extract()
        times = temp.css('span:nth-child(4)::text').extract()
        comments = response.css('#comments div.comment-item div.comment p span.short::text').extract()
        votes = response.css('#comments div.comment-item div.comment h3 span.comment-vote span.votes::text').extract()
        # print(usernames,scores,times,comments,votes)
        title = response.meta['title']  # 从前一个页面得到的
        items2['movie_name'] = title
        for i in range(len(times)):
            items2['username'] = usernames[i]
            items2['score'] = scores[i]
            items2['time'] = times[i]
            items2['comment'] = comments[i]
            items2['vote'] = votes[i]
            yield items2
