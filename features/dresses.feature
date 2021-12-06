Feature: AutomationPractice dresses page test

  Background:
    Given The AutomationPractice site is open
    And clicked dresses link

  Scenario Outline: check all items under dresses page
    When click sub page "<page>"
    Then  "<dress>" should appear in the "<page>".
    Examples:
      | page            | dress                 |
      | Casual Dresses  | Printed Dress         |
      | Evening Dresses | Printed Dress         |
      | Summer Dresses  | Printed Summer Dress  |
      | Summer Dresses  | Printed Chiffon Dress |
