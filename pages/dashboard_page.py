from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DashboardPage(BasePage):

    DASHBOARD_MESSAGE = (
        By.CSS_SELECTOR,
        "div.example h2"
    )

    LOGOUT_BUTTON = (
        By.CSS_SELECTOR,
        "a.button.secondary.radius"
    )

    def is_on_dashboard(self):
        """
        Memastikan user berada di halaman dashboard
        """
        return (
            self.is_visible(self.DASHBOARD_MESSAGE)
            and "/secure" in self.get_current_url()
        )

    def logout(self):
        """
        Klik tombol logout
        """
        self.click(self.LOGOUT_BUTTON)