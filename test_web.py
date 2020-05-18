from selenium.webdriver import Chrome  
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager



# webdriver_manager:  sprawdza wersję przegladrki i driver pod tą przeglądrakę:
# jeśli czegoś brakuje - ściąga to z netu, do naszego katalogu


# Jak działa Selenium?
# 1.Piszemy kod w Pythonie, Javie, ruby,lub C#  a następnie napisany kod jest tłumaczony na json wire protocol
#3. Kod steruje webdriverem (exe ->wykonywalnym), a każda przegladarka ma osobny webdriver,
#. wtedy uruchamia się HTTP server i steruje przegladarkami





# Test - uruchomienie Chrome
def test_my_first_chrome_selenium_test():
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
    # ustawiana automatycznie przez bibliotekę webdriver-manager
    browser = Chrome(executable_path=ChromeDriverManager().install())#w zmiennej browser,jako parametr metody mamy ściezkę do ChromeDrivera,

    # Otwarcie strony testareny - pierwsze użycie Selenium API
    browser.get('http://demo.testarena.pl/zaloguj')

    # Weryfikacja czy tytuł otwartej strony zawiera w sobie 'TestArena'
    assert 'TestArena' in browser.title  

    # Zamknięcie przeglądarki
    browser.quit()




# Test - uruchomienie Firefoxa
def test_my_first_firefox_selenium_test():

    # Uruchomienie przeglądarki Firefox. Ścieżka do geckodrivera (drivera dla Firefoxa), automatycznie przez bibliotekę webdriver-manager

    browser = Firefox(executable_path=GeckoDriverManager().install())


    # Otwarcie strony www.google.pl

    browser.get('https://www.google.pl/')  # pobieramy stronę, ta metoda otwiera jakiś adres w sieci

    # Weryfikacja tytułu

    assert 'Google' in browser.title  # ze tytuł się zgadza, potem robimy asrecję

    browser.fullscreen_window()

    # Zamknięcie przeglądarki
    browser.quit() #

    
    
   


    
