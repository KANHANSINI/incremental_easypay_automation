class AddNewItemPageLocators:
    span_items_xpath = "//*[@id='profiles']/ul/li[2]/a/span[2]"
    button_add_new_item_xpath = "(//button[normalize-space()='Add New Item'])[1]"
    input_name_xpath = "//input[@name='itemName']"
    input_code_xpath = "//input[@name='codeValue']"
    input_rate_xpath = "//input[@name='rateValue']"
    span_select_item_type_xpath = ("//*[@id='addNewRateModal']/div/div/form/div[2]/div[2]/mat-form-field[2]/div/div["
                                   "1]/div")
    span_item_type_xpath = "//span[normalize-space()='Accommodation']"
    input_description_xpath = "//input[@name='itemDescription']"
    button_save_xpath = "(//button[@class='btn btn-danger mat-raised-button'])[1]"
    button_close_xpath = "(//i[@class='material-icons'][normalize-space()='close'])[1]"
