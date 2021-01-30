from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/get_attribute.html"
browser.get(link)
time.sleep(1)

# Находим картинку по id и находим, далее находим атрибут этого элемента
a = browser.find_element_by_id('treasure')
b = a.get_attribute('valuex')

# Вводим переменную чтобы посчитать уровнение
y = calc(b)

# Находим инпут поле и вводим ответ
answer = browser.find_element_by_css_selector("#answer")
time.sleep(1)
answer.send_keys(y)
time.sleep(1)

# Ставим чекбокс
checkbox = browser.find_element_by_css_selector("#robotCheckbox").click()
time.sleep(1)

# Ставим радиобаттон
radiobutton = browser.find_element_by_css_selector("#robotsRule").click()
time.sleep(1)

# Ищем кнопку сабмит и нажимаем на нее
search = browser.find_element_by_css_selector("[type='submit']").click()

# Закрываем браузер
time.sleep(3)
browser.quit()