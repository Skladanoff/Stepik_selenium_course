from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("input_value").text
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    cbx = browser.find_element_by_id("robotCheckbox")
    cbx.click()
    radio = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()
    btn = browser.find_element_by_class_name("btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", btn)
    btn.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


