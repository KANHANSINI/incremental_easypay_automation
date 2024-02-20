class CreateNewGuestTestData:
    first_name = "Emily"
    last_name = "Johnson"
    email = "emily.johnson@example.com"
    phone_number = "0011225544"
    address_line_1 = "123 Main Street"
    address_line_2 = "United States"
    zip_code = "2001100"


class CreateNewGuestTestData_NegativeTesting:
    phone_number = "0000000000000000000000000000000000000000000000000000000000000000000000000000"
    address_line_1 = "11111111111111111111111111111111111111111111111111111111111111111111111111"
    address_line_2 = "22222222222222222222222222222222222222222222222222222222222222222222222222"
