from faker import Faker

class Invalid_Data:
    fake_email = Faker().email()
    fake_password = Faker().password()
    fake_name = Faker().name()
    first_name_1_char = 'Б'
    first_name_31_char = 'Борисборисборисборисборисборисб'
    last_name_1_char = 'Б'
    last_name_31_char = 'Бобосбобосбобосбобосбобосбобосб'
    password_21_char = 'Parol1111111111111111'
    password_no_Lower = 'Parol111'
    password_9_char = 'Parol1'
    password_not_contain_digit = "Parol"
    xss = '<script>alert(123)</script>'
    email_without_domain = 'test@.ru'
    invalid_phoneNumber = '+79876543321'

class Valid_Data:
    valid_first_name = 'Борис'
    valid_last_name = 'Бобос'
    valid_password = 'Parol111'
    valid_phoneNumber = '+79009009090'