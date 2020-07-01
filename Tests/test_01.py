import pytest

from Pages.ToDoPages import SearchHelper


@pytest.mark.Smoke
def test_todo_input(browser):
    todo_main_page = SearchHelper(browser)
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


@pytest.mark.Sanity
def test_todo_input3(browser):
    todo_main_page = SearchHelper(browser)
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


@pytest.mark.Smoke
def test_todo_input2(browser):
    todo_main_page = SearchHelper(browser)
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
