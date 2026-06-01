import allure
from pages.dashboard_page import DashboardPage
@allure.feature("Authentication")
@allure.story("Logout")
class TestLogout:

    @allure.title(
        "User berhasil logout setelah login"
    )
    @allure.severity(
        allure.severity_level.CRITICAL
    )
    def test_user_can_logout(
            self,
            login_page
    ):

        with allure.step(
            "Login menggunakan akun valid"
        ):
            login_page.login(
                "tomsmith",
                "SuperSecretPassword!"
            )

        dashboard = DashboardPage(
            login_page.driver
        )

        with allure.step(
            "Verifikasi dashboard tampil"
        ):
            assert dashboard.is_on_dashboard()

        with allure.step(
            "Klik Logout"
        ):
            dashboard.logout()

        with allure.step(
            "Verifikasi kembali ke login"
        ):
            assert login_page.is_on_login_page()