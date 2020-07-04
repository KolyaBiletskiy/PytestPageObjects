import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")  # means that current fixture will be executed once per session
def browser():
    options = Options()
    # options.add_argument('--headless')
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    yield driver  # divide function before and after test run
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="prod", help="Environment to run tests on")


@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption('--env')