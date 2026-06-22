from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException
)

from pages.base_page import BasePage


class PopupPage(BasePage):
    CLOSE_BUTTONS = [

        (
            By.XPATH,
            "//div[contains(@class,'common-popup-close-icon-container')]"
        ),

        (
            By.XPATH,
            "//img[contains(@src,'commonPopupCloseIcon')]"
        ),

        (
            By.XPATH,
            "//button[contains(@aria-label,'close')]"
        ),

        (
            By.XPATH,
            "//button[text()='Close']"
        ),

        (
            By.XPATH,
            "//button[text()='Skip']"
        ),

        (
            By.XPATH,
            "//button[contains(text(),'No')]"
        )
    ]

    BACKDROP = (
        By.XPATH,
        "//div[contains(@class,'MuiBackdrop-root')]"
    )

    def close_all_popups(self):

        for i in range(10):

            popup_found = False

            for locator in self.CLOSE_BUTTONS:

                try:

                    close_btn = self.wait.until(
                        EC.element_to_be_clickable(locator)
                    )

                    self.driver.execute_script(
                        "arguments[0].click();",
                        close_btn
                    )

                    popup_found = True

                except:
                    pass

            try:

                backdrop = self.driver.find_element(
                    *self.BACKDROP
                )

                self.driver.execute_script(
                    """
                    arguments[0].style.display='none';
                    """,
                    backdrop
                )

            except:
                pass

            if not popup_found:
                break
