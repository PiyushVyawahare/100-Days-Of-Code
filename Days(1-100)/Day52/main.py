import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = "D:\Desktop\Web Development\chromedriver_win32\chromedriver.exe"
USERNAME = "piyushvyawahare2021@gmail.com"
PASSWORD = "Pbv@5807"
SIMILAR_ACCOUNT = "coding_for_beginners_"


class InstaFollower:
    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")

        time.sleep(3)

        username = self.driver.find_element_by_name("username")
        username.send_keys(USERNAME)

        password = self.driver.find_element_by_name("password")
        password.send_keys(PASSWORD)

        password.send_keys(Keys.ENTER)

        time.sleep(3)
        not_now = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_now.click()

        time.sleep(2)
        notNow = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
        notNow.click()

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(2)
        followers = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
