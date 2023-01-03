from signInTest import SignInTest
from rememberBtnTest import RememberBtnTest

##-----------------------Test Case 1----------------------------
params = {
    'browserType': 'chrome',
    'loginUrl': 'https://phptravels.net/login',
    'email': 'user@phptravels.com',
    'passWord': 'demouser',
    'textConfirm': 'Welcome Back'
}

signInTest = SignInTest(params)
signInTest.run()

##-----------------------Test Case 2----------------------------
# params = {
#     'browserType': 'chrome',
#     'loginUrl': 'https://phptravels.net/login',
#     'emailPlaceholder': 'Email',
#     'passWordPlaceholder': 'Password',
# }

# rememberBtnTest = RememberBtnTest(params)
# rememberBtnTest.run()    