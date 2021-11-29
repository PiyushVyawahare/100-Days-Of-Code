import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

URL = "https://www.amazon.in/Infinity-Glide-120-Earphones-Sweatproof/dp/B082MDMW3X/ref=sr_1_1?crid=34LCUQ6QI546&keywords=infinity%2Bglide%2Bn120&qid=1638185602&qsid=257-8798619-9193024&smid=A14CZOWI0VEHLG&sprefix=infinity%2Bglide%2B%2Caps%2C350&sr=8-1&sres=B082MDMW3X%2CB08LB9Q73J%2CB08L9HZNC5%2CB07WCTP58X%2CB084C1Y3N9%2CB0863YHJXZ%2CB07Z64K19G%2CB096KX4X7D%2CB08LDLZBW8%2CB07ZC6DJ2G%2CB096BJ1H47%2CB096BKQM3S%2CB083V2SSQ6%2CB07W7RSYTX%2CB08Y6XTHM2%2CB07Q743T4F&srpt=HEADPHONES&th=1"
MY_EMAIL = "piyushvyawahare2021@gmail.com"
MY_PASSWORD = "Piyush@5807"

browser_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(URL, headers=browser_headers)
website_html = response.text

soup = BeautifulSoup(website_html, "lxml")
price = soup.find(name="span", id="priceblock_dealprice",
                  class_="a-size-medium a-color-price priceBlockDealPriceString").getText()
price_without_currency = price.split("₹")[1]
price_without_separator = price_without_currency.split(",")
price_without_separator = "".join(price_without_separator)
price_as_float = float(price_without_separator)

target_price = 700.00

product_name = soup.find(name="span", id="productTitle").getText().strip()

if price_as_float < target_price:

    message = f"{product_name} is now at {price_as_float}\n Here is the link - {URL}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="piyushvyawahare2001@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}"
        )
