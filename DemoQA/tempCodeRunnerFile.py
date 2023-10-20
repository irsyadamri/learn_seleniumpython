driver.find_element(By.XPATH, '//*[@id="confirmButton"]').click()
time.sleep(2)
driver.switch_to.alert.accept()