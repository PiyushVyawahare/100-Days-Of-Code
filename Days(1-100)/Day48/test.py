from selenium import webdriver

driver = webdriver.Chrome(executable_path='./chromedriver.exe')

driver.get("https://www.amazon.in/Infinity-Glide-120-Earphones-Sweatproof/dp/B082MDMW3X/ref=sr_1_1?crid=34LCUQ6QI546&keywords=infinity%2Bglide%2Bn120&qid=1638185602&qsid=257-8798619-9193024&smid=A14CZOWI0VEHLG&sprefix=infinity%2Bglide%2B%2Caps%2C350&sr=8-1&sres=B082MDMW3X%2CB08LB9Q73J%2CB08L9HZNC5%2CB07WCTP58X%2CB084C1Y3N9%2CB0863YHJXZ%2CB07Z64K19G%2CB096KX4X7D%2CB08LDLZBW8%2CB07ZC6DJ2G%2CB096BJ1H47%2CB096BKQM3S%2CB083V2SSQ6%2CB07W7RSYTX%2CB08Y6XTHM2%2CB07Q743T4F&srpt=HEADPHONES&th=1")
price = driver.find_element_by_id("priceblock_ourprice")
print(price.text)
driver.close()