class LoginPage:

    def __init__(self,browser):
        self.browser = browser

    def login(self, email, password):
        login_field = self.browser.find_element_by_id("email")
        password_field = self.browser.find_element_by_id("password")
        button_login = self.browser.find_element_by_id("login")

        login_field.send_keys('administrator@testarena.pl')
        password_field.send_keys('sumXQQ72$L')
        button_login = self.browser.find_element_by_id('login')
        button_login.click()