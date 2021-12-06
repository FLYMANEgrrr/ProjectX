from behave import given, when, then

from features.steps.locaters import locator

@given('click woman link')
def nav_page(context):
    assert context.driver.find_element(*locator["women_link"]).is_displayed()
    context.driver.find_element(*locator["women_link"]).click()
    assert context.driver.title == "Women - My Store"


@when('top page "{page}" click')
def tops_page(context, page):
    if page == "Tops":
        assert context.driver.find_element(*locator["tops_link"]).is_displayed()
        context.driver.find_element(*locator["tops_link"]).click()
        assert context.driver.title == "Tops - My Store"

@when('"{subsub}"sub sub page click')
def all_tops_dresses(context, subsub):
    if subsub == "T-shirts":
        context.driver.find_element(*locator["t-shirts_link"]).click()
    elif subsub == "Blouses":
        context.driver.find_element(*locator["blouses_link"]).click()

@then('sub page "{top}" under "{page}"')
def tops_catgs(context, top, page):
    if page == "Tops":
        if top == "T-shirts":
            context.driver.find_element(*locator["t-shirts_link"]).is_displayed()

            if context.driver.find_element(*locator["Faded_Short_Sleeve_T-shirts"]).text == top:
                assert context.driver.find_element(*locator["Faded_Short_Sleeve_T-shirts"]).text == top

        elif top == "Blouses":
            context.driver.find_element(*locator["blouses_link"]).is_displayed()

            if context.driver.find_element(*locator["Blouse"]).text == top:
                assert context.driver.find_element(*locator["Blouse"]).text == top
