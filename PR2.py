import scrapy


class QuotesSpider(scrapy.Spider):

    # Задаём имя паука.
    name = "quotes"
    # Сайт для примера.
    start_urls = [
        "https://quotes.toscrape.com/page/1/",
    ]
    # Принимает объект response, содержащий скачанные данные страницы.
    def parse(self, response):
        for quote in response.css("div.quote"):
            # Извлекаем информацию.
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("span small::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall(),
            }

        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)