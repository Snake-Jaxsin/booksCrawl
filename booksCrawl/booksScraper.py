import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BooksscraperSpider(CrawlSpider):
    name = 'booksScraper'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/catalogue/category/books/sequential-art_5/page-1.html']

    #rules
    link_details = LinkExtractor(restrict_css='h3 > a') #
    link_rule = Rule(link_details, callback='parse_item', follow=False)


    next_details = LinkExtractor(restrict_css='li.next > a') # next botton
    next_rule = Rule(next_details, follow=True)

    categories_details = LinkExtractor(restrict_css='.side_categories > ul > li > ul > li a') # categories
    categories_rule = Rule(categories_details, follow=True)

    rules = (
        link_rule,
        categories_rule,
        next_rule
    )

    def parse_item(self, response):
        yield {
            'Title': response.css('h1::text').get(),
            'Category': response.css('a ::text')[3].get(),
            'Price': response.css('p.price_color::text').get(),
            'Available': response.css('p.instock.availability::text')[1:2].get().replace('\n', '').strip(),
            'link': response.url,
        }
