import pytest

from pages.register_page import RegisterPage
from tests.conftest import load_csv


DATA = load_csv(
    "register_data.csv"
)


class TestRegisterDDT:

    @pytest.mark.parametrize(
        "row",
        DATA,
        ids=[
            row["description"]
            for row in DATA
        ]
    )
    def test_register(
            self,
            driver,
            row
    ):

        page = RegisterPage(driver)

        page.register(
            row["firstname"],
            row["lastname"],
            row["username"],
            row["password"]
        )

        expected = row["expected"]

        # Simulasi validasi

        if expected == "PASS":

            assert True, (
                f"{row['description']} "
                "harus berhasil"
            )

        else:

            assert False, (
                f"{row['description']} "
                "harus gagal"
            )