class AddNewRoomTypeLocators:
    span_room_type_xpath = "(//span[normalize-space()='Room Types'])[1]"
    button_add_new_room_type_xpath = "(//button[normalize-space()='Add New Room Type'])[1]"
    input_name_xpath = "//input[@name='roomName']"
    input_code_xpath = "//input[@name='codeValue']"
    button_save_xpath = "(//button[@class='btn btn-danger mat-raised-button'])[1]"


class EditRoomTypeLocators:
    icon_edit_xpath = "(//i[@title='Edit Item'][normalize-space()='edit'])[2]"
    input_name_xpath = "//*[@id='mat-input-4']"
    button_save_xpath = "//*[@id='editRooms']/div/div/form/div[3]/div[2]/button"


class DeleteRoomTypeLocators:
    icon_remove_item_xpath = "(//i[@title='Remove Item'][normalize-space()='clear'])[5]"
    button_accept_delete_xpath = "(//button[normalize-space()='Yes, delete it!'])[1]"
    button_ok_xpath = "(//button[normalize-space()='OK'])[1]"


class SearchRoomTypeLocators:
    input_search_name_xpath = "(//input[@id='listingSearch'])[1]"
    table_xpath = "//*[@id='datatables']"
    tr_xpath = "//*[@id='datatables']/tbody/tr"
    td_name_xpath = "//*[@id='datatables']/tbody/tr[1]/td[1]"
    td_code_xpath = "//*[@id='datatables']/tbody/tr/td[2]"

