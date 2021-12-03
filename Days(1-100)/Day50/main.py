import time

from selenium import webdriver

chrome_driver_path = "D:\Desktop\Web Development\chromedriver_win32\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://tinder.com/")
time.sleep(2)
log_in = driver.find_element_by_link_text("Log in")
log_in.click()
time.sleep(2)

fb_login = driver.find_element_by_xpath('//*[@id="q36386411"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()

time.sleep(2)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]

driver.switch_to.window(fb_login_window)

email = driver.find_element_by_name("email")
email.send_keys("piyushvyawahare2021@gmail.com")

password = driver.find_element_by_name("pass")
password.send_keys("Pbv@5807")

login = driver.find_element_by_name("login")
login.click()

time.sleep(2)
driver.switch_to.window(base_window)

time.sleep(2)
cookie = driver.find_element_by_xpath('//*[@id="q-184954025"]/div/div[2]/div/div/div[1]/button')
cookie.click()

time.sleep(5)
location = driver.find_element_by_xpath('//*[@id="q36386411"]/div/div/div/div/div[3]/button[1]')
location.click()

time.sleep(2)
notification = driver.find_element_by_xpath('//*[@id="q36386411"]/div/div/div/div/div[3]/button[2]')
notification.click()

time.sleep(10)
for _ in range(100):
    time.sleep(2)
    try:
        dismiss = driver.find_element_by_xpath(
            '//*[@id="q-184954025"]/div/div[1]/div/div/main/div/div[1]/div[1]/div/div[4]/div/div[2]/button')
        dismiss.click()

    except:
        time.sleep(2)


driver.quit()
