from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL = (By.XPATH, "//input[@placeholder='Enter your mail']")
    PASSWORD = (By.XPATH, "//input[@type='password']")
    SIGNIN_BUTTON = (By.XPATH, "//button[@type='submit']")

    def validate_email_box(self):
        return self.get_element(self.EMAIL).is_displayed()

    def validate_password_box(self):
        return self.get_element(self.PASSWORD).is_displayed()

    def validate_signin_button(self):
        return self.get_element(self.SIGNIN_BUTTON).is_displayed()

    def login(self, email, password):
        self.enter_text(self.EMAIL, email)
        self.enter_text(self.PASSWORD, password)
        self.click(self.SIGNIN_BUTTON)

    def close_dashboard_popups(self):

        popup_locators = [(By.CSS_SELECTOR, "button.custom-close-button"),

                          (
                              By.CSS_SELECTOR,
                              "div.common-popup-close-icon-container"
                          ),

                          (
                              By.XPATH,
                              "//button[contains(text(),'No, I’m Good')]"
                          ),

                          (
                              By.XPATH,
                              "//button[contains(text(),'No, I'm Good')]"
                          )
                          ]

        for locator in popup_locators:

            try:

                element = self.wait.until(
                    EC.element_to_be_clickable(locator)
                )

                self.driver.execute_script(
                    "arguments[0].click();",
                    element
                )

            except:
                pass
