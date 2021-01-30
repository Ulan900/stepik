from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_xpath('//input[@placeholder="Input your first name"]')
    input1.send_keys('Igor')

    input2 = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
    input2.send_keys('Ulanov')

    input3 = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')
    input3.send_keys('igorulan@gmail.com')

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1").text
    # записываем в переменную welcome_text текст из элемента welcome_text_elt

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert welcome_text_elt == "Congratulations! You have successfully registered!", "The text does not match"

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
