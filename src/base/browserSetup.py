from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class Browser():
    
    def __init__(self, browserType):
        self.browserType = browserType
        self.pageLoadTimeOut = 30
        pass
    
    def driverSetup(self, urlStart):
        match self.browserType:
            case "chrome":
                self.driver = self.initChromeDriver(urlStart)
            case "firefox":
                self.driver = self.initFirefoxDriver(urlStart)
            case "opera":
                self.driver = self.initOperaDriver(urlStart)
            case _:
                print("Browser: " + self.browserType + " is invalid, Launching Chrome as browser of choice...")
                self.browserType = "chrome"
                self.driver = self.initChromeDriver(urlStart)
        return self.driver

    def initChromeDriver(self, urlStart):
        print("Launching Chrome browser...")
        self.driverPath = "resourses/" +  "chromedriver.exe"
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.chromeDriver = webdriver.Chrome(service = Service(self.driverPath), chrome_options= options)
        self.chromeDriver.get(urlStart)
        self.page_load_check()
        return  self.chromeDriver
    
    def initFirefoxDriver(self, urlStart):
        pass

    def initOperaDriver(self, urlStart):
        pass
    
    def page_load_check(self):
        timeOut = self.pageLoadTimeOut
        while timeOut > 0:
            pageLoad =  self.chromeDriver.execute_script('return document.readyState;')
            if pageLoad == 'complete':
                break
            timeOut -= 1

