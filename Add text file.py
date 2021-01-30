import os
from selenium import webdriver
import time



link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
browser.get(link)

a = browser.find_element_by_css_selector("[name='firstname']").send_keys('Igor')
time.sleep(1)
b = browser.find_element_by_css_selector("[name='lastname']").send_keys('Ulanov')
time.sleep(1)
c = browser.find_element_by_css_selector("[name='email']").send_keys('igor@igor.ru')



current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "123.txt"
g = os.path.join(current_dir, "123.txt")

element = browser.find_element_by_css_selector("[type='file']")
element.send_keys(g)


f = browser.find_element_by_tag_name('button').click()
time.sleep(1)
browser.quit()