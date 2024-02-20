class CreateDiscountLocators:
    list_discount_xpath = "(//a[@ng-reflect-router-link='/profiles/discounts'])[1]"
    button_add_new_discount_xpath = "(//button[normalize-space()='Add New Discount'])[1]"
    input_name_xpath = "//input[@name='termName']"
    input_code_xpath = "//input[@name='codeValue']"
    input_amount_xpath = "//input[@name='AmountValue']"
    input_percentage_xpath = "//input[@name='percentageValue']"
    textarea_description_xpath = "//textarea[@name='itemDescription']"
    button_save_xpath = "(//button[@class='btn btn-danger mat-raised-button'])[1]"


class EditDiscountLocators:
    icon_edit_discount_xpath = "//*[@id='datatables']/tbody/tr[1]/td[3]/i[1]"
    input_edit_percentage_xpath = "(//input[@id='mat-input-10'])[1]"
    button_save_xpath = "//*[@id='editDiscount']/div/div/form/div[4]/div[2]/button"


class DeleteDiscountLocators:
    icon_delete_discount_xpath = "//*[@id='datatables']/tbody/tr[3]/td[3]/i[2]"
    button_accept_delete_xpath = "(//button[normalize-space()='Yes, delete it!'])[1]"


class SearchDiscountLocators:
    input_search_xpath = "//*[@id='listingSearch']"
    table_xpath = "//*[@id='datatables']"
    tr_xpath = "//*[@id='datatables']/tbody/tr"
    td_name_xpath = "//*[@id='datatables']/tbody/tr/td[2]"
    td_code_xpath = "//*[@id='datatables']/tbody/tr/td[1]"
