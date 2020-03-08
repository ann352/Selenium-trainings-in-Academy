import pytest
import time
from selenium.webdriver import Chrome    # działa w sb
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

@pytest.fixture()

def browser():   # na metodzie jest wykonuwany, bo defacto nasz fixture steruje przeglądarką, są tu 3 wyrażne sekcje:


    browser = Chrome(executable_path=ChromeDriverManager().install())    # 1.co się wykona przed każdym testem:

    browser.get('https://www.awesome-testing.com/')  # 2. Ta sekcja mówi nam co chcemy zwrócić do testów, return -> ale aby zwrócić coś w połowie używamy ,,yield", czyli nas fixture wydaje z siebie do testów otwartą na stronie do testów przeglądarkę
                                                     # żeby skojarzyć to z testami, to wrzucimy fixture jako argument naszej metody
    cookie = { 'name':'displayCookieNotice', 'value': 'y', 'domain':'www.awesome-testing.com'}
    browser.add_cookie(cookie)  #ciastka bierzemy ze strony -> aplication -> Cookies (klikamy ok na str z ciastkiem) -> refresh -> ciastko i wartości
    browser.refresh()

    # w razie problemów rozwiązaniem byłoby time.sleep(1)

    yield browser  # słówko yield jest granicą sekcji, jezeli nie ma go to wykona się tylko 1 sekcja, jeżeli chcemy zwrócić więcej niż 1 zmienną browser, zwracamy je w tupli

    browser.quit()   # 3. coś co się wykona ZAWSZE po teście, niezaleznie od tego, czy się on uda, czy nie  (zeby wykonac 1 i 3 musimy skopiować 1 do 3?)




def test_post_count(browser):  # wrzucając tu argument powiążemy metodę z testami i wywalamy zduplikowane linie kodu
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
    # ustawiana automatycznie przez bibliotekę webdriver-manager


    # Pobranie listy tytułów   bo było <h1 class = 'a b' i selector .a b
    list_of_post = browser.find_elements(By.CSS_SELECTOR,
                                         '.post-title a')  # a, bo mam to głębiej, ale nie musi być tego a i tak nam zczyta

    # Asercja że lista ma 4 elementy
    assert len(list_of_post) == 4




def test_post_count_after_search(browser):
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
    # ustawiana automatycznie przez bibliotekę webdriver-manager


    # Inicjalizacja searchbara i przycisku search
    search_input = browser.find_element_by_css_selector("input.gsc-input")
    search_button = browser.find_element_by_css_selector('.gsc-search-button')
    # Szukanie

    search_input.send_keys('cypress')
    search_button.click()

    # Czekanie na stronę
    wait = WebDriverWait(browser, 10)
    grey_status_bar = (By.CLASS_NAME, 'status-msg-body')
    wait.until(expected_conditions.visibility_of_element_located(grey_status_bar))

    # Pobranie listy tytułów
    list_of_post = browser.find_elements(By.CSS_SELECTOR, '.post-title a')

    # Asercja że lista ma 3 elementy
    assert len(list_of_post) == 3





def test_post_count_on_cypress_label(browser):
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera


    # Inicjalizacja elementu z labelką
    category = browser.find_element_by_link_text('Cypress')

    # Kliknięcie na labelkę
    category.click()

    # Czekanie na stronę
    wait=WebDriverWait(browser,10)
    grey_status_bar=(By.CLASS_NAME,'status-msg-body')
    wait.until(expected_conditions.visibility_of_element_located(grey_status_bar))

    # Pobranie listy tytułów
    list_of_entries = browser.find_elements(By.CSS_SELECTOR, '.post-title a')

    # Asercja że lista ma 1 element
    assert len(list_of_entries) == 1



# # kolejność zdarzeń:
# # fixture skojarzony z testem -> odplamy sekcje I
# # yield skaczemy do metody testowej, jak to się wykona skaczemy do sekcji 3
