import pytest
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pages.login_page import LoginPage


@pytest.fixture()
def browser():  # na metodzie jest wykonuwany, bo defacto nasz fixture steruje przeglądarką, są tu 3 wyrażne sekcje:

    browser = Chrome(executable_path=ChromeDriverManager().install())  # 1.co się wykona przed każdym testem:

    browser.get('http://demo.testarena.pl')  # 2. Ta sekcja mówi nam co chcemy zwrócić do testów, return -> ale aby zwrócić coś w połowie używamy ,,yield", czyli nas fixture wydaje z siebie do testów otwartą na stronie do testów przeglądarkę
    # żeby skojarzyć to z testami, to wrzucimy fixture jako argument naszej metody


    # w razie problemów rozwiązaniem byłoby time.sleep(1)

    yield browser  # słówko yield jest granicą sekcji, jezeli nie ma go to wykona się tylko 1 sekcja, jeżeli chcemy zwrócić więcej niż 1 zmienną browser, zwracamy je w tupli

    browser.quit()  # 3. coś co się wykona ZAWSZE po teście, niezaleznie od tego, czy się on uda, czy nie  (zeby wykonac 1 i 3 musimy skopiować 1 do 3?)


def test_arena(browser):

    login_page= LoginPage(browser)
    login_page.login('administrator@testarena.pl','sumXQQ72$L')

    # login_field = browser.find_element_by_id("email")
    # password_field = browser.find_element_by_id("password")
    # login_field.send_keys('administrator@testarena.pl')
    # password_field.send_keys('sumXQQ72$L')
    # button_login = browser.find_element_by_id('login')
    # button_login.click()

    admin_button = browser.find_element_by_css_selector('.header_admin a')
    admin_button.click()

    dodaj_projekt_button= browser.find_element_by_link_text('DODAJ PROJEKT')
    dodaj_projekt_button.click()

