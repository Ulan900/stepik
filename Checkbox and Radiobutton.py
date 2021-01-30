from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# заходим на сайт
link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)
time.sleep(1)

# ищем значение x > записываем его в формате текст в переменную x > считаем значение и записываем в переменную y
x_element = browser.find_element_by_css_selector("#input_value")
x = x_element.text
y = calc(x)
time.sleep(1)

# находим input поле > вводим посчитанное раннее значение из переменной y
answer = browser.find_element_by_css_selector("#answer")
answer.send_keys(y)
time.sleep(1)

# находим чекбокс и выбираем его
checkbox = browser.find_element_by_css_selector("#robotCheckbox").click()
time.sleep(1)

# находим радиобаттон и нажимаеи на него
radiobutton = browser.find_element_by_css_selector("#robotsRule").click()
time.sleep(1)

# ищем кнопку сабмит и нажимаем на нее
search = browser.find_element_by_css_selector("[type='submit']").click()