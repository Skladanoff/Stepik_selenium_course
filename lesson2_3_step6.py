from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element_by_class_name("trollface")
    button1.click()

    browser.switch_to.window(browser.window_handles[1])

    x = browser.find_element_by_id("input_value").text
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    button2 = browser.find_element_by_class_name("btn")
    button2.click()



finally:
    time.sleep(30)
    browser.quit()
