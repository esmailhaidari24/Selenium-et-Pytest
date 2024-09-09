import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestDefaultSuite():
    def setup_method(self, method):
        # Configuration des options Chrome pour bloquer les publicités et les pop-ups
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--incognito")
        
        # Initialisation du driver avec les options configurées
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def close_popups(self):
        try:
            # Attendre et fermer toute publicité pop-up qui apparaît
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".close-button"))
            ).click()
        except Exception as e:
            print(f"Erreur lors de la fermeture des pop-ups : {e}")

    def scroll_to_element(self, element):
        # Faire défiler l'élément dans la vue au centre de l'écran
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", element)

    def test_testexo1(self):
        self.driver.get("https://demoqa.com/text-box")
        self.close_popups()  # Fermer les pop-ups
        
        self.driver.implicitly_wait(10)  # Attendre 10 secondes avant de fermer le navigateur pour voir le résultat

        user_name = self.driver.find_element(By.ID, "userName")
        self.scroll_to_element(user_name)  # Faire défiler jusqu'à l'élément
        user_name.click()
        user_name.send_keys("esmail")

        user_email = self.driver.find_element(By.ID, "userEmail")
        self.scroll_to_element(user_email)  # Faire défiler jusqu'à l'élément
        user_email.send_keys("esmail@gmail.fr")

        current_address = self.driver.find_element(By.ID, "currentAddress")
        self.scroll_to_element(current_address)  # Faire défiler jusqu'à l'élément
        current_address.click()
        current_address.send_keys("lyon")

        permanent_address = self.driver.find_element(By.ID, "permanentAddress")
        self.scroll_to_element(permanent_address)  # Faire défiler jusqu'à l'élément
        permanent_address.click()
        permanent_address.send_keys("lyon, villeurbanne ")

        submit_button = self.driver.find_element(By.ID, "submit")
        self.scroll_to_element(submit_button)  # Faire défiler jusqu'à l'élément
        submit_button.click()

    def test_testexo2(self):
        self.driver.get("https://demoqa.com/checkbox")
        self.close_popups()  # Fermer les pop-ups éventuels
    
        expand_icon = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".rct-icon-expand-close > path"))
        )
        expand_icon.click()
        
        expand_all_icon = self.driver.find_element(By.CSS_SELECTOR, ".rct-icon-expand-all")
        self.scroll_to_element(expand_all_icon)  # Faire défiler jusqu'à l'élément
        expand_all_icon.click()

        node_icon = self.driver.find_element(By.CSS_SELECTOR, "#tree-node > ol > .rct-node > .rct-text .rct-node-icon > .rct-icon")
        self.scroll_to_element(node_icon)  # Faire défiler jusqu'à l'élément
        node_icon.click()

    def test_test41(self):
        self.driver.get("https://demoqa.com/webtables")
        self.close_popups()  # Fermer les pop-ups

        add_new_record_button = self.driver.find_element(By.ID, "addNewRecordButton")
        self.scroll_to_element(add_new_record_button)  # Faire défiler jusqu'à l'élément
        add_new_record_button.click()

        first_name = self.driver.find_element(By.ID, "firstName")
        self.scroll_to_element(first_name)  # Faire défiler jusqu'à l'élément
        first_name.click()
        first_name.send_keys("max")

        last_name = self.driver.find_element(By.ID, "lastName")
        self.scroll_to_element(last_name)  # Faire défiler jusqu'à l'élément
        last_name.click()
        last_name.send_keys("maxi")

        user_email = self.driver.find_element(By.ID, "userEmail")
        self.scroll_to_element(user_email)  # Faire défiler jusqu'à l'élément
        user_email.click()
        user_email.send_keys("max@gmail.com")

        age = self.driver.find_element(By.ID, "age")
        self.scroll_to_element(age)  # Faire défiler jusqu'à l'élément
        age.click()
        age.send_keys("23")

        salary = self.driver.find_element(By.ID, "salary")
        self.scroll_to_element(salary)  # Faire défiler jusqu'à l'élément
        salary.click()
        salary.send_keys("3344")

        department = self.driver.find_element(By.ID, "department")
        self.scroll_to_element(department)  # Faire défiler jusqu'à l'élément
        department.click()
        department.send_keys("rhon")

        submit_button = self.driver.find_element(By.ID, "submit")
        self.scroll_to_element(submit_button)  # Faire défiler jusqu'à l'élément
        submit_button.click()

    def test_testexo3(self):
        self.driver.get("https://demoqa.com/radio-button")
        self.close_popups()  # Fermer les pop-ups

        radio_option = self.driver.find_element(By.CSS_SELECTOR, ".custom-control:nth-child(2) > .custom-control-label")
        self.scroll_to_element(radio_option)  # Faire défiler jusqu'à l'élément
        radio_option.click()

        result_text = self.driver.find_element(By.CSS_SELECTOR, ".text-success")
        self.scroll_to_element(result_text)  # Faire défiler jusqu'à l'élément
        result_text.click()

    def test_testexo42(self):
        self.driver.get("https://demoqa.com/webtables")
        self.close_popups()  # Fermer les pop-ups

        edit_icon = self.driver.find_element(By.CSS_SELECTOR, "#edit-record-1 path")
        self.scroll_to_element(edit_icon)  # Faire défiler jusqu'à l'élément
        edit_icon.click()

        first_name_wrapper = self.driver.find_element(By.ID, "firstName-wrapper")
        self.scroll_to_element(first_name_wrapper)  # Faire défiler jusqu'à l'élément
        first_name_wrapper.click()

        first_name = self.driver.find_element(By.ID, "firstName")
        self.scroll_to_element(first_name)  # Faire défiler jusqu'à l'élément
        first_name.send_keys("ari")

        last_name = self.driver.find_element(By.ID, "lastName")
        self.scroll_to_element(last_name)  # Faire défiler jusqu'à l'élément
        last_name.click()
        last_name.send_keys("arii")

        user_email = self.driver.find_element(By.ID, "userEmail")
        self.scroll_to_element(user_email)  # Faire défiler jusqu'à l'élément
        user_email.click()
        user_email.send_keys("ari@example.com")

        age = self.driver.find_element(By.ID, "age")
        self.scroll_to_element(age)  # Faire défiler jusqu'à l'élément
        age.click()
        age.send_keys("34")

        salary = self.driver.find_element(By.ID, "salary")
        self.scroll_to_element(salary)  # Faire défiler jusqu'à l'élément
        salary.send_keys("4000")  # Corrigez cette ligne
        # Remarquez que la ligne pour le département est manquante ici. Assurez-vous de l'ajouter si nécessaire.
