import time
import pyautogui
from utilities.helper import take_screenshot

SHORT_WAIT = 4
MEDIUM_WAIT = 7
LONG_WAIT = 40


def sleep(seconds):
    time.sleep(seconds)


def upload_image(image_path):
    sleep(SHORT_WAIT)
    pyautogui.typewrite(image_path)
    pyautogui.press("enter")
    sleep(SHORT_WAIT)


def upload_video(video_path):
    sleep(SHORT_WAIT)
    pyautogui.typewrite(video_path)
    pyautogui.press("enter")
    sleep(SHORT_WAIT)


# Login Assertions
def perform_login_invalid_credentials_001_assertion(driver, login_page, logger, success_message):
    if success_message in login_page.retrieve_error_message():
        assert True
        logger.info("********* Login with valid username and invalid password - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "login_invalid_credentials_scr.png")
        logger.error("*********  Login with valid username and invalid password - Test Failed *********")
        assert False


def perform_login_invalid_credentials_002_assertion(driver, login_page, logger, success_message):
    if success_message in login_page.retrieve_error_message():
        assert True
        logger.info("********* Login with invalid username and valid password - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "login_invalid_credentials_scr.png")
        logger.error("********* Login with invalid username and valid password - Test Failed *********")
        assert False


def perform_login_invalid_credentials_003_assertion(driver, login_page, logger, success_message):
    if success_message in login_page.retrieve_error_message():
        assert True
        logger.info("********* Login with invalid username and invalid password - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "login_invalid_credentials_scr.png")
        logger.error("********* Login with invalid username and invalid password - Test Failed *********")
        assert False


def perform_create_payment_invoice_assertion(driver, create_invoice_page, logger, success_message):
    if success_message in create_invoice_page.retrieve_success_message():
        assert True
        logger.info("********* Create Payment Invoice - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_create_payment_invoice_scr.png")
        logger.error("*********  Create Payment Invoice - Test Failed *********")
        assert False


def perform_create_new_guest_assertion(driver, create_new_guest_page, logger, success_message):
    if success_message in create_new_guest_page.retrieve_success_message():
        assert True
        logger.info("********* Create Payment Invoice - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_create_guest_scr.png")
        logger.error("*********  Create Payment Invoice - Test Failed *********")
        assert False


def perform_create_new_invoice_negative_testing(driver, create_invoice_page, logger, success_message):
    if success_message in create_invoice_page.retrieve_warning_message():
        assert True
        logger.info("********* Create new invoice negative testing - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_create_payment_invoice_scr.png")
        logger.error("*********  Create new invoice negative testing - Test Failed *********")
        assert False


def perform_create_new_discount_assertion(driver, create_new_discount_page, logger, success_message):
    if success_message in create_new_discount_page.retrieve_warning_message():
        assert True
        logger.info("********* Create new discount - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_create_new_discount_scr.png")
        logger.error("*********  Create new discount - Test Failed *********")
        assert False


def perform_create_new_item_assertion(driver, item_page, logger, success_message):
    if success_message in item_page.retrieve_warning_message():
        assert True
        logger.info("********* Create add new item - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_create_item_scr.png")
        logger.error("********* Create add new item - Test Failed *********")
        assert False


def perform_create_new_general_term_assertion(driver, create_new_general_terms, logger, success_message):
    if success_message in create_new_general_terms.retrieve_warning_message():
        assert True
        logger.info("********* Create new general terms - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_create_new_general_terms_scr.png")
        logger.error("*********  Create new general terms - Test Failed *********")
        assert False


def perform_create_new_payment_term_assertion(driver, create_new_payment_terms, logger, success_message):
    if success_message in create_new_payment_terms.retrieve_warning_message():
        assert True
        logger.info("********* Create new payment terms - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_create_new_payment_terms_scr.png")
        logger.error("*********  Create new payment terms - Test Failed *********")
        assert False


def perform_save_edit_invoice_assertion(driver, invoice_page, logger, success_message):
    if success_message in invoice_page.retrieve_success_message():
        assert True
        logger.info("********* Save invoice - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_save_invoice_scr.png")
        logger.error("*********  Save invoice - Test Failed *********")
        assert False


def perform_send_email_assertion(driver, invoice_page, logger, success_message):
    if success_message in invoice_page.retrieve_success_message():
        assert True
        logger.info("********* Send Email - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_send_email_scr.png")
        logger.error("*********  Send Email - Test Failed *********")
        assert False


def perform_generate_link_assertion(driver, invoice_page, logger, success_message):
    if success_message in invoice_page.retrieve_success_message():
        assert True
        logger.info("********* Generate link - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_generate_link_scr.png")
        logger.error("*********  Generate link - Test Failed *********")
        assert False


def perform_delete_invoice_assertion(driver, invoice_page, logger, success_message):
    if success_message in invoice_page.retrieve_success_message():
        assert True
        logger.info("********* Delete Invoice - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_delete_invoice_scr.png")
        logger.error("*********  Delete Invoice - Test Failed *********")
        assert False


def perform_edit_discount_assertion(driver, edit_discount_page, logger, success_message):
    if success_message in edit_discount_page.retrieve_warning_message():
        assert True
        logger.info("********* Edit discount - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_edit_discount_scr.png")
        logger.error("*********  Edit discount - Test Failed *********")
        assert False


def perform_delete_discount_assertion(driver, delete_discount_page, logger, success_message):
    if success_message in delete_discount_page.retrieve_warning_message():
        assert True
        logger.info("********* Delete discount - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_delete_discount_scr.png")
        logger.error("*********  Delete discount - Test Failed *********")
        assert False


def perform_create_new_discount_without_enter_amount_or_percentage_assertion(driver, create_new_discount_page, logger,
                                                                             success_message):
    if success_message in create_new_discount_page.retrieve_warning_message():
        assert True
        logger.info("********* Create new discount without enter amount or percentage - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_create_new_discount_scr.png")
        logger.error("*********  Create new discount without enter amount or percentage - Test Failed *********")
        assert False


def perform_duplicate_records_discount_assertion(driver, create_new_discount_page, logger, success_message):
    if success_message in create_new_discount_page.retrieve_warning_message():
        assert True
        logger.info("********* Check duplicate records - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_check_duplicate_records_scr.png")
        logger.error("*********  Check duplicate records - Test Failed *********")
        assert False


def perform_create_new_guest_negative_testing_assertion(driver, create_new_guest_page, logger, success_message):
    if success_message in create_new_guest_page.retrieve_warning_message():
        assert True
        logger.info("********* Create add new guest - Negative Testing - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_create_guest_negative_testing_scr.png")
        logger.error("********* Create add new guest - Negative Testing - Test Failed *********")
        assert False


def perform_create_new_item_type_assertion(driver, item_type_page, logger, success_message):
    if success_message in item_type_page.retrieve_success_message():
        assert True
        logger.info("********* Create new item type - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_create_new_item_type_scr.png")
        logger.error("*********  Create new item type - Test Failed *********")
        assert False


def perform_edit_item_type_assertion(driver, item_type_page, logger, success_message):
    if success_message in item_type_page.retrieve_success_message():
        assert True
        logger.info("********* Edit item type - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_edit_item_type_scr.png")
        logger.error("*********  Edit item type - Test Failed *********")
        assert False


def perform_create_new_room_type_assertion(driver, room_type, logger, success_message):
    if success_message in room_type.retrieve_success_message():
        assert True
        logger.info("********* Create new room type - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_create_new_room_type_scr.png")
        logger.error("********* Create new room type - Test Failed *********")
        assert False


def perform_create_room_type_assertion(driver, room_type, logger, success_message):
    if success_message in room_type.retrieve_warning_message():
        assert True
        logger.info("********* Create new room type - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_create_new_room_type_scr.png")
        logger.error("********* Create new room type - Test Failed *********")
        assert False


def perform_edit_room_type_assertion(driver, room_type, logger, success_message):
    if success_message in room_type.retrieve_success_message():
        assert True
        logger.info("********* Edit room type - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_edit_room_type_scr.png")
        logger.error("********* Edit room type - Test Failed *********")
        assert False


def perform_remove_room_type_assertion(driver, room_type, logger, success_message):
    if success_message in room_type.retrieve_warning_message():
        assert True
        logger.info("********* Remove room type - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_remove_room_type_scr.png")
        logger.error("********* Remove room type - Test Failed *********")
        assert False


def perform_add_new_user_assertion(driver, access, logger, success_message):
    if success_message in access.retrieve_success_message():
        assert True
        logger.info("********* Add new user - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_add_new_user_scr.png")
        logger.error("********* Add new user - Test Failed *********")
        assert False


def perform_delete_user_assertion(driver, delete_user, logger, success_message):
    if success_message in delete_user.retrieve_warning_message():
        assert True
        logger.info("********* Delete user - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_delete_user_scr.png")
        logger.error("*********  Delete user - Test Failed *********")
        assert False


def perform_add_new_user_with_same_email_assertion(driver, access, logger, success_message):
    if success_message in access.retrieve_warning_message():
        assert True
        logger.info("********* Add new user with same email - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_add_new_user_negative_testing_scr.png")
        logger.error("********* Add new user with same email - Test Failed *********")
        assert False


def perform_add_new_user_with_invalid_email_assertion(driver, access, logger, success_message):
    if success_message in access.error_message():
        assert True
        logger.info("********* Add new user with invalid email - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_add_new_user_negative_testing_scr.png")
        logger.error("********* Add new user with invalid email - Test Failed *********")
        assert False


def perform_edit_user_assertion(driver, access, logger, success_message):
    if success_message in access.retrieve_success_message():
        assert True
        logger.info("********* Edit user - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_edit_user_scr.png")
        logger.error("********* Edit user - Test Failed *********")
        assert False


def perform_edit_configuration_assertion(driver, configurations, logger, success_message):
    if success_message in configurations.retrieve_warning_message():
        assert True
        logger.info("********* Edit configuration details - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_edit_configuration_scr.png")
        logger.error("********* Edit configuration details - Test Failed *********")
        assert False


def perform_delete_configuration_assertion(driver, configurations, logger, success_message):
    if success_message in configurations.retrieve_warning_message():
        assert True
        logger.info("********* Delete configuration details - Test Passed *********")
    else:
        take_screenshot(driver, ".\\screenshots\\", "test_delete_configuration_scr.png")
        logger.error("********* Delete configuration details - Test Failed *********")
        assert False
