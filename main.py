import os

@pytest.fixture(scope="function")
def driver():

    options = webdriver.ChromeOptions()

    if os.getenv("CI"):

        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        ),
        options=options
    )

    yield driver

    driver.quit()