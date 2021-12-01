import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

URL = "https://www.linkedin.com/jobs/search/?f_AL=true&f_WT=2&keywords=python%20developer"
chrome_driver_path = "D:\Desktop\Web Development\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(URL)

time.sleep(2)

sign_in = driver.find_element_by_xpath("/html/body/div[1]/header/nav/div/a[2]")
sign_in.click()

time.sleep(5)

username = driver.find_element_by_id("username")
username.send_keys("piyushvyawahare2001@gmail.com")

password = driver.find_element_by_id("password")
password.send_keys("Piyush@5807")
password.send_keys(Keys.ENTER)

time.sleep(5)
#
all_jobs = driver.find_elements_by_css_selector(".job-card-list__title")

for job in all_jobs:
    job.click()
    save = driver.find_element_by_css_selector(".jobs-save-button")
    save.click()

