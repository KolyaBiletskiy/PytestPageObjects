import pytest
import time

from Pages.Blog import Blog

@pytest.mark.blog
def test_login(browser, env):
    blog_page = Blog(browser, env)
    blog_page.open_blog()
    blog_page.get_and_write_info()
    time.sleep(5)



