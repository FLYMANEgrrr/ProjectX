from behave import given, when, then
from selenium.webdriver.chrome import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from features.steps.locaters import locator


# @given('The AutomationPractice site is open')
# def open_website(context):
#     context.driver = webdriver.Chrome(ChromeDriverManager().install())
#     context.driver.implicitly_wait(10)
#     context.driver.get("http://automationpractice.com/index.php")
#     context.driver.maximize_window()
#     assert context.driver.title == "My Store"
#
#
# @given('The Sign In link is clicked')
# def click_signin_link(context):
#     assert context.driver.find_element(*locator["sign_in_link"]).is_displayed()
#     context.driver.find_element(*locator["sign_in_link"]).click()
#     assert context.driver.title == "Login - My Store"

#
# @given('Input email "{email}" and password "{pwd}"')
# def enter_info(context, email, pwd):
#     context.driver.find_element(*locator["sign_in_email"]).send_keys(email)
#     context.driver.find_element(*locator["sign_in_pass"]).send_keys(pwd)
#
#
@given('Click sign in button for cart')
def click_signin_button(context):
    context.driver.find_element(*locator["sign_in_button"]).click()


#
# @given('click woman link')
# def nav_page(context):
#     assert context.driver.find_element(*locator["women_link"]).is_displayed()
#     context.driver.find_element(*locator["women_link"]).click()
#     assert context.driver.title == "Women - My Store"


@given('click item')
def sstep(context):
    context.driver.find_element(*locator["women_item1"]).click()


@when('checkitem')
def stepp(context):
    context.driver.find_element(*locator["checkitem"]).click()

@when('add cart')
def add_cart(context):
    context.driver.find_element(*locator["checkout_button1"]).click()


@when('add cart1')
def add_cart(context):
    context.driver.find_element(*locator["checkout_button2"]).click()

@when('add cart2')
def add_cart(context):
    context.driver.find_element(*locator["checkout_button2.5"]).click()


@when('agree condition')
def add_cart(context):
    context.driver.find_element(*locator["checkout_button_3_1"]).click()
    # context.driver.find_element(*locator["checkout_button_3_2"]).click()

@then('deal')
def add_cart(context):
    context.driver.find_element(*locator["checkout_button_3_3"]).click()
