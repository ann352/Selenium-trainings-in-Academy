import pytest    # test działa w sb
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_post_count():
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
    # ustawiana automatycznie przez bibliotekę webdriver-manager
    browser = Chrome(executable_path=ChromeDriverManager().install())

    # Otwarcie strony

    browser.get('https://www.awesome-testing.com/')

    # Pobranie listy tytułów   bo było <h1 class = 'a b' i selector .a b
    list_of_post = browser.find_elements(By.CSS_SELECTOR,
                                         '.post-title a')  # a, bo mam to głębiej, ale nie musi być tego a i tak nam zczyta

    # Asercja że lista ma 4 elementy
    assert len(list_of_post) == 4

    # Zamknięcie przeglądarki

    browser.quit()


def test_post_count_after_search():
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
    # ustawiana automatycznie przez bibliotekę webdriver-manager
    browser = Chrome(executable_path=ChromeDriverManager().install())

    # Otwarcie strony

    browser.get('https://www.awesome-testing.com/')

    # Inicjalizacja searchbara i przycisku search
    search_input = browser.find_element_by_css_selector("input.gsc-input")
    search_button = browser.find_element_by_css_selector('.gsc-search-button')
    # Szukanie

    search_input.send_keys('cypress')
    search_button.click()

    # Czekanie na stronę
    time.sleep(5)  # czekamy na posty

    # Pobranie listy tytułów
    list_of_post = browser.find_elements(By.CSS_SELECTOR, '.post-title a')

    # Asercja że lista ma 3 elementy
    assert len(list_of_post) == 3

    # Zamknięcie przeglądarki
    browser.quit()


def test_post_count_on_cypress_label():
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera

    # ustawiana automatycznie przez bibliotekę webdriver-manager
    browser = Chrome(executable_path=ChromeDriverManager().install())

    # Otwarcie strony
    browser.get('https://www.awesome-testing.com/')

    # Inicjalizacja elementu z labelką
    category = browser.find_element_by_link_text('Cypress')

    # Kliknięcie na labelkę
    category.click()

    # Czekanie na stronę
    time.sleep(5)

    # Pobranie listy tytułów
    list_of_entries = browser.find_elements(By.CSS_SELECTOR, '.post-title a')

    # Asercja że lista ma 1 element
    assert len(list_of_entries) == 1

    # Zamknięcie przeglądarki
    browser.quit()
