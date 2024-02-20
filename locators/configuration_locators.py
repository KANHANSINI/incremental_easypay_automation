class OrganizationDetailsLocators:
    paragraph_configuration_xpath = "(//p[normalize-space()='Configurations'])[1]"
    span_organization_details_xpath = "(//span[normalize-space()='Organization Details'])[1]"
# Search Configuration Locators:
    input_search_xpath = "(//input[@id='listingSearch'])[1]"
    td_code_xpath = "(//td[@class='sorting_1'])[1]"
    td_name_xpath = "//*[@id='datatables']/tbody/tr/td[2]"
# Edit Configuration Locators:
    icon_edit_xpath = "(//i[@title='Edit Item'])[1]"
# Delete Configuration Locators:
    icon_delete_xpath = "(//i[@title='Remove Item'])[1]"


class PaymentSettingsLocators:
    span_payment_settings_xpath = "(//span[normalize-space()='Payment Settings'])[1]"
# Edit Payment Settings Locators:
    icon_edit_xpath = "(//i[@title='Edit Item'])[1]"
# Delete Payment Settings Locators:
    icon_delete_xpath = "(//i[@title='Remove Item'])[1]"
# Search Payment Settings Locators:
    input_search_xpath = "(//input[@id='listingSearch'])[1]"
    td_name_xpath = "//*[@id='datatables']/tbody/tr/td[2]"
    td_empty_name_xpath = "(//td[@class='dataTables_empty'])[1]"


class EmailConfigurationLocators:
    span_email_configurations_xpath = "(//span[normalize-space()='Email Configuration'])[1]"
# Edit Email Configuration Locators:
    icon_edit_xpath = "(//i[@title='Edit Item'])[1]"
# Delete Email Configuration Locators:
    icon_delete_xpath = "(//i[@title='Remove Item'])[1]"
# Search Email Configuration Locators:
    input_search_xpath = "(//input[@id='listingSearch'])[1]"
    td_name_xpath = "//*[@id='datatables']/tbody/tr/td[1]"


class TaxSetupLocators:
    span_tax_setup_xpath = "(//span[normalize-space()='Tax Setup'])[1]"
    button_create_new_tax_setup_xpath = "(//button[normalize-space()='Add New Tax Setup'])[1]"
    input_name_xpath = "//*[@id='mat-input-2']"
    input_percentage_xpath = "//*[@id='mat-input-5']"
    span_select_rules_xpath = "//*[@id='mat-select-0']/div/div[1]/span"
    span_visa_charges_xpath = "(//span[normalize-space()='Visa Charges'])[1]"
    span_tourism_fee_xpath = "(//span[normalize-space()='Tourism Fee'])[1]"
    span_rule_2_xpath = "(//span[@class='toggle'])[1]"
    button_save_xpath = "(//button[@class='btn btn-danger mat-raised-button'])[1]"

