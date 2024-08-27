
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


# Configuration des options Chrome pour désactiver la popup de sélection du moteur de recherche
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

#chrome_options.add_argument("--disable-popup-blocking")# pour bloquer les popups
# Initialiser le navigateur

driver = webdriver.Chrome(options=chrome_options)

driver.get ("https://demoqa.com/text-box")

#remplir les champs du formulaire

driver.find_element(By.ID, "userName").send_keys("esmail")
time.sleep(1)

time.sleep(1)
driver.find_element(By.ID, "userEmail").send_keys("esmailhaidari24@gmail.fr")
time.sleep(1)
driver.find_element(By.ID, "currentAddress").send_keys("villeurbanne")
time.sleep(1)
driver.find_element(By.ID, "permanentAddress").send_keys("permanentAddress")
time.sleep(1)

submit_button = driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)

driver.find_element(By.ID, "submit").click()
time.sleep(4)

print("page chargee")
