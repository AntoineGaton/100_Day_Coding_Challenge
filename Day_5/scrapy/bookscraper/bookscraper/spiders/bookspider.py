#scrapy crawl bookspider
import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        # List of books
        books = response.css('article.product_pod')

        print('------------>', response.css('li.next a::attr(href)').get())

        for book in books:
            yield {
                'title' : book.css('h3 a::attr(title)').get(),
                'price' : book.css('.price_color::text').get(),
                'image' : book.css('.image_container img::attr(src)').get(),
                'url' : book.css('h3 a::attr(href)').get()
            }

        # Next page url
        # Got this from the button on the page
        next_page = response.css('li.next a::attr(href)').get()

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
        