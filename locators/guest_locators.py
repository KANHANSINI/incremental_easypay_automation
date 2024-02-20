class CreateNewGuestPageLocators:
    list_create_new_invoice_xpath = "(//a[@class='nav-link'])[2]"
    link_create_new_invoice_xpath = "(//a[@routerlink='/create/new-invoice'])[1]"
    input_select_guest_xpath = "//input[@name='guest']"
    span_create_new_guest_xpath = "//*[@id='mat-option-0']/span"
    input_first_name_xpath = "//input[@name='FirstName']"
    input_last_name_xpath = "//input[@name='Lastname']"
    input_email_xpath = "//input[@name='emailValue']"
    input_phone_number_xpath = "//input[@name='phoneValue']"
    input_address_line_1_xpath = "//input[@name='addressline1']"
    input_address_line_2_xpath = "//input[@name='addressline2']"
    div_select_country_xpath = "//*[@id='cityCountry']/div"
    span_country_xpath = "//span[contains(text(), 'Singapore')]"
    div_select_state_xpath = "//*[@id='cityState']/div"
    span_state_xpath = "//span[contains(text(), ' Central Singapore Community Development Council ')]"
    div_select_city_xpath = "//*[@id='cityname']/div"
    option_city_xpath = "//mat-option[.//span[text()=' Singapore ']]"
    input_zip_code_xpath = "//input[@placeholder='Zip Code']"
    button_save_and_select_xpath = "//*[@id='addNewGuestModal']/div/div/form/div[3]/button"
    span_guest_xpath = "//*[@id='profiles']/ul/li[1]/a/span[2]"
    button_add_new_guest_xpath = "(//button[normalize-space()='Add New Guest'])[1]"


class AddNewGuestPageLocators:
    input_first_name_xpath = "//input[@name='FirstName']"
    input_last_name_xpath = "//input[@name='Lastname']"
    input_email_xpath = "//input[@name='emailValue']"
    input_phone_number_xpath = "//input[@name='phoneValue']"
    input_address_line_1_xpath = "//input[@name='addressline1']"
    input_address_line_2_xpath = "//input[@name='addressline2']"
    span_drop_down_select_country_xpath = "//*[@id='cityCountry']/div/div[1]/span"
    span_country_xpath = "(//span[normalize-space()='Germany'])[1]"
    span_drop_down_select_state_xpath = "//*[@id='cityState']/div/div[1]/span"
    span_state_xpath = "(//span[normalize-space()='Hamburg'])[1]"
    span_drop_down_select_city_xpath = "//*[@id='cityname']/div/div[1]/span"
    span_city_xpath = "(//span[normalize-space()='Horst'])[1]"
    input_zip_code_xpath = "//input[@name='pin']"
    button_save_xpath = "//*[@id='addNewGuestModal']/div/div/form/div[3]/div[2]/button"
