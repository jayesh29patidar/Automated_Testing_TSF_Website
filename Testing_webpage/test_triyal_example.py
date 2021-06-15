from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get('https://mailchimp.com/')

login = driver.find_element_by_xpath('/html/body/header/nav/ul/li[2]/a')
login.click()

username = driver.find_element_by_id("username")
username.send_keys("Jayeshpatidar29")

passod = driver.find_element_by_id("password")
passod.send_keys('Annu@1234')


log_in = driver.find_element_by_xpath('//button[@class="button-large button-wide full-width p1 !margin-bottom--lv5"]')
log_in.click()
