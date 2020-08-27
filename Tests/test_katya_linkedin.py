import pytest
import time

from Pages.Linkedin import Link

@pytest.mark.link
def test_login(browser, env):
    link_page = Link(browser, env)
    link_page.login()
    link_page.move_to_sales_nav()
    link_page.vmware_leads_list()
    link_page.get_and_write_info()
    time.sleep(10)



