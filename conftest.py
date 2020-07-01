import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")  # означает что данная функция-фикстура будет исполнятся только 1 раз за тестовую сессию
def browser():
    options = Options()
    # options.add_argument('--headless')
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    yield driver  # разделяет функцию на часть — до тестов и после тестов.
    driver.quit()
