from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    img = browser.find_element_by_tag_name("img")
    x = img.get_attribute("valuex")

    y = calc(x)

    input = browser.find_element_by_id("answer")
    input.send_keys(y)
    cbx = browser.find_element_by_id("robotCheckbox")
    cbx.click()
    radio = browser.find_element_by_id("robotsRule")
    radio.click()
    btn = browser.find_element_by_class_name("btn")
    btn.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


