import time

from Base.BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Data:
    email = ""
    password = ''

class LinkLocators:
    email = (By.CSS_SELECTOR, '[id="session_key"]')
    password = (By.CSS_SELECTOR, '[id="session_password"]')
    sign_in_btn = (By.CSS_SELECTOR, '[class="sign-in-form__submit-button"]')
    sales_nav = (By.CSS_SELECTOR, '[data-link-to="sales-nav"]')

class SalesLocators:
    menu_lists = (By.CSS_SELECTOR, '[href="/sales/lists/people"]')
    vmvare_leads = (By.CSS_SELECTOR, 'table[class] tbody tr:first-child  a')
    lead_name = (By.CSS_SELECTOR, 'tbody[class="ember-view"] tr [role="presentation"] a')
    position = (By.CSS_SELECTOR, 'tbody[class="ember-view"] tr [role="presentation"] div:nth-child(2)')
    account = (By.CSS_SELECTOR, 'tbody[class="ember-view"] tr td:nth-child(2)')
    location = (By.CSS_SELECTOR, 'tbody[class="ember-view"] tr td:nth-child(3)')
    next_btn = (By.CSS_SELECTOR, 'button[aria-label="Next"]')
    current_page = (By.CSS_SELECTOR, '[aria-current="true"]')

class Link(BasePage):

    def login(self):
        self.driver.get("https://www.linkedin.com/")
        email_field = self.find_element(LinkLocators.email)
        pass_field = self.find_element(LinkLocators.password)
        email_field.send_keys(Data.email)
        pass_field.send_keys(Data.password)
        pass_field.send_keys(Keys.RETURN)
        return pass_field

    def move_to_sales_nav(self):
        self.find_element(LinkLocators.sales_nav).click()
        self.wait_tab(2)
        self.driver.switch_to.window(self.driver.window_handles[1])

    def vmware_leads_list(self):
        self.find_element(SalesLocators.menu_lists).click()
        self.find_element(SalesLocators.vmvare_leads).click()
        time.sleep(2)

    def get_and_write_info(self):

        for item in range(24):

            leads_names = self.find_elements(SalesLocators.lead_name)
            position = self.find_elements(SalesLocators.position)
            account = self.find_elements(SalesLocators.account)
            location = self.find_elements(SalesLocators.location)

            for names, positions, accounts, locations in zip(leads_names, position, account, location):
                name = names.text
                name_link = names.get_attribute('href')
                position = positions.text
                account = accounts.text
                location = locations.text

                with open("leads_list.txt", "a") as file:
                    file.write(f"{name}; {name_link}; {position}; {account}; {location}, \n")

            self.find_element(SalesLocators.next_btn).click()


            name_on_current_page = '//tbody[@class="ember-view"]/tr//*[@role="presentation"]/a[text()="'+str(name)+'"]'
            print(name_on_current_page)
            WebDriverWait(self.driver, 10).until(EC.invisibility_of_element((By.XPATH, name_on_current_page)))
            time.sleep(2)

















