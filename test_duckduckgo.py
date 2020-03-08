from selenium.webdriver import Chrome    # działa w sb
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_searching_in_duckduckgo():
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
    # ustawiana automatycznie przez bibliotekę webdriver-manager
    browser = Chrome(executable_path=ChromeDriverManager().install())

    # Otwarcie strony duckduckgo

    browser.get('https://duckduckgo.com/')
    # Znalezienie paska wyszukiwania

    search_form_ = browser.find_element(By.CSS_SELECTOR,'#search_form_input_homepage')

    # Znalezienie guzika wyszukiwania (lupki)

    search_button = browser.find_element_by_id('search_button_homepage')
    # metoda submit to to samo co click w 90%

    # send.Keys ('tekst'), na elemencie możemy też zrobić asercje



    # Asercje że elementy są widoczne dla użytkownika

    assert search_button.is_displayed()   #nasze zmienne tu wrzucamy i możemy też dla czytelnika, napisać is True

    assert search_form_.is_displayed()

    # Szukanie Vistula University

    search_form_.send_keys("Vistula Uniwersity")  #wyślij klucze
    search_button.click()                   #kliknij

    # Sprawdzenie że jakikolwiek wynik ma tytuł 'Vistula University in Warsaw',nie że pierwszy, ale, że jakikolwiek wynik ma taki tytuł

    #lista el. z tytułem, czyli selector typu result_title

    list = browser.find_elements(By.CSS_SELECTOR, '.result_title')   #tworzymy listę elementów z tytułami

    # browser.find_element  zwraca nam unikatowy el, a jak on nie jest unikatowy zwraca pierwszy wynik
    # browser.find_elements zwraca nam wszystkie element

    list_of_titles = []  # tworzymy pustą listę i do każdego el. dodajemy i text, listę el selenium, przrobilismy na stringi i sprawdzamy cz nasz text tu jest
    for i in list:
        list_of_titles.append(i.text)
        assert 'Vistula University in Warsaw' in list_of_titles

    # Zamknięcie przeglądarki

    browser.quit()
