from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/selects2.html'

o = browser.get(link)
x = browser.find_element_by_id('num1').text
y = browser.find_element_by_id('num2').text
c = (str(int(x) + int(y)))


a = Select(browser.find_element_by_tag_name("select"))
a.select_by_value(c)
time.sleep(2)


k = browser.find_element_by_tag_name('button').click()
time.sleep(2)

browser.quit()