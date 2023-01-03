from seleniumpagefactory.Pagefactory import PageFactory
from base.browserSetup import Browser

class DashboardPage(PageFactory, Browser):
    def __init__(self, driver):
        self.driver = driver
        self.pageLoadTimeOut = 30

    locators = {
                'welcomeUser': ('XPATH', '//span[contains(@class,"author__meta")]')
    }

    def get_welcome_text(self):
        try:
            text = self.welcomeUser.get_text()
            print(f"Welcome text: {text}")
            return text
        except Exception as e:
            print(f"Get welcome text FAIL: {str(e)}")
            return None

    def page_load_check(self):
        timeOut = self.pageLoadTimeOut
        while timeOut > 0:
            pageLoad =  self.driver.execute_script('return document.readyState;')
            if pageLoad == 'complete':
                break
            timeOut -= 1