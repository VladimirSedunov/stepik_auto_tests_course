from time import sleep
import time
import math

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

import json

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sss = ''


@pytest.fixture(scope="session")
def load_config():
    with open('config.json') as config_file:
        config = json.load(config_file)
        return config


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()

    yield browser

    # print("\nquit browser..")
    # browser.quit()


@pytest.mark.parametrize('link',
                         [
                             "https://stepik.org/lesson/236895/step/1",
                             "https://stepik.org/lesson/236896/step/1",
                             "https://stepik.org/lesson/236897/step/1",
                             "https://stepik.org/lesson/236898/step/1",
                             "https://stepik.org/lesson/236899/step/1",
                             "https://stepik.org/lesson/236903/step/1",
                             "https://stepik.org/lesson/236904/step/1",
                             "https://stepik.org/lesson/236905/step/1",
                         ])
def test_authorization(browser, load_config, link):
    global sss
    print()
    login = load_config['login_stepik']
    password = load_config['password_stepik']

    browser.get(link)

    WebDriverWait(driver=browser, timeout=5).until(EC.element_to_be_clickable((By.ID, "ember479")))
    browser.find_element(By.CSS_SELECTOR, "#ember479").click()

    WebDriverWait(driver=browser, timeout=5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#id_login_email")))
    browser.find_element(By.CSS_SELECTOR, "#id_login_email").send_keys(login)
    browser.find_element(By.CSS_SELECTOR, "#id_login_password").send_keys(password)
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    sleep(2)

    try:
        WebDriverWait(driver=browser, timeout=5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".again-btn")))
        again = browser.find_element(By.CSS_SELECTOR, ".again-btn")
        again.click()
        sleep(2)
    except:
        print('0')
        pass

    try:
        WebDriverWait(driver=browser, timeout=2).until(EC.element_to_be_clickable(browser.find_element(By.CSS_SELECTOR, "textarea[placeholder='Напишите ваш ответ здесь...']")))
        browser.find_element(By.CSS_SELECTOR, "textarea[placeholder='Напишите ваш ответ здесь...']").click()
        browser.find_element(By.CSS_SELECTOR, "textarea[placeholder='Напишите ваш ответ здесь...']").clear()
        answer = str(math.log(int(time.time() + 0.095)))
        browser.find_element(By.CSS_SELECTOR, "textarea[placeholder='Напишите ваш ответ здесь...']").send_keys(answer)

        WebDriverWait(driver=browser, timeout=5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission")))
        browser.find_element(By.CSS_SELECTOR, ".submit-submission").click()
        sleep(2)
    except:
        print('1')
        pass

    try:
        text = browser.find_element(By.CSS_SELECTOR, 'p.smart-hints__hint').text
        print(text)
        if text == 'Correct!':
            pytest.fail('')
        else:
            sss += text
    except:
        print('2')
        pass

    print(f'{sss=}')
