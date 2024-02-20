class AddNewItemTypeLocators:
    span_item_type_xpath = "//a[@href='/profiles/item-types']"
    button_add_new_item_type_xpath = "(//button[normalize-space()='Add New Item Type'])[1]"
    input_name_xpath = "//input[@name='countryName']"
    input_code_xpath = "//input[@name='countryCode']"
    button_save_xpath = "//*[@id='addNewItemTypesModal']/div/div/form/div[3]/div[2]/button"


class EditItemTypeLocators:
    icon_edit_item_type_xpath = "(//i[@title='Edit Item'][normalize-space()='edit'])[2]"
    input_edit_name_xpath = "//*[@id='mat-input-15']"
    button_save_xpath = "(//button[@class='btn btn-danger mat-raised-button'])[2]"


class DeleteItemTypeLocators:
    icon_delete_item_type_xpath = "//*[@id='datatables']/tbody/tr[2]/td[3]/i[2]"
    button_delete_accept_xpath = "(//button[normalize-space()='Yes, delete it!'])[1]"
    button_ok_xpath = "(//button[normalize-space()='OK'])[1]"

