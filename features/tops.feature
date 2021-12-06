Feature: AutomationPractice Tops page test

  Background:
    Given The AutomationPractice site is open
    And click woman link

  Scenario Outline: Checking all types of Tops.
    When top page "<page>" click
    Then  sub page "<top>" under "<page>"
    Examples:
      | page | top    |
      | Tops | T-shirts |
      | Tops | Blouses  |

  Scenario Outline: Checking T-Shirts & Blouses.
    When top page "<page>" click
    And "<subsub>"sub sub page click
    Then  sub page "<top>" under "<page>"
    Examples:
      | page | subsub  | top                       |
      | Tops | T-shirts | Faded Short Sleeve T-shirts |
      | Tops | Blouses  | Blouse                      |