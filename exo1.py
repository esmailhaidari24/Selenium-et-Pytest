from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Configuration des options Chrome pour désactiver la popup de sélection du moteur de recherche
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")


#chrome_options.add_argument("--disable-popup-blocking")# pour bloquer les popups


import time
# Initialiser le navigateur
driver = webdriver.Chrome(options=chrome_options)

# Ouvrir la page de test
driver.get("https://demoqa.com/text-box")

# Remplir les champs du formulaire
driver.find_element(By.ID, "userName").send_keys("John Doe")
time.sleep(3)
driver.find_element(By.ID, "userEmail").send_keys("john.doe@example.com")
time.sleep(3)
driver.find_element(By.ID, "currentAddress").send_keys("123 Rue de Paris")
time.sleep(3)
driver.find_element(By.ID, "permanentAddress").send_keys("456 Rue de Lyon")
time.sleep(3)

# Soumettre le formulaire
driver.find_element(By.ID, "submit").click()

time.sleep(10)
# Fermer le navigateur

driver.quit()



