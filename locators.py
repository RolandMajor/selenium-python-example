from selenium.webdriver.common.by import By

text_fields = {
    "Username": (By.ID, "user-name"),
    "Password": (By.ID, "password"),
    "First Name": (By.ID, "first-name"),
    "Last Name": (By.ID,"last-name"),
    "Zip Code": (By.ID, "postal-code")
}

item_buttons = {
    "Sauce Labs Backpack": (By.ID, "add-to-cart-sauce-labs-backpack"),
    "Sauce Labs Bike Light": (By.ID, "add-to-cart-sauce-labs-bike-light"),
    "Sauce Labs Bolt T-Shirt": (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
    "Sauce Labs Fleece Jacket": (By.ID, "add-to-cart-sauce-labs-fleece-jacket"),
    "Sauce Labs Onesie": (By.ID, "add-to-cart-sauce-labs-onesie"),
    "Test.allTheThings() T-Shirt (Red)": (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
}

navigation_buttons = {
    "Login": (By.ID, "login-button"),
    "Cart": (By.CLASS_NAME, "shopping_cart_link"),
    "Checkout": (By.ID, "checkout"),
    "Continue": (By.ID, "continue"),
    "Finish": (By.ID, "finish"),
    "Back Home": (By.ID, "back-to-products"),
}

labels = {
    "Error Message": (By.CSS_SELECTOR, "#login_button_container > div > form > div.error-message-container.error > h3"),
    "Price Label": (By.CLASS_NAME, "summary_total_label"),
    "Checkout Error": (By.CSS_SELECTOR, "#checkout_info_container > div > form > div.checkout_info > div.error-message-container.error > h3")
}

