from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')
driver.implicitly_wait(5)
sum1 = driver.find_element(By.ID, 'sum1')
sum2 = driver.find_element(By.ID, 'sum2')

sum1.send_keys(Keys.NUMPAD1, Keys.NUMPAD5)
sum2.send_keys(15)

btn = driver.find_element(By.CSS_SELECTOR, 'button[onclick="return total()"]')
btn.click()

