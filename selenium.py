#for installing : pip install selenium
from selenium import webdriver
import time 

driver_path="C:\Users\user\Downloads\chromedriver_win32" #webdriver chrome
driver=webdriver.Chrome(driver_path)
driver.get("https://tcmb.gov.tr/") #going to website
print("WEBSITE TITLE:",driver.title())
driver.refresh()
driver.maximize.window() #full screen

#click to "Bugun" button on website
conventer_page=driver.find_element_by_xpath('//*[@id="tcmbMainContent"]/section[3]/div/div[3]/a[1]').click()
time.sleep(3) #waiting


exchange_name=driver.find_element_by_xpath('//*[@id="kurlarContainer"]/table[1]/tbody/tr[1]/td[3]').text

exchange=driver.find_element_by_xpath('//*[@id="kurlarContainer"]/table[1]/tbody/tr[1]/td[5]').text

USD=float(exchange.replace(',','.'))

print(f'{exchange_name}=>{USD}')


time.sleep(3)
driver.quit()