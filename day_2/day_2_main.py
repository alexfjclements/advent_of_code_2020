from day_2.day_2_data import formatted_data


# return number of validated passwords
def password_checker(input_data, section_one=True):

    valid_number = 0
    for password in input_data:
        if section_one:
            if validity_check(password):
                valid_number += 1
        else:
            if updated_validity_check(password):
                valid_number += 1

    return valid_number


# all passwords and conditions presented in the same format. Use these to extract the required information to
# conduct the test.
def validity_check(password_details):
    first_split = password_details.split('-', 1)
    min_no = int(first_split[0])

    second_split = first_split[1].split(' ', 1)
    max_no = int(second_split[0])

    third_split = second_split[1].split(':', 1)
    letter = third_split[0]

    password = third_split[1].split(' ')[1]

    letter_count = password.count(letter)

    if min_no <= letter_count <= max_no:
        return True
    else:
        return False


def updated_validity_check(password_details):
    first_split = password_details.split('-', 1)
    pos_one = int(first_split[0]) - 1

    second_split = first_split[1].split(' ', 1)
    pos_two = int(second_split[0]) - 1

    third_split = second_split[1].split(':', 1)
    letter = third_split[0]

    password = third_split[1].split(' ')[1]

    if password[pos_one] == letter or password[pos_two] == letter:
        if not password[pos_one] == password[pos_two]:
            return True
        else:
            return False
    else:
        return False


print(password_checker(formatted_data, False))
