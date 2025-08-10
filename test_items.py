from time import sleep


def test_1(browser):
    link = f"http://selenium1py.pythonanywhere.com"
    browser.get(link)
    sleep(5)
