import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from capcha import pass_captcha, submit_and_exit


def cost(s):
    return 0 if s.strip() == '' else int(s)


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# button = WebDriverWait(driver=browser, timeout=20).until(
#     lambda x: 99 < cost(str(x.find_element(value="price").text).replace('$', '')) <= 100)

is_100 = WebDriverWait(driver=browser, timeout=15).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))

browser.find_element(value='book').click()

pass_captcha(browser)
submit_and_exit(browser)

browser.quit()
