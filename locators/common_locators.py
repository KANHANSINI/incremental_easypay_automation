class CommonLocators:
    notification_xpath = ("//div[@class='alert alert-with-icon col-xs-11 col-sm-3 "
                          "alert alert-success animated fadeInDown']")
    notification_error_xpath = ("//div[@class='alert alert-with-icon col-xs-11 col-sm-3 "
                                "alert alert-danger animated fadeInDown']")
    notification_no_permission_xpath = ("//div[@class='alert alert-with-icon col-xs-11 col-sm-3 "
                                        "alert alert-warning animated fadeInDown']")
    error_message_xpath = "(//div[@role='dialog'])[1]"
    email_error_message_xpath = "//*[@id='mat-error-0']"
    password_error_message_xpath = "//*[@id='mat-error-1']"
