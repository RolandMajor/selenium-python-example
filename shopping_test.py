from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from locators import text_fields, item_buttons, navigation_buttons, labels
from csv import reader
from hamcrest import assert_that, equal_to
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.implicitly_wait(10)

driver.get("http://saucedemo.com/")
driver.maximize_window()

driver.find_element(*text_fields["Username"]).send_keys("standard_user")
driver.find_element(*text_fields["Password"]).send_keys("secret_sauce")
driver.find_element(*navigation_buttons["Login"]).click()

with open('shopping_data.csv') as csvfile:
    csvreader = reader(csvfile, delimiter=',')
    for item1, item2, expected_total in csvreader:

        driver.find_element(*item_buttons[item1]).click()
        driver.find_element(*item_buttons[item2]).click()
        driver.find_element(*navigation_buttons["Cart"]).click()
        driver.find_element(*navigation_buttons["Checkout"]).click()
        driver.find_element(*text_fields["First Name"]).send_keys("testname_first")
        driver.find_element(*text_fields["Last Name"]).send_keys("testname_last")
        driver.find_element(*text_fields["Zip Code"]).send_keys("1111")
        driver.find_element(*navigation_buttons["Continue"]).click()

        actual_total = driver.find_element(*labels["Price Label"]).text
        assert_that(actual_total, equal_to(expected_total))

        driver.find_element(*navigation_buttons["Finish"]).click()
        driver.find_element(*navigation_buttons["Back Home"]).click()


driver.quit()