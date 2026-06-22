Feature: Zen Portal Login

  Scenario: Validate Username Input Box

    Given User opens Zen Portal
    Then Username textbox should be visible


  Scenario: Validate Password Input Box

    Given User opens Zen Portal
    Then Password textbox should be visible


  Scenario: Validate Sign In Button

    Given User opens Zen Portal
    Then Sign In button should be visible


  Scenario: Successful Login

    Given User opens Zen Portal
    When User enters valid credentials
    Then Login should be successful


  Scenario: Unsuccessful Login

    Given User opens Zen Portal
    When User enters invalid credentials
    Then Login should fail


  Scenario: Validate Logout

    Given User opens Zen Portal
    When User logs in
    Then User should logout successfully