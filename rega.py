from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

driver = webdriver.Chrome()

driver.get ("https://registrar.nu.edu.kz/user/login")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "edit-name"))
)

username = "YOUR_USERNAME"
password = "YOUR_PASSWORD"

input_element = driver.find_element(By.ID, "edit-name")
input_element.send_keys(username)

input_element = driver.find_element(By.ID, "edit-pass")
input_element.send_keys(password + Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.LINK_TEXT, "COURSE REGISTRATION"))
)
link = driver.find_element(By.LINK_TEXT, "COURSE REGISTRATION")
link.click()

time.sleep(2)

input_element = driver.find_element(By.ID, "titleText-inputEl")
input_element.send_keys("CSCI 490" + Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//table[@id='gridview-1025-table']//tbody/tr" ))
).click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "green-button"))
).click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "blue-button"))
).click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "course-cloud"))
).click()


time.sleep(30)
