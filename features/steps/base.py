from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Base:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait
        self.url = "https://yandex.ru/"

    def find_element(self, locator, timeout = 10):
        return self.wait(self.driver, timeout).until(EC.presence_of_element_located(locator),
                                                      message = f"Can't find element by locator {locator}")

    def find_elements(self, locator, timeout = 10):
        return self.wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator),
                                                      message = f"Can't find elements by locator {locator}")

    def open_site(self):
        return self.driver.get(self.url)
        
    def close_tab(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    #def wait_url(self, timeout, link):
    #    return self.wait(self.driver, timeout).until(lambda d: link if (self.driver.current_url in link) else self.driver.current_url)

    def wait_img(self, locator, timeout, img, src):
        return self.wait(self.driver, timeout).until(lambda d: img.get_attribute('src') if (img.get_attribute('src') not in src) else 'can\'t get next image')