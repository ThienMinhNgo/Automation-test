import sys
sys.path.append(r".\src")

from base.browserSetup import Browser
from base.testTool import TestTool
from pages.signInPage import SignInPage
from pages.dashBoardPage import DashboardPage


class RememberBtnTest (TestTool):
    def __init__(self, params):
        super().__init__()
        print("----------RememberBtn Test----------")
        self.browserType = params['browserType']
        self.loginUrl = params['loginUrl']
        self.emailPlaceholder = params['emailPlaceholder']
        self.passWordPlaceholder = params['passWordPlaceholder']

        self.driver = Browser(self.browserType).driverSetup(self.loginUrl)
        self.signInPage = SignInPage(self.driver)

    def run(self):
        compareEmail = self.assertEqual(self.signInPage.get_email_placeholder(), self.emailPlaceholder)
        comparePass = self.assertEqual(self.signInPage.get_password_placeholder(), self.passWordPlaceholder)
        if compareEmail == True and comparePass == True:
            self.signInPage.click_rememberBtn()
            self.signInPage.verify_rememberBtn_checked()
        else:
            print("emailPlaceholder or passwordPlaceholder wrong !")
