import os
import pytest


@pytest.hookimpl(
    tryfirst=True,
    hookwrapper=True
)
def pytest_runtest_makereport(
        item,
        call
):

    outcome = yield

    report = outcome.get_result()

    if (
        report.when == "call"
        and report.failed
    ):

        driver = item.funcargs.get(
            "driver"
        )

        if driver:

            os.makedirs(
                "reports/screenshots",
                exist_ok=True
            )

            filename = (
                item.nodeid
                .replace("/", "_")
                .replace("::", "_")
            )

            driver.save_screenshot(
                f"reports/screenshots/{filename}.png"
            )

            print(
                f"\nScreenshot disimpan: {filename}.png"
            )