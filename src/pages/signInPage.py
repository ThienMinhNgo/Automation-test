from seleniumpagefactory.Pagefactory import PageFactory

class SignInPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
                'emailInput': ('XPATH', '//input[contains(@name,"email")]'),
                'passwordInput': ('XPATH', '//input[contains(@name,"password")]'),
                'rememberMeBtn': ('XPATH', '//label[contains(text(),"Remember Me")]'),
                'loginSumitBtn': ('XPATH', '//button[contains(@type,"submit")]'),
    }

    def input_email(self, email):
        try:
            self.emailInput.set_text(email)
            print("Input email: SUCCESS")
        except Exception as e:
            print(f"Input email FAIL: {str(e)}")

    def input_password(self, password):
        try:
            self.passwordInput.set_text(password)
            print("Input password: SUCCESS")
        except Exception as e:
            print(f"Input password FAIL: {str(e)}")

    def login_summit(self):
        try:
            self.loginSumitBtn.click()
            print("Login summit: SUCCESS")
        except Exception as e:
            print(f"Login summit FAIL: {str(e)}")

    def click_rememberBtn(self):
        try:
            self.rememberMeBtn.click()  
            print("Click rememberBtn: SUCCESS")
        except Exception as e:
            print(f"Click rememberBtn FAIL: {str(e)}")

    def get_email_placeholder(self):
        try:
            email_placeholder = self.emailInput.getAttribute('placeholder')
            print(f'Email placeholder: {email_placeholder}')
            return email_placeholder
        except Exception as e:
            print(f"Get email placeholder FAIL: {str(e)}")
            return None
        
    def get_password_placeholder(self):
        try:
            password_placeholder = self.passwordInput.getAttribute('placeholder')
            print(f'Password placeholder: {password_placeholder}')
            return password_placeholder
        except Exception as e:
            print(f"Get password placeholder FAIL: {str(e)}")
            return None

    def verify_rememberBtn_checked(self):
        script = "return document.getElementsByClassName('custom-checkbox')[0].children[0].checked"
        is_checked = self.driver.execute_script(script)
        print(f'RememberBtn checked: {is_checked}')
        

