from RPA.Browser.Selenium import Selenium

class NYNEWS_OBJ:

    def __init__(self, url: str) -> None:
        self.url = url
        self.browser_lib = Selenium()
        self.__initialize()


    def __initialize(self):
        self.browser_lib.open_available_browser(self.url)
        self.browser_lib.maximize_browser_window()


    def search_for(self, word, css_exp="css:input.css-1j26cud"):
        self.browser_lib.input_text(css_exp, word)
        self.browser_lib.press_keys(css_exp, "ENTER")


    def click_on_btn(self, css_exp="css:button.css-tkwi90.e1iflr850"):
        self.browser_lib.click_button(css_exp)


    def click_on_element(self, css_exp: str):
        self.browser_lib.click_element(css_exp)


    def quit_browsers(self):
        self.browser_lib.close_all_browsers()


    def press_key(self, css_exp: str, key_name: str):
        self.browser_lib.press_keys(css_exp, key_name)


    def wait_for_element_to_be_present(self, css_exp: str):
        self.browser_lib.wait_until_element_is_visible(css_exp)
