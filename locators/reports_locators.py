class ReportLocators:
    paragraph_reports_xpath = "(//p[normalize-space()='Reports'])[1]"


class PaymentReceiptsLocators:
    span_payment_receipts_xpath = "(//span[normalize-space()='Payment Receipts'])[1]"
    input_date_from_xpath = "//*[@id='min']"
    input_date_to_xpath = "//*[@id='max']"
    button_search_xpath = "(//button[@id='search'])[1]"
    table_xpath = "//*[@id='paymentReceipt']"
    tr_xpath = "//*[@id='paymentReceipt']/tbody/tr[1]"
    td_name_xpath = "//*[@id='paymentReceipt']/tbody/tr[1]/td[1]"
    button_export_xpath = "(//button[@data-target='#exportModal'])[1]"
    button_excel_xpath = "(//button[@class='btn btn-success mat-button'])[1]"
    button_pdf_xpath = "(//button[@class='btn btn-danger mat-button'])[1]"
    button_close_xpath = "(//button[@class='close mat-button'])[1]"


class InvoiceReportsLocators:
    input_date_from_xpath = "//*[@id='min']"
    input_date_to_xpath = "//*[@id='max']"
    span_invoice_reports_xpath = "(//span[normalize-space()='Invoice Reports'])[1]"
    table_xpath = "//*[@id='invoiceReceiptTable']"
    tr_xpath = "//*[@id='invoiceReceiptTable']/tbody/tr[1]"
    td_name_xpath = "//*[@id='invoiceReceiptTable']/tbody/tr[1]/td[2]"
    button_search_xpath = "(//button[@class='btn btn-danger mat-raised-button'])[1]"
    button_date_from_xpath = "(//button[@aria-label='Open calendar'])[1]"
    div_arrow_xpath = "(//div[@class='mat-calendar-arrow'])[1]"
    div_year_1_xpath = "(//div[normalize-space()='2020'])[1]"
    div_month_xpath = "(//div[normalize-space()='JAN'])[1]"
    div_date_xpath = "(//div[normalize-space()='1'])[1]"
    button_date_to_xpath = "(//button[@aria-label='Open calendar'])[2]"
    div_year_2_xpath = "(//div[normalize-space()='2021'])[1]"
