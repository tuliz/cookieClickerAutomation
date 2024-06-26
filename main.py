from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://orteil.dashnet.org/experiments/cookie/')

# Get the cookie element
cookie = driver.find_element(By.ID, 'cookie')
# Get the products in store and their prices

# Set up timers for the store purchase and for the loop
timer = time.time() + 8
five_minutes = time.time() + 60*5
# Keep The Clicks With a While loop
while True:

    cookie.click()

    # Get the current number of cookies
    number_cookies = driver.find_element(By.ID, 'money').text
    cookies = int(number_cookies.replace(',','')) if ',' in number_cookies else int(number_cookies)
    # Check if timer is up
    if time.time() > timer:
        store_prices = driver.find_elements(By.CSS_SELECTOR, '#store b')
        # Check if the current cookies are enough to buy an upgrade
        for n in range(len(store_prices)-2,-1,-1):
            price = int(store_prices[n].text.split(' ')[3 if n == 5 or n == 7 else 2].replace(',',''))
            if cookies > price:
                store_prices[n].click()
                break
        # Restart Five Seconds timer
        timer = time.time() + 8

    # Check if 5 minutes are passed, if True get the current cookies per seconds and escape from the loop
    if time.time() > five_minutes:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break

