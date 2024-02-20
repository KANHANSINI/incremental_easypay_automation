class DashboardPageLocators:
    button_drop_down_hotel_xpath = "//*[@id='navigation']/ul/div/button"
    list_hotels_xpath = "//ul[@class='dropdown-menu dropdown-menu-left show']//li[a[text()='Testing Hotel']]"
    button_date_range_selection_xpath = ("(//button[@class='dropdown-toggle btn btn-primary btn-round "
                                         "mat-raised-button'])[1]")
    list_date_range_xpath = "(//ul[@class='dropdown-menu dropdown-menu-left show'])[1]"
    list_today_xpath = "//a[contains(text(),'Today')]"
    list_yesterday_xpath = "//a[contains(text(),'Yesterday')]"
    list_last_week_xpath = "//a[contains(text(),'Last Week')]"
    list_last_month_xpath = "//a[contains(text(),'Last Month')]"
    list_custom_xpath = "//a[contains(text(),'Custom')]"
    input_from_date_xpath = "(//input[@id='fromDateCustom'])[1]"
    input_to_date_xpath = "(//input[@id='toDateCustom'])[1]"
    button_search_xpath = ("(//button[contains(@class,'btn btn-danger "
                           "my-4 mat-raised-button ng-star-inserted')])[1]")
    td_guest_xpath = "//*[@id='invoiceTable']/tbody/tr[1]/td[1]"
    div_success_invoices_xpath = ("(//div[contains(@class,'col-md-5 text-center mt-2 "
                                  "border-right padding-0 cursor-pointer')])[1]")
    div_pending_invoices_xpath = ("(//div[contains(@class,'col-md-5 text-center mt-2 "
                                  "border-right padding-0 cursor-pointer')])[2]")
    div_failed_invoices_xpath = ("(//div[contains(@class,'col-md-5 text-center mt-2"
                                 " border-right padding-0 cursor-pointer')])[3]")
    button_create_new_invoice_xpath = "(//button[normalize-space()='Create New Invoice'])[1]"
