from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from locators import text_fields, navigation_buttons, labels
from csv import reader
from hamcrest import assert_that, equal_to
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

PAGE_URL = "http://saucedemo.com/"

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.implicitly_wait(10)

driver.get(PAGE_URL)
driver.maximize_window()

driver.find_element(*text_fields["Username"]).send_keys("standard_user")
driver.find_element(*text_fields["Password"]).send_keys("secret_sauce")
driver.find_element(*navigation_buttons["Login"]).click()
driver.find_element(*navigation_buttons["Cart"]).click()
driver.find_element(*navigation_buttons["Checkout"]).click()

with open('checkout_data.csv') as csvfile:
    csvreader = reader(csvfile, delimiter=',')
    for firstname, lastname, zipcode, expected_error in csvreader:
        driver.find_element(*text_fields["First Name"]).send_keys(Keys.CONTROL, 'a')
        driver.find_element(*text_fields["First Name"]).send_keys(Keys.DELETE)
        driver.find_element(*text_fields["Last Name"]).send_keys(Keys.CONTROL, 'a')
        driver.find_element(*text_fields["Last Name"]).send_keys(Keys.DELETE)
        driver.find_element(*text_fields["Zip Code"]).send_keys(Keys.CONTROL, 'a')
        driver.find_element(*text_fields["Zip Code"]).send_keys(Keys.DELETE)

        driver.find_element(*text_fields["First Name"]).send_keys(firstname)
        driver.find_element(*text_fields["Last Name"]).send_keys(lastname)
        driver.find_element(*text_fields["Zip Code"]).send_keys(zipcode)
        driver.find_element(*navigation_buttons["Continue"]).click()
        actual_error = driver.find_element(*labels["Checkout Error"]).text
        assert_that(actual_error, equal_to(expected_error))

driver.quit()
