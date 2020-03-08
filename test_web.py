from selenium.webdriver import Chrome  # z bibliotek import klasy, metody, itd.
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


# działa w sb

# ta biblioteka Webdriver_manager: 1. sprawdza wersję przegladrki
#2. sprawdza driver pod tą przeglądrakę:
#jeśli nie ma ściąga z netu do naszego katalogu
# ustawia zmienną systemową do Drivera, 2 metody i dzięki niej działa nam tu Selenium (zeby storować przeglądarke_
# mamy tu pytest (jak rider do testów) jeszcze i webdriver manager (ścieżka)

# jak działa Selenium: 1.piszemy kod (w Pythonie, Javie, ruby, C# 2. Napisany kod jest tłumaczony na json wire protocol
#3. Kod steruje webdrivermem (exe ->wykonywalnym), każda przegladrka ma osobny webdriver, chromedriver
#. HTTp server wtedy startuje i steruje przegladarkami
#kod -> manager sprawia , że ta warstwa jest przezroczysta (webdriver, chromedriver,gackodriver,safaridriver.)
#




# Test - uruchomienie Chroma
def test_my_first_chrome_selenium_test():
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
    # ustawiana automatycznie przez bibliotekę webdriver-manager
    browser = Chrome(executable_path=ChromeDriverManager().install())  #zmienna browser, paramtr metody ,,ściezka do chrom Drivera",

    # Otwarcie strony testareny - pierwsze użycie Selenium API
    browser.get('http://demo.testarena.pl/zaloguj')

    # Weryfikacja czy tytuł otwartej strony zawiera w sobie 'TestArena'
    assert 'TestArena' in browser.title  # ze tytuł się zgadza'''

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

     # albo maximize_window   # powiększymy okno przegladraki, max -maxymalizuje, full screen działa jak f11 i chowa pasek

    #jak wpiszemy browser.  to mamy dużo metod find element, najlepiej oczywiście by ,,id" -> ale id nie zawsze mamy na stronie
    # potem po klasie, która musi byc unikatowa, po name (nazwie) , po css selektor, by xpath i po link texcie (jak mam cpress -> odnosnik w texscie)
    # po kawalki linka

    # zamiast pisać browser.find_(By ID,'id')
    # to browser find_element_by_id('id')
    # szukamy listy -> find_elements


    # <div id = 'slawek' > </div>
    # browser.find_element(By ID, 'slawek')  # tu nie dajemy hasha
    #browser.find_element(By CSSselekto z hashem) chyba
    #browser.find_element(By CLASS_NAME,'cat') chyba
    #browser.find_element_by_css_selector("[name='heding']")
    #browser.find_element_by_id()

