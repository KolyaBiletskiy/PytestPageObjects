import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")  # означает что данная функция-фикстура будет исполнятся только 1 раз за тестовую сессию
def browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver  # разделяет функцию на часть — до тестов и после тестов.
    driver.quit()
