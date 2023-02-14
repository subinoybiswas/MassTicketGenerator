from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import random
import string
import os
import time
import csv
options = webdriver.ChromeOptions()

prefs={"download.default_directory":"C:\\Users\\SUBINOY\\OneDrive\\Documents\\Python-LAPTOP-2SS827IP\\Automation\\Tickets"}

options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(executable_path='./chromedriver',options=options)

driver.maximize_window()  
driver.get("https://htmljstemplates.com/utilities/qr-ticket-generator") 
time.sleep(6)
qr= driver.find_element("id","qrInput")
qr.send_keys("Hello")
dd= Select(driver.find_element("id","qrType"))
dd.select_by_value("event")


#Variables
eventName="ABC Competetion"
logoURL ="C:\\Users\\SUBINOY\\OneDrive\\Documents\\Python-LAPTOP-2SS827IP\\Automation\\logo.png"
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
changeforname=driver.find_element(By.XPATH,"//*[text()='Admit 1']")
changeforrandom =driver.find_element(By.XPATH,"//*[text()='1AD3434']")
#downloadbutton=driver.find_element(By.XPATH,"//*[text()='Donwload Ticket']")
downloadbutton=driver.find_element(By.CLASS_NAME,'col-md-6')
Initial_path= "C:\\Users\\SUBINOY\\OneDrive\\Documents\\Python-LAPTOP-2SS827IP\\Automation\\Tickets"
def tiny_file_rename(newname, folder_of_download):
    filename = max([f for f in os.listdir(folder_of_download)], key=lambda xa :   os.path.getctime(os.path.join(folder_of_download,xa)))
    if '.part' in filename:
        time.sleep(1)
        os.rename(os.path.join(folder_of_download, filename), os.path.join(folder_of_download, newname+".png"))
    else:
        os.rename(os.path.join(folder_of_download, filename),os.path.join(folder_of_download,newname+".png"))
def qrid(nme):
    res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=7))
    pasteid = nme + res
    print(res)
    qr.clear()
    qr.send_keys(pasteid)
    time.sleep(1)
    qr.send_keys(Keys.ENTER)
    time.sleep(2)
    changeforname.clear()
    changeforname.send_keys(nme)
    changeforrandom.clear()
    changeforrandom.send_keys(res)
    time.sleep(2)
    try:
        element = WebDriverWait(driver, 50).until(
        EC.element_to_be_clickable(downloadbutton))
        time.sleep(2)
        element.click()
        time.sleep(1)
        tiny_file_rename(pasteid,Initial_path)
    except:
        time.sleep(3)
        downloadbutton.click()
        time.sleep(1)
        tiny_file_rename(pasteid,Initial_path)
        #element = WebDriverWait(driver, 20).until(
        #EC.element_to_be_clickable(downloadbutton))
        #time.sleep(3)
        #element.click()
        #time.sleep(1)
        #tiny_file_rename(pasteid,Initial_path)
with open('C:\\Users\\SUBINOY\\OneDrive\\Documents\\abcde.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for lims in spamreader:
        qrid(lims[0])
#o = ["Subi","AB"]
#for pm in o:
 #   qrid(pm)


time.sleep(100)  
