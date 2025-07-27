from selenium import webdriver
from selenium.webdriver.common.by import By

from capcha import pass_captcha, submit_and_exit

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/cats.html")

browser.find_element(value="button")

browser.quit()
