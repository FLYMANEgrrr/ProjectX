
from behave import given, when, then
from features.steps.locaters import locator

@given('clicked dresses link')
def nav_page(context):
    assert context.driver.find_element(*locator["dresses_link"]).is_displayed()
    context.driver.find_element(*locator["dresses_link"]).click()
    assert context.driver.title == "Dresses - My Store"


@when('click sub page "{page}"')
def dress_page(context, page):
    if page == "Casual Dresses":
        assert context.driver.find_element(*locator["casual_dresses_link"]).is_displayed()
        context.driver.find_element(*locator["casual_dresses_link"]).click()
        assert context.driver.title == "Casual Dresses - My Store"
    if page == "Evening Dresses":
        assert context.driver.find_element(*locator["evening_dresses_link"]).is_displayed()
        context.driver.find_element(*locator["evening_dresses_link"]).click()
        assert context.driver.title == "Evening Dresses - My Store"
    if page == "Summer Dresses":
        assert context.driver.find_element(*locator["summer_dresses_link"]).is_displayed()
        context.driver.find_element(*locator["summer_dresses_link"]).click()
        assert context.driver.title == "Summer Dresses - My Store"


@then('"{dress}" should appear in the "{page}".')
def pick_dress(context, dress, page):
    if page == "Casual Dresses":
        assert context.driver.find_element(*locator["casual_printed_dress"]).text == dress
    elif page == "Evening Dresses":
        assert context.driver.find_element(*locator["evening_printed_dress"]).text == dress
    elif page == "Summer Dresses":
        if context.driver.find_element(*locator["printed_summer_dress"]).text == dress:
            assert True, "It's Printed Summer Dress"
        else:
            assert context.driver.find_element(*locator["printed_chiffon_dress"]).text == dress
