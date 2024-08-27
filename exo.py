
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



# ouverture de la fenêtre du navigateur
driver = webdriver.Chrome()
driver.get("http://www.python.org")
print("page chargée")
time.sleep(10)

# fermeture de la fenêtre du navigateur
driver.quit()