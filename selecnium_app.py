from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

options=Options()
options.chrome_executable_path="C:\\Users\\User.DESKTOP-PEUUQC0\\Desktop\\WeHelp\\tiktok_selenium\\chromedriver.exe"

driver=webdriver.Chrome(options=options)
driver.get("https://www.tiktok.com/@geevideo")
sleep(10)
link = driver.find_elements(By.LINK_TEXT, "不登入繼續")
tags = driver.find_elements(By.CLASS_NAME, "captcha_verify_bar--title")
print(link)
driver.close()