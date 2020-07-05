import pytest

from Pages.ToDoPages import SearchHelper

@pytest.mark.smoke
@pytest.mark.skip
class TodoTests:
    @pytest.mark.sanity
    def test_todo_input(self, browser, env):
        todo_main_page = SearchHelper(browser, env)
        todo_main_page.go_to_site()
        todo_main_page.enter_word("Hello")
        todo_main_page.press_enter()
        todo_main_page.enter_word("John")
        todo_main_page.press_enter()
        elements = todo_main_page.check_navigation_bar()
        with open("list.txt", "w") as file:
            file.write(str(elements))
            file.close()
        assert "John" and "adsadasdasd" in elements


    @pytest.mark.sanity
    def test_todo_input3(self, browser, env):
        todo_main_page = SearchHelper(browser, env)
        todo_main_page.go_to_site()
        todo_main_page.enter_word("Hello")
        todo_main_page.press_enter()
        todo_main_page.enter_word("John")
        todo_main_page.press_enter()
        elements = todo_main_page.check_navigation_bar()
        with open("list.txt", "w") as file:
            file.write(str(elements))
            file.close()
        assert "John" and "Sanity" in elements

    @pytest.mark.skip(reason="Test reason")
    def test_todo_input2(self, browser, env):
        todo_main_page = SearchHelper(browser, env)
        todo_main_page.go_to_site()
        todo_main_page.enter_word("Hello")
        todo_main_page.press_enter()
        todo_main_page.enter_word("John")
        todo_main_page.press_enter()
        elements = todo_main_page.check_navigation_bar()
        with open("list.txt", "w") as file:
            file.write(str(elements))
            file.close()
        assert "John" in elements
