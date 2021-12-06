from selenium.webdriver.common.by import By

locator = {
    "logo": (By.XPATH, "//*[@id='header_logo']/a/img"),
    "sign_in_link": (By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a'),
    "dresses_link": (By.XPATH, '//*[@id="block_top_menu"]/ul/li[2]/a'),
    "women_link": (By.XPATH, '//*[@id="block_top_menu"]/ul/li[1]/a'),
    "tops_link": (By.XPATH, '//*[@id="subcategories"]/ul/li[1]/h5/a'),
    "t-shirts_link": (By.XPATH, '//*[@id="subcategories"]/ul/li[1]/h5/a'),
    "blouses_link": (By.XPATH, '//*[@id="subcategories"]/ul/li[2]/h5/a'),
    "Faded_Short_Sleeve_T-shirts": (By.XPATH, '//*[@id="center_column"]/ul/li/div/div[2]/h5/a'),
    "Blouse": (By.XPATH, '//*[@id="center_column"]/ul/li/div/div[2]/h5/a'),
    "sign_in_email": (By.ID, "email"),
    "sign_in_pass": (By.ID, "passwd"),
    "sign_in_button": (By.ID, "SubmitLogin"),
    "my_account": (By.XPATH, '//*[@id="center_column"]/h1'),
    "error_msg": (By.XPATH, '//*[@id="center_column"]/div[1]/ol/li'),
    "sign_up_email": (By.ID, "email_create"),
    "account_name": (By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a/span'),
    "create_account_button": (By.ID, "SubmitCreate"),
    "gender_radiobutton_mr": (By.ID, "id_gender1"),
    "gender_radiobutton_mrs": (By.ID, "id_gender2"),
    "firstname": (By.ID, "customer_firstname"),
    "lastname": (By.ID, "customer_lastname"),
    "sign_up_password": (By.ID, "passwd"),
    "days_dropdown": (By.ID, "days"),
    "months_dropdown": (By.ID, "months"),
    "years_dropdown": (By.ID, "years"),
    "newsletter_checkbox": (By.ID, "newsletter"),
    "optin_checkbox": (By.ID, "optin"),
    "sign_up_address": (By.ID, "address1"),
    "city": (By.ID, "city"),
    "state_dropdown": (By.ID, "id_state"),
    "postcode": (By.ID, "postcode"),
    "mobile": (By.ID, "phone_mobile"),
    "register_button": (By.ID, "submitAccount"),
    "contact_us": (By.XPATH, "//*[@id='contact-link']/a"),
    "subject_heading": (By.ID, "id_contact"),
    "contact_email": (By.ID, "email"),
    "contact_message": (By.ID, "message"),
    "attach_file_button": (By.ID, "fileUpload"),
    "submit_message_contact": (By.ID, "submitMessage"),
    "succ_contact_msg": (By.XPATH, '//*[@id="center_column"]/p'),
    "fail_contact_msg": (By.XPATH, '//*[@id="center_column"]/div/ol/li'),
    "casual_dresses_link": (By.XPATH, '//*[@id="subcategories"]/ul/li[1]/h5/a'),
    "evening_dresses_link": (By.XPATH, '//*[@id="subcategories"]/ul/li[2]/h5/a'),
    "summer_dresses_link": (By.XPATH, '//*[@id="subcategories"]/ul/li[3]/h5/a'),
    "printed_summer_dress": (By.XPATH, '//*[@id="center_column"]/ul/li[1]/div/div[2]/h5/a'),
    "printed_chiffon_dress": (By.XPATH, '//*[@id="center_column"]/ul/li[3]/div/div[2]/h5/a'),
    "casual_printed_dress": (By.XPATH, '//*[@id="center_column"]/ul/li/div/div[2]/h5/a'),
    "evening_printed_dress": (By.XPATH, '//*[@id="center_column"]/ul/li/div/div[2]/h5/a'),
    "retrieve_password_button": (By.XPATH, '//*[@id="form_forgotpassword"]/fieldset/p/button'),
    "forgot_email": (By.ID, "email"),
    "forgot_pass_error_msg": (By.XPATH, '//*[@id="center_column"]/div/div/ol/li'),
    "forgot_pass_success_msg_info": (By.XPATH, '//*[@id="center_column"]/div/p'),
    "forgot_pass_link": (By.XPATH, '//*[@id="login_form"]/div/p[1]/a'),
    "women_item1": (By.XPATH, '//*[@id="center_column"]/ul/li[1]/div/div[2]/h5/a'),
    "checkitem":(By.XPATH,'//*[@id="add_to_cart"]/button'),
    "checkout_button1": (By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a'),
    "checkout_button2": (By.XPATH, '//*[@id="center_column"]/p[2]/a[1]'),
    "checkout_button2.5":(By.XPATH,'//*[@id="center_column"]/form/p/button'),
    "checkout_button_3_1":(By.XPATH,'//*[@id="cgv"]'),
    "checkout_button_3_2":(By.XPATH,'//*[@id="uniform-cgv"]'),
    "checkout_button_3_3":(By.XPATH,'//*[@id="form"]/p/button')

}
