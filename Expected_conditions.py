from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
from math import log, sin
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/explicit_wait2.html'
browser.get(link)

button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))

a = browser.find_element_by_id('book').click()

b = browser.find_element_by_id('input_value').text
c = calc(b)
d = browser.find_element_by_id('answer').send_keys(c)

e = browser.find_element_by_id('solve').click()
browser.quit()
