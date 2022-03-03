import platform
from pynput.keyboard import Key, Controller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time


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
            PATH = "driver/MacOS/chromedriver"

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

    def accept_tac(self, wait_time: int = 1):
        btn_id = "pz-gdpr-btn-accept"

        try:
            get_btn = WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located((By.ID, btn_id))
            )
            get_btn.click()

        except NoSuchElementException as NSE:
            print(NSE)
    
    def close_instruction(self, wait_time: int = 1):
        # Need to improve
        self.driver.find_element_by_xpath("//body").click()
    
    #buggy function. need to improve
    def key_press(self, word: str):
        # pynput working good.
        # need to improve.

        keyboard = Controller()

        for w in word:
            keyboard.press(w)
            keyboard.release(w)

        keyboard.press(Key.enter)
        time.sleep(3)


if __name__ == '__main__':
    sb = SeleniumBot()
    sb.visit_website("https://www.nytimes.com/games/wordle/index.html")

    sb.accept_tac()
    sb.close_instruction()
    sb.key_press("pzazz")
    sb.key_press("jazzy")
    sb.key_press("buzzy")
    sb.key_press("fuzzy")
    sb.key_press("muzzy")
    sb.key_press("bezzy")
