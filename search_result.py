from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def self(args):
    pass

class SearchResultPage:

    def __init__(self, browser):
        self.browser = browser

    def wait_for_load(self):

        wait = WebDriverWait(self.browser,10)
        grey_status_bar = (By.CLASS_NAME, 'status-msg-body')
        wait.until(expected_conditions.visibility_of_element_located(grey_status_bar))


    def get_list_of_titles(self, expected_count):
        list_of_post = self.browser.find_elements(By.CSS_SELECTOR, '.post-title a')

        # Asercja że lista ma 3 elementy
        assert len(list_of_post) == expected_count






