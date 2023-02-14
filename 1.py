from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import *
from selenium.webdriver.support.ui import Select
import time
import random
import string
driver = webdriver.Chrome()

driver.maximize_window()  
driver.get("https://htmljstemplates.com/utilities/qr-ticket-generator") 
time.sleep(6)
driver.find_element("id","qrInput").send_keys("Hello")
dd= Select(driver.find_element("id","qrType"))
dd.select_by_value("event")


#Variables
eventName="Event"
logoURL ="C:\\Users\\SUBINOY\\OneDrive\\Pictures\\WhatsApp Image 2022-10-15 at 23.50.12.jpg" #In C:\\ABC\\ format
eventDetail ="In-Person Event"
eventLocation = "Location: " + "JIS College of Engineering, Kalyani, Nadia"
eventDate="March 8, 2023"


#Setup
name=driver.find_elements(By.CLASS_NAME, "h5")
name[0].clear()
name[0].send_keys(eventName)
image=driver.find_elements(By.ID,"uploadLogo")
image[0].send_keys(logoURL)
detail = driver.find_elements(By.CLASS_NAME, "smallFont")
detail[0].clear()
detail[0].send_keys(eventDetail)
date1 = driver.find_element(By.XPATH,"//*[text()=' 12th Dec 2022 - 22nd Dec 2022']")
date1.clear()
date1.send_keys(eventDate)
location1 = driver.find_element(By.XPATH,"//*[text()=' A Grand Hotel, Park Ave, Bridgeport, CT']")
location1.clear()
location1.send_keys(eventLocation)
element = driver.find_element(By.CLASS_NAME,'mx-3')
driver.execute_script("""
var element = arguments[0];
element.parentNode.removeChild(element);
""", element)
element = driver.find_element(By.CLASS_NAME,'mx-3')
driver.execute_script("""
var element = arguments[0];
element.parentNode.removeChild(element);
""", element)
element = driver.find_element(By.CLASS_NAME,'mx-3')
driver.execute_script("""
var element = arguments[0];
element.parentNode.removeChild(element);
""", element)


#def(nme):
#    res = ''.join(random.choices(string.ascii_uppercase +
#                             string.digits, k=N))
# 
#
#    print("The generated random string : " + str(res))
#    pasteid= nme+
time.sleep(100)  
