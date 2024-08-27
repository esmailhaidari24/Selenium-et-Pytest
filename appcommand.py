
#application commands

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


# Configuration des options Chrome pour désactiver la popup de sélection du moteur de recherche
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

# Initialiser le navigateur

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://demoqa.com/text-box")

driver.maximize_window()


#driver.get
#driver.title
#driver .current_url
#driver.page_source

 
print(driver.title)
time.sleep(2)

print(driver.current_url)

print(driver.page_source)

driver.quit()


