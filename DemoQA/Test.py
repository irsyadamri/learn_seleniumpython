from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#EXPLICITLY WAIT library
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException



#Karena Erorr selenium 4
# agar browser testnya tidak menutup sendiri dari sini<<
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
# agar browser testnya tidak menutup sendiri >>samapai sini


driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demoqa.com/alerts")
time.sleep(2)

# driver.find_element(By.XPATH, '//*[@id="alertButton"]').click()
# time.sleep(2)
# driver.switch_to.alert.accept()

# driver.find_element(By.XPATH, '//*[@id="confirmButton"]').click()
# time.sleep(2)
# driver.switch_to.alert.accept()

# driver.find_element(By.XPATH, '//*[@id="confirmButton"]').click()
# time.sleep(2)
# driver.switch_to.alert.dismiss()

# driver.find_element(By.XPATH, '//*[@id="promtButton"]').click()
# time.sleep(2)
# driver.switch_to.alert.send_keys("irsyad")
# time.sleep(2)
# driver.switch_to.alert.accept()

