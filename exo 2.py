
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time 
import pytest


# Configuration des options Chrome pour désactiver la popup de sélection du moteur de recherche
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")


# Initialiser le navigateur
driver = webdriver.Chrome(options=chrome_options)

# Ouvrir la page de test
driver.get("https://demoqa.com/text-box")


# Remplir les champs du formulaire

driver.find_element(By.ID, "userName").send_keys("John Doe")
time.sleep(2)
driver.find_element(By.ID, "userEmail").send_keys("john.doe@example.com")
time.sleep(2)
driver.find_element(By.ID, "currentAddress").send_keys("123 Rue de Paris")
time.sleep(2)
driver.find_element(By.ID, "permanentAddress").send_keys("456 Rue de Lyon")
time.sleep(2)

# Soumettre le formulaire
driver.find_element(By.ID, "submit").click()

# Vérifier les valeurs saisies
assert "John Doe" in driver.find_element(By.ID, "name").text
    
assert "john.doe@example.com" in driver.find_element(By.ID, "email").text

assert "123 Rue de Paris" in driver.find_element(By.ID, "output").text
assert "456 Rue de Lyon" in driver.find_element(By.ID, "output").text




# Fermer le navigateur
driver.quit()






