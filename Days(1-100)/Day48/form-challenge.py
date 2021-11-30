from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "D:\Desktop\Web Development\chromedriver_win32\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element_by_name("fName")
lname = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")
button = driver.find_element_by_css_selector("button")

fname.send_keys("skjbcjb")
lname.send_keys("sjkbsmcn")
email.send_keys("sjkxcbjfddsa@gmail.com")
button.click()


