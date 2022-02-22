@wahed
Feature: Interview
  As a potential UK customer, I want to explore Wahed’s Annual Fees at
    www.wahedinvest.com/pricing with various investment amounts and
    portfolio strategies using a pricing calculator before I decide to invest.

  Background:
    Given user navigate to wahed url

 @scenario1
  Scenario Outline: Test wahed acceptance criteria
    Then The <country> should be displayed at the top right of the page
    And Default values are to show <investValue> and Very Aggressive with a Total Annual Fee of <annualFee>
    And Only allow numeric values in the I want to invest in box
   Examples:
   | country        | investValue | annualFee |
   | United Kingdom | £10,000     | 0.99%     |

  @scenario2
  Scenario Outline: Test minimum investment value
    When user enters <minimumInvestmentValue>
    Then user is shown the error message “Minimum investment is £50”
    Examples:
    |minimumInvestmentValue|
    | 49                   |

  @scenario3
  Scenario Outline:
    When user enters <investmentValue>
    Then total annual fee is <annualFee>
    Examples:
      | investmentValue | annualFee |
      | 1000            | 4.22%     |
      | 5000            | 1.35%     |
      | 123456          | 1.12%     |