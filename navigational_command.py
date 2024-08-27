
# Navigation commands


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


# Configuration des options Chrome pour désactiver la popup de sélection du moteur de recherche
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

# Initialiser le navigateur

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://demo.nopcommerce.com/register")
driver.get("https://demoqa.com/text-box")


#back
#forward
#refresh

driver.back() #retourne à la page précédente
driver.forward() #retourne à la page suivante
driver.refresh() #actualise la page
time.sleep(2)

driver.quit()