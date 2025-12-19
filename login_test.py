from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from locators import text_fields, navigation_buttons, labels
from csv import reader
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)

driver.get("http://saucedemo.com/")
driver.maximize_window()

with open('login_data.csv') as csvfile:
    csvreader = reader(csvfile, delimiter=';')
    for row in csvreader:
        username, password, error = row
        
        driver.find_element(*text_fields["Username"]).send_keys(Keys.CONTROL, 'a')
        driver.find_element(*text_fields["Username"]).send_keys(Keys.DELETE)
        driver.find_element(*text_fields["Password"]).send_keys(Keys.CONTROL, 'a')
        driver.find_element(*text_fields["Password"]).send_keys(Keys.DELETE)
        
        driver.find_element(*text_fields["Username"]).send_keys(username)
        driver.find_element(*text_fields["Password"]).send_keys(password)
        driver.find_element(*navigation_buttons["Login"]).click()
       
        assert driver.find_element(*labels["Error Message"]).text == error
        
driver.quit()
