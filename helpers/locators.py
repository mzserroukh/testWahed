from selenium.common.exceptions import TimeoutException, InvalidElementStateException, WebDriverException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Locators(object):

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)

        try:
            self.driver.implicitly_wait(10)
        except WebDriverException as _:
            pass

    def insert_text(self, text, *loc, **kwargs):
        try:
            delay = kwargs.get('delay', 5)
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located(loc))
            element = self.driver.find_element(*loc)
            self.driver.execute_script("return arguments[0].scrollIntoView();", element)
            self.driver.find_element(*loc).clear()

            element.send_keys(text)
        except InvalidElementStateException as _:
            element.send_keys(text)

    def click_element(self, *loc, **kwargs):
        delay = kwargs.get('delay', 5)
        WebDriverWait(self.driver, delay).until(EC.presence_of_element_located(loc))
        element = self.driver.find_element(*loc)
        # element.click()
        self.driver.execute_script("arguments[0].click();", element)

    def get_text(self, *loc, **kwargs):
        delay = kwargs.get('delay', 2)
        WebDriverWait(self.driver, delay).until(EC.presence_of_element_located(loc))
        element = self.driver.find_element(*loc)
        self.driver.execute_script("return arguments[0].scrollIntoView();", element)
        return element.text

    def select_element_drop_down(self, drop_down_text, *loc, **kwargs):
        delay = kwargs.get('delay', 5)
        WebDriverWait(self.driver, delay).until(EC.element_to_be_clickable(loc))
        element = Select(self.driver.find_element(*loc))
        element.select_by_visible_text(drop_down_text)

    def select_element(self, *loc, **kwargs):
        delay = kwargs.get('delay', 10)
        try:
            WebDriverWait(self.driver, delay).until(EC.visibility_of_element_located(loc))
            element = self.driver.find_element(*loc)
            if element != '' or element is not None:
                self.driver.execute_script("return arguments[0].scrollIntoView();", element)
                return True
            else:
                return False
        except TimeoutException as _:
            return False

    def get_attribute_text(self, value, *loc, **kwargs):
        delay = kwargs.get('delay', 2)
        try:
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located(loc))
            element = self.driver.find_element(*loc)
            if element != '' or element is not None:
                self.driver.execute_script("return arguments[0].scrollIntoView();", element)
                return element.get_attribute(value)
            else:
                return False
        except TimeoutException as _:
            return False

    def select_elements(self, *loc, **kwargs):
        delay = kwargs.get('delay', 5)
        try:
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located(loc))
            element = self.driver.find_elements(*loc)
            list_of_text_found = [str(found_text.text) for found_text in element]
            return list_of_text_found
        except TimeoutException as _:
            return False

    def click_elements(self, pos, *loc, **kwargs):
        delay = kwargs.get('delay', 5)
        WebDriverWait(self.driver, delay).until(EC.presence_of_element_located(loc))
        elements = self.driver.find_elements(*loc)
        for counter, element in enumerate(elements):
            if counter == pos:
                element.click()
                break

    def press_enter(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.RETURN)
        actions.perform()
