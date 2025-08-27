import scrapy

class QuotesSpider(scrapy.Spider):

    ### STEP 3.1 ADD CODE HERE ### 
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):

        ### STEP 3.2 ADD CODE HERE ### 
        quotes = response.css('div.quote')

        self.log(f"Found {len(quotes)} quotes on the page")

        # Iterate over each quote found and yield the extracted data
        

        ### STEP 4.1 ADD CODE HERE ### 
        for current_quote in quotes:
            yield {
                'quote': current_quote.css('span.text::text').get(),
                'author': current_quote.css('small.author::text').get()
            }

        # Follow pagination link (Next button)
        ### STEP 5.1 ADD CODE HERE ### 
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
