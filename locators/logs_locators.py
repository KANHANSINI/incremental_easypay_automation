class LogsPageLocators:
    paragraph_logs_xpath = "(//p[normalize-space()='Logs'])[1]"


class EmailLocators:
    span_email_logs_xpath = "//*[@id='maps']/ul/li[1]/a/span[2]"
    span_payment_logs_xpath = "//*[@id='maps']/ul/li[2]/a/span[2]"
    icon_actions_xpath = "//*[@id='datatables']/tbody/tr[1]/td[5]/i"
    icon_close_xpath = "(//i[normalize-space()='close'])[1]"
    input_search_xpath = "(//input[@id='listingSearch'])[1]"
    table_xpath = "//*[@id='datatables']"
    tr_xpath = "//*[@id='datatables']/tbody/tr"
    td_recipients_name_xpath = "//*[@id='datatables']/tbody/tr[1]/td[4]"
    td_invoice_number_xpath = "//*[@id='datatables']/tbody/tr[1]/td[1]"
    td_date_xpath = "//*[@id='datatables']/tbody/tr[1]/td[2]"
    td_subject_xpath = "//*[@id='datatables']/tbody/tr[1]/td[3]"
    td_confirmation_number_xpath = "//*[@id='datatables']/tbody/tr/td[1]"
    td_date_time_xpath = "//*[@id='datatables']/tbody/tr/td[2]"
    td_amount_xpath = "//*[@id='datatables']/tbody/tr[1]/td[4]"
    td_invoice_number_payment_log_xpath = "//*[@id='datatables']/tbody/tr/td[3]"
