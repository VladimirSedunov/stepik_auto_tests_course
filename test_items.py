from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_check_add_button_for_coders_at_work(browser):
    link = f"http://selenium1py.pythonanywhere.com"
    browser.get(link)

    css_menu = ".dropdown-menu a[href$='/catalogue/']"
    WebDriverWait(driver=browser, timeout=5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_menu)))
    browser.find_element(By.CSS_SELECTOR, css_menu).click()


    # css_book = "article.product_pod a[href$='/catalogue/coders-at-work 207/']"
    css_book = "[title='Coders at Work']"
    WebDriverWait(driver=browser, timeout=5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_book)))
    browser.find_element(By.CSS_SELECTOR, css_book).click()

    css_add = ".btn-add-to-basket"
    WebDriverWait(driver=browser, timeout=5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_add)))
    # WebDriverWait(driver=browser, timeout=5).until(EC._element_if_visible((By.CSS_SELECTOR, css_add)))
    assert len(browser.find_elements(By.CSS_SELECTOR, css_add)) == 1
    assert EC._element_if_visible(browser.find_element(By.CSS_SELECTOR, css_add))

    sleep(5)
