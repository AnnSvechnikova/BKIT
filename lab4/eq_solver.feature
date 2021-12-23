Feature: solving a biquadrate equation
    Scenario: One root
        Given I have the coefs 1 and 0 and 0
        When I solve equation
        Then I expect the result to be 0

    Scenario: Two roots
        Given I have the coefs 1 and 0 and -16
        When I solve equation
        Then I expect the result to be 2, -2

    Scenario: Three roots
        Given I have the coefs -4 and 16 and 0
        When I solve equation
        Then I expect the result to be 2, -2, 0