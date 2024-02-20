class AccessLocators:
    paragraph_access_xpath = "(//p[normalize-space()='Access'])[1]"
    span_users_xpath = "(//span[normalize-space()='Users'])[1]"


class AddNewUserLocators:
    button_create_new_user_xpath = "(//button[normalize-space()='Create New User'])[1]"
    input_email_xpath = "//*[@id='id_email']"
    input_name_xpath = "//*[@id='mat-input-4']"
    input_password_xpath = "//*[@id='mat-input-3']"
    input_confirm_password_xpath = "//*[@id='mat-input-5']"
    span_assign_role_xpath = "//*[@id='mat-select-0']/div/div[1]/span"
    span_assign_a_role_xpath = "//*[@id='mat-option-3']/span"
    span_assign_hotel_xpath = "//*[@id='720854229-selectable']/span"
    button_save_xpath = "(//button[@class='btn btn-danger mat-raised-button'])[1]"
    span_error_xpath = "//*[@id='mat-error-1']"
    mat_error_name_xpath = "//*[@id='mat-error-2']"


class DeleteUserLocators:
    icon_delete_xpath = "//*[@id='datatables']/tbody/tr[2]/td[4]/i[2]"
    button_accept_delete_xpath = "(//button[normalize-space()='Yes, delete it!'])[1]"


class SearchUserLocators:
    input_search_xpath = "//*[@id='listingSearch']"
    td_name_xpath = "//*[@id='datatables']/tbody/tr[1]/td[1]"
    td_email_xpath = "//*[@id='datatables']/tbody/tr[1]/td[2]"
    td_role_xpath = "//*[@id='datatables']/tbody/tr/td[3]"


class EditUserLocators:
    icon_edit_xpath = "//*[@id='datatables']/tbody/tr[2]/td[4]/i[1]"
