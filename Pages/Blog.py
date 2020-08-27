import time

from Base.BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BlogLocators:
    title = (By.CSS_SELECTOR, '[class="block post-page"] [class="entry-title"] a')
    name_date = (By.CSS_SELECTOR, '[class="block post-page"] [class="entry-meta"]')
    next_btn = (By.CSS_SELECTOR, '[class="emm-next"]')


class Blog(BasePage):

    def open_blog(self):
        self.driver.get("https://cdn.net/blog/")
        time.sleep(2)

    def text_content(self):

        textContent = self.find_elements(BlogLocators.name_date)

        for item in textContent:
            print(item.get_property('textContent').split('|')[0])

    def get_and_write_info(self):

        for item in range(13):

            titles = self.find_elements(BlogLocators.title)
            name_dates = self.find_elements(BlogLocators.name_date)

            for title_item, name_date in zip(titles, name_dates):
                title = title_item.text
                title_link = title_item.get_attribute('href')
                name_and_date = name_date.get_property('textContent').split('|')[0]

                with open("blog_list.txt", "a") as file:
                    file.write(f"{title}; {title_link}; {name_and_date}, \n")

            self.find_element(BlogLocators.next_btn).click()


            title_on_current_page = '//a[text()="'+str(title)+'"]'
            print(title)
            WebDriverWait(self.driver, 10).until(EC.invisibility_of_element((By.XPATH, title_on_current_page)))
            time.sleep(2)

















