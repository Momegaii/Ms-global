from selenium import webdriver
from selenium.webdriver.service import Service

service = Service('C:\Users\Moha\Desktop\chromedriver.exe')

#service.start() to check on th files storted in service

driver = webdriver.Chrome(service=service)
driver.get('https://www.google.com/')
