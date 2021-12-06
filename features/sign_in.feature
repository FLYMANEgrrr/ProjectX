Feature: AutomationPractice sign in page test

  Background:
    Given The AutomationPractice site is open
    And The Sign In link is clicked

  Scenario: Sign in to AutomationPractice with valid credential
    Given Input email "s2@gmail.com" and password "12345"
    When Click sign in button
    Then successfully login account


  Scenario Outline: Fail Sign-In
    Given Enter email "<parameter>" and password "<password>"
    When Click sign in button
    Then The "<msg>" error message is shown
    Examples:
      | parameter         | password | msg                        |
      |                   | 123      | An email address required. |
      | invalid.email.com | 12345    | Invalid email address.     |
      | valid@email.com   |          | Password is required.      |
      |                   |          | An email address required. |
      | leijun@gmail.com  | 1asdfda  | Authentication failed.     |