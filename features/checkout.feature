Feature: Saucedemo Checkout

  Background:
    Given the home page is opened
    And the 'Username' field is filled with 'standard_user'
    And the 'Password' field is filled with 'secret_sauce'
    And the 'Login' button is clicked
    And the 'Cart' button is clicked
    And the 'Checkout' button is clicked

    Scenario Outline: Incorrect checkout attempts
      Given the 'First Name' field is filled with '<firstname>'
      And the 'Last Name' field is filled with '<lastname>'
      And the 'Zip Code' field is filled with '<zipcode>'
      When the 'Continue' button is clicked
      Then the '<checkoutError>' message is shown
      Examples:
        | firstname 	| lastname     | zipcode     | checkoutError                  |
        | [blank]   	| [blank]      | [blank]     | Error: First Name is required  |
	    | [blank]       | TestLastName | [blank]     | Error: First Name is required  |
	    | [blank]       | [blank]      | TestZipCode | Error: First Name is required  |
        | [blank]       | TestLastName | TestZipCode | Error: First Name is required  |
        | TestFirstName | [blank]      | [blank]     | Error: Last Name is required   |
	    | TestFirstName | [blank]      | TestZipCode | Error: Last Name is required   |
	    | TestFirstName | TestLastName | [blank]     | Error: Postal Code is required |
