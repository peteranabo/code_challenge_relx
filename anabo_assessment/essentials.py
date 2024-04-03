from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service


class SeleniumPackage:

    """
    Initializes the SeleniumPackage class
    """

    def __init__(self):

        self.service = Service()
        self.opts = ChromeOptions()
        self.opts.add_experimental_option("detach", True)
        #self.opts.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.opts.add_experimental_option('useAutomationExtension', False)
        self.driver = Chrome(service=self.service, options=self.opts,)
        self.wait = WebDriverWait(self.driver, 3600)



instanced_selenium_package = SeleniumPackage()