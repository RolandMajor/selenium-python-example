Feature: Saucedemo Shopping

  Background:
    Given the home page is opened
    And the 'Username' field is filled with 'standard_user'
    And the 'Password' field is filled with 'secret_sauce'
    And the 'Login' button is clicked

    Scenario Outline: Buying a backpack and t-shirt
      Given the '<item1>' is added to the cart
      And the '<item2>' is added to the cart
      And the 'Cart' button is clicked
      And the 'Checkout' button is clicked
      And the 'First Name' field is filled with 'testname_first'
      And the 'Last Name' field is filled with 'testname_last'
      And the 'Zip Code' field is filled with '1111'
      When the 'Continue' button is clicked
      Then the price should read '<total>'
      And the 'Finish' button is clicked
      And the 'Back Home' button is clicked
      Examples:
        | item1 	            | item2                             | total 	    |
        | Sauce Labs Backpack   | Sauce Labs Bolt T-Shirt           | Total: $49.66 |
        | Sauce Labs Bike Light | Sauce Labs Fleece Jacket          | Total: $64.78 |
	    | Sauce Labs Onesie     | Test.allTheThings() T-Shirt (Red) | Total: $25.90 |
