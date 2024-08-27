from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time 
import pytest


# Configuration des options Chrome pour désactiver la popup de sélection du moteur de recherche
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")
chrome_options.add_argument("--disable-extensions")

# Initialiser le navigateur
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://money.rediff.com/gainers")

driver.maximize_window()

#self

#text_message = driver.find_element(By.XPATH, "//a[normalize-space()='Oriental Trimex']/self::a").text
#print(text_message)
#time.sleep(4)


#prent
#text_message = driver.find_element(By.XPATH, "//a[normalize-space()='Oriental Trimex']/parent::td").text
#print(text_message)

#child

#childs = driver.find_elements(By.XPATH, "//a[normalize-space()='Oriental Trimex']/ancestor::tr/child::td ")
#print(len(childs))
#print(childs)

#driver.quit()

#ancestor
"""
text_message = driver.find_element(By.XPATH, "//a[normalize-space()='Oriental Trimex']/ancestor::tr").text
print(text_message)
time.sleep(4)
driver.quit()
"""

#descendant
"""
descendants = driver.find_elements(By.XPATH, "//a[normalize-space()='Oriental Trimex']/ancestor::tr/descendant:: *")
print("number of descendent", len(descendants))

time.sleep(4)
driver.quit()
"""

#following

followings = driver.find_elements(By.XPATH, "//a[normalize-space()='Oriental Trimex']/ancestor::tr/following:: *")
print("number of following: ", len(followings))

time.sleep(4)
driver.quit()
