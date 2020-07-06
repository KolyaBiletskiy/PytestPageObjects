import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


# @pytest.fixture(scope="session")  # means that current fixture will be executed once per session
# def browser():
#     options = Options()
#     # options.add_argument('--headless')
#     driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
#     yield driver  # divide function before and after test run
#     driver.quit()
"""
In this case the tests will be run both on chrome and firefox and the webdrivers should be places in the
default location, for instance, on mac "usr/local/bin"
scope desc:
function	Run once per test
class	Run once per class of tests
module	Run once per module
session	Run once per session
"""
@pytest.fixture(params=[webdriver.Chrome, webdriver.Firefox], scope='module')
def browser(request):
    driver = request.param
    drvr = driver()
    yield drvr
    drvr.quit()


"""
Here we add the possibility to select environment via command line
"""
def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="prod", help="Environment to run tests on")


@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption('--env')