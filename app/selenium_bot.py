import platform
from selenium import webdriver

class SeleniumBot:

    def __init__(self):
        self.driver = self._init_selenium_driver()

    def _init_selenium_driver(self):

        PATH = ""

        if platform.system() == "Darwin":
            # if macos show app verification problem
            # then go to driver/macOS using terminal
            # then execute: xattr -d com.apple.quarantine chromedriver
            PATH = "driver/MacOS/chromedriver"

        # please test in windows and Linux os
        elif platform.system() == "Windows":
            PATH = "driver/Windows/chromedriver.exe"

        elif platform.system() == "Linux":
            PATH = "driver/Linux/chromedriver"
        
        else:
            print("We only support Windows, MacOS and Linux OS!!")

        return webdriver.Chrome(PATH)

    def visit_website(self, url: str):

        if self.driver:
            self.driver.get(url)


if __name__ == '__main__':
    sb = SeleniumBot()
    sb.visit_website("https://google.com")