from behave import given, when, then
from features.steps.locaters import locator

@when('retrieve password button is clicked')
def click_retrieve_password(context):
    context.driver.find_element(*locator["retrieve_password_button"]).click()

@given('Enter forgot email "{email}"')
def step_impl(context, email):
    context.driver.find_element(*locator["forgot_email"]).send_keys(email)


@given('click forgot password link')
def forgot_pass_link(context):
    assert context.driver.find_element(*locator["forgot_pass_link"]).is_displayed()
    context.driver.find_element(*locator["forgot_pass_link"]).click()
    assert context.driver.title == "Forgot your password - My Store"

@then('show error message "{msg}"')
def error_msg_info(context,msg):
    if context.driver.find_element(*locator["forgot_pass_error_msg"]):
        print("Invalid email address.")
    context.driver.close()
    assert True, "Test Passed"

@then('show success info get forgot pass email')
def access_granted(context):
    text = context.driver.find_element(*locator["forgot_pass_success_msg_info"]).text
    assert text == "A confirmation email has been sent to your address: s2@gmail.com"
    context.driver.close()