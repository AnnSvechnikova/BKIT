Feature: generating ideas for parties
    Scenario: cycling
        Given user answers "да", "да", "да"
        When bot recieves the messages
        Then I expect the result to bе "велопрогулка"

    Scenario: picknick
        Given user answers "да", "нет", "да"
        When bot recieves the messages
        Then I expect the result to bе "пикник"

