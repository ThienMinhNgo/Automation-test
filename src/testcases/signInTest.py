import sys
sys.path.append(r".\src")

from base.browserSetup import Browser
from base.testTool import TestTool
from pages.signInPage import SignInPage
from pages.dashBoardPage import DashboardPage


class SignInTest(TestTool):
    def __init__(self, params):
        super().__init__()
        print("----------SignIn Test----------")
        self.browserType = params['browserType']
        self.loginUrl = params['loginUrl']
        self.email = params['email']
        self.passWord = params['passWord']
        self.textConfirm = params['textConfirm']

        self.driver = Browser(self.browserType).driverSetup(self.loginUrl)
        self.signInPage = SignInPage(self.driver)
        self.dashboardPage = DashboardPage(self.driver)

    def run(self):
        self.signInPage.input_email(self.email)
        self.signInPage.input_password(self.passWord)
        self.signInPage.login_summit()
        self.assertEqual(self.dashboardPage.get_welcome_text(), self.textConfirm)



