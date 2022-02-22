import logging

from selenium.webdriver.common.by import By

from .locators import Locators

invest_amount_locator = (By.XPATH, "//input[contains(@class,'pricing-input')]")
error_message_locator = (By.CLASS_NAME, "error-message")
fee_locator = (By.XPATH, "//*[contains(@class,'pricing-percentage')]/h1")


class Functions(object):

    def __init__(self, driver):
        self.driver = driver
        self.locator = Locators(self.driver)

    @staticmethod
    def log(text):
        # This method will be used to log to the console
        logging.getLogger().setLevel(logging.INFO)
        logging.info(text)

    def verify_country(self, country):
        """
        Verify country is displayed in this case: United Kingdom
        """
        country_locator = (By.CLASS_NAME, "country-name")
        assert self.locator.get_text(*country_locator) == country

    def verifyDefaultValues(self, value, fee):
        """
        Verify Default Values
        """
        assert str(self.locator.get_text(*invest_amount_locator)) in str(value)
        assert str(self.locator.get_text(*fee_locator)) in str(fee)

    def verifyOnlyNumericIsAllowed(self):
        """
        Verify numeric values are accepted
        """
        invest_fee = "12,345"
        self.locator.insert_text(invest_fee, *invest_amount_locator)
        value_found = self.locator.get_attribute_text("value", *invest_amount_locator)
        assert invest_fee == str(value_found)

        invest_fee_string = "abc"
        self.locator.insert_text(invest_fee_string, *invest_amount_locator)
        value_string_found = self.locator.get_attribute_text("value", *invest_amount_locator)
        assert bool(value_string_found) is False

    def enter_value(self, value):
        self.locator.insert_text(value, *invest_amount_locator)

    def verify_error_message(self, error_message):
        assert self.locator.select_element(*error_message_locator) is True
        assert str(self.locator.get_text(*error_message_locator)) in str(error_message)

    def verify_total_annual_fee(self, annual_fee):
        assert self.locator.select_element(*fee_locator) is True
        assert str(self.locator.get_text(*fee_locator)) in str(annual_fee)