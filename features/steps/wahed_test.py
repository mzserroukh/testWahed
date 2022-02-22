import time

from behave import *
from selenium.webdriver.common.by import By


@given('user navigate to wahed url')
def step_navigate_to_url(context):
    context.driver.get(context.url)


@then('The "{country}" should be displayed at the top right of the page')
def step_country_is_displayed(context, country):
    context.function.verifyCountry(country)


@then('The United Kingdom should be displayed at the top right of the page')
def step_search(context):
    context.function.verify_country("United Kingdom")


@then('Default values are to show "{value}" and Very Aggressive with a Total Annual Fee of "{fee}"')
def step_default_values(context, value, fee):
    context.function.verifyDefaultValues(value, fee)


@then('Default values are to show £10,000 and Very Aggressive with a Total Annual Fee of 0.99%')
def step_default_values(context):
    context.function.verifyDefaultValues("10,000", "0.99%")


@then('Only allow numeric values in the I want to invest in box')
def verify_only_numeric_values(context):
    context.function.verifyOnlyNumericIsAllowed()


@when('user enters {value}')
def enter_value(context, value):
    context.function.enter_value(value)


@then('user is shown the error message {error_message}')
def verify_error_message(context, error_message):
    context.function.verify_error_message(error_message)


@then('total annual fee is {annual_fee}')
def verify_total_annual_fee(context, annual_fee):
    context.function.verify_total_annual_fee(annual_fee)