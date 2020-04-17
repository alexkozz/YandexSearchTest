from base import Base
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class YandexSeacrhLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
    LOCATOR_YANDEX_SEARCH_SUGGESTION_TABLE = (By.CLASS_NAME, "mini-suggest__popup_visible")
    LOCATOR_YANDEX_SEARCH_FIRST_RESULT = (By.XPATH, "((//li[@class='serp-item'])[1]//b)[2]")
    LOCATOR_YANDEX_SEARCH_IMAGES_BTN = (By.XPATH, "(//div[contains(@class, 'home-tabs')])/a[@data-id='images']")
    LOCATOR_YANDEX_SEARCH_IMAGES_IMG = (By.XPATH, "//div[@class='image__wrap']//img")
    LOCATOR_YANDEX_SEARCH_IMAGES_FIRST_IMG_MIN = (By.XPATH, "//div[contains(@class, 'cl-teaser')]")
    LOCATOR_YANDEX_SEARCH_IMAGES_NAV_LEFT = (By.XPATH, "//div[contains(@class, 'cl-viewer-navigate__item_left')]")
    LOCATOR_YANDEX_SEARCH_IMAGES_NAV_RIGHT = (By.XPATH, "//div[contains(@class, 'cl-viewer-navigate__item_right')]")

class YaPages(Base):

    def check_first_result(self, text):
        element = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIRST_RESULT, timeout = 3)
        assert text in element.text, 'first result does not match'
    
    def check_url(self, link):
        time.sleep(3)
        url = self.driver.current_url
        assert url == link, url + ' is not ' + link

    def check_suggestion_table(self):
        self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_SUGGESTION_TABLE, timeout = 3)

    def click_first_image_min(self):
        self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_IMAGES_FIRST_IMG_MIN, timeout = 5).click()

    def enter_word(self, field, word):
        field.click()
        field.send_keys(word)
        return field
    
    def get_image(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_IMAGES_IMG, timeout = 3)

    def get_next_image_src(self, img, src):
        return self.wait_img(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_IMAGES_IMG, 3, img, src)

    def get_images_btn(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_IMAGES_BTN, timeout = 3)

    def get_nav_left(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_IMAGES_NAV_LEFT, timeout = 3)

    def get_nav_right(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_IMAGES_NAV_RIGHT, timeout = 3)

    def get_search_field(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD, timeout = 3)

    def img_equal(self, src1, src2):
        assert src1 in src2, 'images are not equal'

    def img_not_equal(self, src1, src2):
        assert src1 not in src2, 'images are equal'

    def press_enter(self, element):
        element.send_keys(Keys.ENTER)
        return element

    
        