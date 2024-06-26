from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://orteil.dashnet.org/cookieclicker/')

#Wait for the page to load and then choose language
driver.implicitly_wait(10)
english = driver.find_element(By.ID, 'langSelect-EN')
english.click()

# Wait for another load after choosing language and for game to load and show cookie
driver.implicitly_wait(10)
# Get the cookie element
big_cookie = driver.find_element(By.ID, 'bigCookie')
# Get the products in store and their prices
cursor = driver.find_element(By.ID, 'product0')
cursor_price = int(driver.find_element(By.ID, 'productPrice0').text)
store = [{'product':cursor, 'price':cursor_price}]

# Keep The Clicks With a While loop
while True:
    big_cookie.click()
    # Get the current number of cookies
    number_cookies = int(driver.find_element(By.ID, 'cookies').text.split(' ')[0])

    # Check if the current cookies are enough to buy an upgrade
    for product in store:
        if number_cookies > product['price']:
            product['product'].click()