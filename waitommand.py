from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest
import time

# Configuration des options Chrome pour désactiver la popup de sélection du moteur de recherche
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

# Initialiser le navigateur
driver = webdriver.Chrome(options=chrome_options)

# Ouvrir Google
driver.get("https://www.google.com/")

driver.implicitly_wait(10)  # Attendre 10 secondes avant de fermer le navigateur pour voir le résultat

# Pause pour permettre le chargement de la page
time.sleep(2)

# Tenter de cliquer sur le bouton "Tout accepter"
try:
    accept_button = driver.find_element(By.XPATH, "//button[contains(., 'Tout accepter')]")
    accept_button.click()
    print("Bouton 'Tout accepter' cliqué.")
except:
    print("Bouton 'Tout accepter' non trouvé, continuons.")

# Tenter de cliquer sur le bouton "Tout refuser" (au cas où)
try:
    refuse_button = driver.find_element(By.XPATH, "//button[contains(., 'Tout refuser')]")
    refuse_button.click()
    print("Bouton 'Tout refuser' cliqué.")
except:
    print("Bouton 'Tout refuser' non trouvé, continuons.")

# Maximiser la fenêtre du navigateur
driver.maximize_window()

# Attendre quelques secondes avant de fermer le navigateur pour voir le résultat


button= driver.find_element(By.XPATH,"//textarea[@id='APjFqb']")
button.send_keys("selenium")
button.submit()

driver.find_element(By.XPATH,'//*[@id="rso"]/div[8]/div/div/div[1]/div/div/span/a/h3').click()

driver.quit()