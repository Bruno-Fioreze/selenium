from  selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


browser = Chrome()

browser.get("http://127.0.0.1:5500/")
browser.implicitly_wait(3)
browser.maximize_window()
#browser.find_element_by_id("btn").click().sendKey("/home/bruno/Área de Trabalho/selenium/text.txt");
elemento = browser.find_element(By.XPATH, "//*[@id='arquivo']")
elemento.send_keys("/home/bruno/Área de Trabalho/selenium/text.txt")
browser.implicitly_wait(3)
btn = browser.find_element(By.XPATH, '//*[@id="arquivo"]')

browser.quit()