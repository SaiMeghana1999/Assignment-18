from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DashboardPage(BasePage):
    PROFILE_ARROW = (By.ID, "profile-click-icon")
    LOGOUT = (By.XPATH, "//div[text()='Log out']")

    def logout(self):
        self.click(self.PROFILE_ARROW)
        self.click(self.LOGOUT)
