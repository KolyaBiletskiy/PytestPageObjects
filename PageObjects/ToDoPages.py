from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ToDoLocators:
    title = (By.CSS_SELECTOR, "header h1")
    input = (By.CSS_SELECTOR, "input[type='text']")
    complete_checkbox = (By.CSS_SELECTOR, '.view input[type="checkbox"]')
    labels = (By.CSS_SELECTOR, '.todo-list label')


class SearchHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(ToDoLocators.input)
        search_field.send_keys(word)
        search_field.send_keys(Keys.RETURN)
        return search_field

    def press_enter(self):
        return self.find_element(ToDoLocators.complete_checkbox, time=2).send_keys(Keys.RETURN)

    def check_navigation_bar(self):
        all_labels = self.find_elements(ToDoLocators.labels, time=2)
        labels_in_list = [x.text for x in all_labels if len(x.text) > 0]
        print(labels_in_list)
        return labels_in_list
