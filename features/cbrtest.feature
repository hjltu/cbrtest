Feature: cbrtest

Scenario Outline: Visit search <site>
    When open <site>
    Then search bar must be empty

Examples: Site
| site|
| google.ru |

Scenario: Google search
    When fill the search bar
    Then click the search button

Scenario: Open cbr.ru
    When found link cbr.ru
    Then click on the link cbr.ru

Scenario: Open reception
    Given checked that the site is open
    When open link "Reception"
    Then open section "Write thanks"

Scenario: Write thanks message
    When write text
    When click checkbox
    Then take a screenshot

Scenario: Compate two "About" texts
    When click on burger
    And open link "About"
    And open link "Warning"
    Then save warning text
    When change language on "en"
    And compare new text
    Then take another screenshot
