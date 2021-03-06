from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, env):
        self.driver = driver
        self.base_url = {
            'prod': 'http://todomvc-app-for-testing.surge.sh/',
            'dev': 'http://todomvc-app-for-testing.surge.sh/dsadasd',
            'stage': 'http://todomvc-app-for-testing.surge.sh/'
        }[env]

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def wait_tab(self, num, time=10):
        return WebDriverWait(self.driver, time).until(EC.number_of_windows_to_be(num),
                                                      message=f"Can't find enough number of windows - {num}")

