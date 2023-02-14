from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import *
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome()

driver.maximize_window()  
driver.get("https://htmljstemplates.com/utilities/qr-ticket-generator") 
driver.find_element("id","qrInput").send_keys("Hello")
dd= Select(driver.find_element("id","qrType"))
dd.select_by_value("event")
#n1= driver.find_element("xpath","//*[contains(@text='National Conference | Climate Change')]")
eventName="Event"
logoURL ="C:\\Users\\SUBINOY\\OneDrive\\Pictures\\WhatsApp Image 2022-10-15 at 23.50.12.jpg" #In C:\\ABC\\ format
eventDetail ="In-Person Event"
name=driver.find_elements(By.CLASS_NAME, "h5")
time.sleep(6)
name[0].clear()
name[0].send_keys(eventName)
image=driver.find_elements(By.ID,"uploadLogo")

#image[0].click()
image[0].send_keys(logoURL)
detail = driver.find_elements(By.CLASS_NAME, "smallFont")
detail[0].clear()
detail[0].send_keys(eventDetail)
date1 = driver.find_element(By.XPATH,"//*[text()=' 12th Dec 2022 - 22nd Dec 2022']")
date1.clear()
date1.send_keys("1234")

location1 = driver.find_element(By.XPATH,"//*[text()=' A Grand Hotel, Park Ave, Bridgeport, CT']")
location1.clear()
location1.send_keys("<strong>HDBADF</strong>")
time.sleep(100)  