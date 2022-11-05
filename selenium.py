import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# For one element

driver = webdriver.Chrome(executable_path="chromedriver.exe")

driver.get("https://shop.labourseauxlivres.fr/")

search_bar = driver.find_element(By.CLASS_NAME, "search-bar__input")

search_bar.send_keys("Les justes Camus")

find_button = driver.find_element(By.CLASS_NAME, "search-bar__submit")
find_button.click()

product_link = driver.find_element(By.CLASS_NAME, "product-item__info-inner")
product_link.click()

add_to_cart = driver.find_element(By.CSS_SELECTOR, ".product-form__add-button.button.button--primary")
add_to_cart.click()

# For a list of element

for i in list_of_books:
    search_bar = driver.find_element(By.CLASS_NAME, "search-bar__input")
    search_bar.send_keys(i)
    find_button = driver.find_element(By.CLASS_NAME, "search-bar__submit")
    find_button.click()
    product_link = driver.find_element(By.CLASS_NAME, "product-item__info-inner")
    product_link.click()
    product_link_2 = driver.find_element(By.CSS_SELECTOR, ".product-form__add-button.button.button--primary")
    product_link_2.click()
