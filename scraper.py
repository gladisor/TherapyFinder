from selenium import webdriver
from selenium.webdriver.chrome.options import Options

path = 'C:\Program Files (x86)\chromedriver.exe'

driver = webdriver.Chrome(path)

data = driver.get('https://www.psychologytoday.com/')
print(data)

driver.quit()
