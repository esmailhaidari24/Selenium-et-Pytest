
# condtional commands

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

driver.maximize_window()
time.sleep(2)



#is_displayed
#is_enabled
#is_selected

searchebox= driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
#is_displayed
print("displayed status: ", searchebox.is_displayed())  #true
#is_enabled
print('enabled status:', searchebox.is_enabled()) #true


#is_selected
ra_male= driver.find_element(By.XPATH,"//label[normalize-space()='Male']")
ra_famle= driver.find_element(By.XPATH,"//label[@for='gender-female']")




print(ra_male.is_selected())  #false
print(ra_famle.is_selected()) #false

print("après la selection du sexe: ")

ra_male.click()
print( ra_male.is_selected())  #true
print(ra_famle.is_selected()) #false

ra_famle.click()
print( ra_male.is_selected())  #false
print(ra_famle.is_selected()) #true   


elements= driver.find_elements(By.XPATH,"//div[@class='footer-upper']//a")
print(len(elements))
print(elements[0].text)
for element in elements:
    print(element.text)   
    

driver.find_element(By.LINK_TEXT,"Log in").click()
driver.close()