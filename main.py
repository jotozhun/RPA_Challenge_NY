import time
import requests

from objects.NYNEWS_OBJ import NYNEWS_OBJ
from utils.utils import map_categories_to_index
from utils.nytimes_vars import *
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from SeleniumLibrary.errors import ElementNotFound

nynews_obj = NYNEWS_OBJ(url=NYTIMES_URL)
word = "murder"
categories = ["Arts", "U.S.", "World"]

today_date = datetime.now()
print(today_date.strftime(EXECUTION_NAME_FORMAT))

categories_indexes = map_categories_to_index(categories, CATEGORIES_MAP_INDEX)

# Define a main() function that calls the other functions in order:
def main():
    try:
        nynews_obj.click_on_btn()
        nynews_obj.search_for(word=word)
        # time.sleep(5)

        nynews_obj.click_on_element("css:select.css-v7it2b")
        nynews_obj.press_key("css:select.css-v7it2b", "DOWN")
        # time.sleep(5)
        nynews_obj.click_on_btn("css:button.css-4d08fs")
        nynews_obj.wait_for_element_to_be_present("css:div.css-tw4vmx")
        # time.sleep(1)
        # parent_div = nynews_obj.browser_lib.find_element("css:div.css-tw4vmx")
        category_elements = nynews_obj.browser_lib.find_elements('css:input[type="checkbox"]')
        for category_index in categories_indexes:
            category_elements[category_index].click()
        nynews_obj.click_on_btn("css:button.popup-visible.css-4d08fs")


        nynews_obj.click_on_btn("css:button.css-p5555t")
        nynews_obj.wait_for_element_to_be_present("css:div.css-91q1y8")

        date_options = nynews_obj.browser_lib.find_elements('css:button.css-jba1a6')
        date_options[-1].click()

        specific_date_inputs = nynews_obj.browser_lib.find_elements("css:input.css-9wn7z1")
        start_date = today_date.replace(day=1) - relativedelta(month=1)

        specific_date_inputs[0].send_keys(start_date.strftime(STANDARD_DATE_FORMAT))
        specific_date_inputs[1].send_keys(today_date.strftime(STANDARD_DATE_FORMAT))

        nynews_obj.click_on_btn("css:button.css-p5555t.popup-visible.calendar-open")

        # title_elements = nynews_obj.browser_lib.find_elements("css:h4.css-2fgx4k")
        # date_elements = nynews_obj.browser_lib.find_elements("css:span.css-17ubb9w")
        # description_elements = nynews_obj.browser_lib.find_elements("css:p.css-16nhkrn")

        news_elements = nynews_obj.browser_lib.find_elements("css:li.css-1l4w6pd")
        for news_element in news_elements:
            title_element = nynews_obj.browser_lib.find_element("css:h4.css-2fgx4k", news_element).text
            date_element = nynews_obj.browser_lib.find_element("css:span.css-17ubb9w", news_element).text
            description_element = nynews_obj.browser_lib.find_element("css:p.css-16nhkrn", news_element).text
            try:
                image = nynews_obj.browser_lib.find_element("css:img.css-rq4mmj", news_element)
                image_url = image.get_attribute("src")
                image_filename = image_url.split("/")[-1].split("?")[0]
                # with open(f"logs/{today_date.strftime(EXECUTION_NAME_FORMAT)}/images/{image_filename}", "wb") as file:
                with open(image_filename, "wb") as file:
                    image_response = requests.get(image_url, stream=True)
                    for image_batch in image_response.iter_content(1024):
                        if not image_batch:
                            break
                        file.write(image_batch)
            except ElementNotFound as e:
                print("not found")

        time.sleep(15)

    finally:
        nynews_obj.quit_browsers()


# Call the main() function, checking that we are running as a stand-alone script:
if __name__ == "__main__":
    main()