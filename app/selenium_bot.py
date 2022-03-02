import platform
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class SeleniumBot:
    def __init__(self):
        service = Service(self.create_path())
        self.driver = webdriver.Chrome(service=service)

    def create_path(self):
        PATH = ""

        if platform.system() == "Darwin":
            # if macos show app verification problem
            # then go to driver/macOS using terminal
            # then execute: xattr -d com.apple.quarantine chromedriver
            PATH = "app/driver/MacOS/chromedriver"

        # please test in windows and Linux os
        elif platform.system() == "Windows":
            PATH = "app/driver/Windows/chromedriver.exe"

        elif platform.system() == "Linux":
            PATH = "app/driver/Linux/chromedriver"

        else:
            print("We only support Windows, MacOS and Linux OS!!")

        return PATH

    def visit_website(self, url: str):

        if self.driver:
            self.driver.get(url)


if __name__ == '__main__':
    sb = SeleniumBot()
    sb.visit_website("https://www.nytimes.com/games/wordle/index.html")
