#scrapy crawl bookspider
#try spotify with scrapy
import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        # List of books
        books = response.css('article.product_pod')

        print('------------>', response.css('article.product_pod').get())
        print('------------>', response.css('li.next a::attr(href)').get())
        print('------------>', response.css('li.next a::attr(href)').get())

        for book in books:
            # Next page url
            # Got this from the button on the page
            book_url = response.css('h3 a::attr(href)').get()

            # If there is a next page, go to it
            if next_page is not None:
                # If the url doesn't have catalogue/ in it, add it
                if "catalogue/" in next_page:
                    next_page_url = "https://books.toscrape.com/" + next_page
                    print('------------>', next_page_url)
                else:
                    next_page_url = "https://books.toscrape.com/catalogue/" + next_page
                    print('------------>', next_page_url)
                yield response.follow(next_page_url, callback=self.parse)

    def parse_book_page(self, response):
            pass
            