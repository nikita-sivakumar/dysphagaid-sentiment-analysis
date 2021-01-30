import scrapy


class SafestrawReviewSpider(scrapy.Spider):
    name = 'safestraw_review'
    # allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/Bionix-Safestraw-Drinking-Thickened-Liquids/product-reviews/B00L3D2MY0/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews',
                    'https://www.amazon.com/Bionix-Safestraw-Drinking-Thickened-Liquids/product-reviews/B00L3D2MY0/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=2']
    def parse(self, response):
        data = response.css('#cm_cr-review_list')
        
        # Collect username
        user_names = data.css('.a-profile-name')

        # Collect product star ratings
        star_ratings = data.css('.review-rating')

        # Collect review title
        review_titles = data.css('.review-title')
        
        # Collecting user review
        comments = data.css('.review-text')
        count = 0
        
        # Combining results
        for review in star_ratings:
            yield{  'username':''.join(user_names[count].xpath(".//text()").extract()),
                    'stars': ''.join(review.xpath('.//text()').extract()),
                    'review_title':''.join(review_titles[count].xpath(".//text()").extract()),
                    'comment': ''.join(comments[count].xpath(".//text()").extract())
                     }
            count=count+1
