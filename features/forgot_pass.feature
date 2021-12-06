Feature: AutomationPractice forgot password in page test

  Background:
    Given The AutomationPractice site is open
    And The Sign In link is clicked

  Scenario: forgot password test with valid email
    Given click forgot password link
    And Enter forgot email "s2@gmail.com"
    When retrieve password button is clicked
    Then show success info get forgot pass email

  Scenario Outline: Forgot test with invalid email address
    Given click forgot password link
    And Enter forgot email "<email>"
    When retrieve password button is clicked
    Then show error message "<msg>"
    Examples:
      |   email            |       msg            |
      | asdl@af.com        |Invalid email address.|
      | leijun@gail.com    |Invalid email address.|
      |    asdafsd         |Invalid email address.|
      | sfajslk@126.com    |Invalid email address.|
      | sendkey.sfs.com    |Invalid email address.|