import scrapy
import tripadvisor_scrapper.helpers as helpers

from tripadvisor_scrapper.items import Location, RatingDetail

class RatingSpider(scrapy.Spider):
    name = "ratings"

    def start_requests(self):
        urls = [
            u"https://www.tripadvisor.com.br/Restaurant_Review-g303631-d2639583-Reviews-Bacio_di_Latte-Sao_Paulo_State_of_Sao_Paulo.html"
            # ,u"https://www.tripadvisor.com.br/Restaurant_Review-g303631-d5316821-Reviews-Bacio_di_Latte_Shopping_JK_Iguatemi-Sao_Paulo_State_of_Sao_Paulo.html"
        ]

        for url in urls:
            yield scrapy.Request(url=url) 

    def parse(self, response):
    
        # Get overall rating and total rating count
        name = response.css('div.restaurantName .ui_header::text').get()
        street_address = response.css('div.businessListingContainer .blEntry.address span.detail span.street-address::text').get()
        extended_address = response.css('div.businessListingContainer .blEntry.address span.detail span.extended-address::text').get()
        locality = response.css('div.businessListingContainer .blEntry.address span.detail span.locality::text').get()
        phone_number = response.css('div.businessListingContainer .blEntry.phone span.detail::text').get()
        opening_hours = response.css('div.locationHoursContainer .locationHoursInner [class^="public-location-hours-LocationHours__hoursOpenerText"] span:nth-child(2)::text').get()
        overall_rating = helpers.str_to_float(response.css('[class|="restaurants-detail-overview-cards-RatingsOverviewCard__overallRating"]::text').get())
        rating_count = helpers.str_to_int(response.css('[class|="restaurants-detail-overview-cards-RatingsOverviewCard__ratingCount"]::text').get())
        
        # Get detailed ratings
        rating_details = []
        detail_items = response.css('#REVIEWS .ppr_rup.ppr_priv_detail_filters:first-child [data-prwidget-name="filters_detail_checkbox"]:first-child .content .choices div.ui_checkbox.item')
        for detail in detail_items:
            rating_details.append(dict(RatingDetail(
                label = detail.css("label.row_label.label::text").get(),
                rating = helpers.str_to_int(detail.css("span.row_num::text").get())
            )))

        return Location(
            url = response.url,
            name = name,
            street_address = street_address,
            extended_address = extended_address,
            locality = locality,
            phone_number = phone_number,
            opening_hours = opening_hours,
            overall_rating = overall_rating,
            rating_count = rating_count,
            rating_details = rating_details
        )
