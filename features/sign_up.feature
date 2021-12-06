Feature: AutomationPractice sign in page test

  Background:
    Given The AutomationPractice site is open
    And The Sign In link is clicked

  Scenario: Create a User using valid data
    Given Enter email "123456@mail.com"
    When Click create account button
    When Gender "Mr."
    And First name"Hello"
    And last name"World"
    And Password "123456789"
    And Date of Birth of "9-10-1954"
    And Advertise
    And Address "Example street 19"
    And City "San Francisco"
    And State "Washington"
    And zip code "12345"
    And USA
    And telephone "952766"
    And Default My Address
    Then successfully create and username "Hello world"

  Scenario Outline: Create a User using valid data
    Given Enter email "<email>"
    When Click create account button
    And Gender "<gender>"
    And First name"<fname>"
    And last name"<lname>"
    And Password "<passwd>"
    And Date of Birth of "<dob>"
    And Advertise
    And Address "<address>"
    And City "<city>"
    And State "<state>"
    And zip code "<zip-code>"
    And USA
    And telephone "<mobile>"
    And Default My Address
    Then successfully create and username "<acc>"
    Examples:
      | email            | gender | fname  | lname      | acc               | passwd  | dob       | address            | city          | state      | zip-code | mobile  |
      | rrwww@email.com  | Mr.    | han    | meimei     | han meimei        | 5678910 | 1-12-1950 | Example street 15  | San Francisco | California | 00000    | 5876657 |
      | wer@email.com    | Mr.    | lee    | lei        | lee lei           | 5978910 | 8-10-1955 | Example street 139 | Los Angeles   | New York   | 67890    | 6454578 |
      | wr@email.com     | Mrs.   | wang   | wam        | wang wam          | 5678999 | 1-11-1956 | Example street 8   | San Diego     | Washington | 12345    | 3876656 |
      | asf@email.com    | Mr.    | lee    | na         | lee na            | 3278910 | 9-10-1954 | Example street 10  | San Jose      | California | 11111    | 7857558 |
      | sdf@mail.com     | Mr.    | jobs   | alex       | jobs alex         | 1234567 | 9-12-1991 | Example street 234 | San Jose      | California | 12345    | 9952766 |
      | phpum1@email.com | Mr.    | David  | Jobs       | David Jobs        | 5978910 | 8-10-1955 | Example street 139 | Los Angeles   | New York   | 67890    | 9676687 |