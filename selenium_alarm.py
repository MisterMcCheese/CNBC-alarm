from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import time
import schedule
import os
def  job():
    
    driver = webdriver.Firefox(executable_path= 'C:\\Users\\mcrou\\geckodriver.exe')

    driver.get('https://player.siriusxm.com/home/CNBC')
    #find login butoon
    time.sleep(5)
    signin = driver.find_element_by_css_selector('.sign-in-button')
    signin.click()
    time.sleep(1)
    username = driver.find_element_by_css_selector('input.ng-pristine:nth-child(1)')
    password = driver.find_element_by_css_selector('input.ng-pristine:nth-child(2)')

    username.send_keys('MCROUND94@GMAIL.COM')
    password.send_keys('')

    login_attempt = driver.find_element_by_css_selector('.login-button')

    login_attempt.click()
    time.sleep(7)
  #  login_button = driver.find_element_by_css_selector('.play-pause-btn')
  #  login_button.click()
    cnbc_button= driver.find_element_by_css_selector('#hero-carousel-0-p136-z1 > div:nth-child(1) > div:nth-child(1) > li:nth-child(1)')
    cnbc_button.click()
    #content-carousel-0 > div:nth-child(1) > div:nth-child(1) > li:nth-child(1) > channel-content-tile:nth-child(1) > div:nth-child(1) > div:nth-child(1) > tile-image:nth-child(2) > img:nth-child(1)
    #get program to open tws ahit have to input security code

    os.startfile('C:\\Jts\\tws.exe')
    

    #login SA openbinance
   # driver.get('

schedule.every().monday.at("07:00").do(job)
schedule.every().tuesday.at("06:28").do(job)
schedule.every().wednesday.at("07:00").do(job)
schedule.every().thursday.at("07:47").do(job)
schedule.every().friday.at("07:00").do(job)
schedule.every().saturday.at("06:00").do(job)
schedule.every().sunday.at("07:32").do(job)

while True:
        schedule.run_pending()
        time.sleep(1)


