from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, browser):
        self.browser = browser

    def verify_post_count(self,expected_count):
        list_of_post = self.browser.find_elements(By.CSS_SELECTOR, '.post-title a')
        assert len(list_of_post) == expected_count

    def search (self, search_term):

        search_input = self.browser.find_element_by_css_selector("input.gsc-input")
        search_button = self.browser.find_element_by_css_selector('.gsc-search-button')
        # Szukanie

        search_input.send_keys(search_term)
        search_button.click()




    def click_label (self,label):
        label = self.browser.find_element_by_link_text(label)
        label.click()


