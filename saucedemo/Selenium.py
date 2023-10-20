from selenium import webdriver
from selenium.webdriver.common.by import By



#Karena Erorr selenium 4
# agar browser testnya tidak menutup sendiri dari sini<<
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
# agar browser testnya tidak menutup sendiri >>samapai sini


driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.saucedemo.com/v1/")

#Login
driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
driver.find_element(By.XPATH, '//*[@id="inventory_filter_container"]/div')
