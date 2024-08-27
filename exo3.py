from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Configuration des options Chrome pour désactiver la popup de sélection du moteur de recherche
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

# Ouverture de la fenêtre du navigateur avec les options configurées
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://demoqa.com/radio-button") 
 
#driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div/div[2]/div[2]/div[2]/label').click()
#time.sleep(4)

driver.find_element(By.XPATH,"//label[@for='yesRadio']").click()

driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/label').click()
time.sleep(4)

driver.close()

#  la soultion donné par tom
"""
element = driver.find_element(By.CSS_SELECTOR, ".col-12.mt-4.col-md-6")
listYesAndNo = element.find_elements(By.CSS_SELECTOR, ".custom-control.custom-radio.custom-control-inline")
for YesOrNo in listYesAndNo:
    driver.execute_script("arguments[0].scrollIntoView();", YesOrNo)
    time.sleep(1)
    if YesOrNo.text == "Yes":
        YesOrNo.find_element(By.TAG_NAME, "label").click()
        assert "Yes" in driver.find_element(By.CLASS_NAME, "text-success").text
    if YesOrNo.text == "Impressive":
        YesOrNo.find_element(By.TAG_NAME, "label").click()
        assert "Impressive" in driver.find_element(By.CLASS_NAME, "text-success").text
    time.sleep(1)
time.sleep(1)

"""