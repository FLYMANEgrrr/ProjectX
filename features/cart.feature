Feature: add item to cart
  Background: login account
    Given The AutomationPractice site is open
    And The Sign In link is clicked
    And Input email "s1ss@gmail.com" and password "12345"
    And Click sign in button for cart

  Scenario: test add item to cart
    Given click woman link
    And click item
    When checkitem
    And add cart
    And add cart1
    And add cart2
    And agree condition
    Then deal

