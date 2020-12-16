from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time
from random import randint

firefox_options = Options()
firefox_options.add_argument('--dns-prefetch-disable')
firefox_options.add_argument('--no-sandbox')
firefox_options.add_argument('--lang=en-US')
global browser
browser = webdriver.Firefox() 

browser.get("https://sw.wikipedia.org/wiki/Mwanzo") 

browser.find_element_by_id("pt-login").click()

jina="UmojaWetu"
siri="agmen130498"

mtumiaji = browser.find_element_by_id("wpName1")
mtumiaji.send_keys(jina)    
mtumiaji.send_keys(Keys.TAB)

nenolasiri = browser.find_element_by_id("wpPassword1")
nenolasiri.send_keys(siri)    
nenolasiri.send_keys(Keys.TAB)

browser.find_element_by_id("wpLoginAttempt").click()

newpage = input("Kichwa cha makala: ")

tafuta = browser.find_element_by_id("searchInput")
tafuta.send_keys(newpage)    
tafuta.send_keys(Keys.RETURN)

time.sleep(10)

browser.find_element_by_xpath('//a[@class="new"]').click()

time.sleep(10)

"""browser.find_element_by_xpath('//span[@class="oo-ui-popupToolGroup-handle"]').click()

browser.find_element_by_xpath('//span[@class="oo-ui-widget oo-ui-iconElement oo-ui-tool-with-icon oo-ui-tool oo-ui-tool-name-categories oo-ui-widget-enabled"]').click()

time.sleep(5)

jamii1 = input("Jamii1: ")
jamii2 = input("Jamii2: ")
jamii3 = input("Jamii3: ")

link1 = browser.find_element_by_xpath('//input[@placeholder="Ongeza jamii"]')
link1.send_keys(jamii1)    
link1.send_keys(Keys.RETURN)

time.sleep(10)

link2 = browser.find_element_by_xpath('//input[@placeholder="Ongeza jamii"]')
link2.send_keys(jamii2)    
link2.send_keys(Keys.RETURN)

time.sleep(10)

link3 = browser.find_element_by_xpath('//input[@placeholder="Ongeza jamii"]')
link3.send_keys(jamii3)    
link3.send_keys(Keys.RETURN)

browser.find_element_by_xpath('//a[@class="oo-ui-buttonElement-button"]').click()"""

#write makala

browser.find_element_by_xpath('//a[@title="Unaweza kuhariri ukurasa huu.  Tafadhali tumia kitufe cha kuhakikisha kabla ya kuhifadhi."]').click()

f = open('Makala.txt', 'r')
content = f.read()

time.sleep(10)

browser.find_element_by_id("wpTextbox1").send_keys(content)

f.close()

browser.find_element_by_id("wpSave").click()

print("makala imechapishwa")