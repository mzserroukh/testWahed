import os
from selenium import webdriver
from helpers.locators import Locators
from helpers.functions import Functions


def before_all(context):
    project_root = os.path.abspath(os.getcwd())
    driver_root = os.path.join(project_root, "driver/chromedriver")
    context.driver = webdriver.Chrome(driver_root)
    context.url = 'https://www.wahedinvest.com/pricing/'
    context.function = Functions(context.driver)
    context.locator = Locators(context.driver)
    context.driver.maximize_window()


def after_scenario(context, scenario):
    pass


def after_all(context):
    context.driver.quit()
