# Name: Alexander Bowles
# Program: Regex Validator
# Description: Validates a phone number, Social Security number, and ZIP code using regular expressions.

import re


# Validate phone number
def validate_phone(phone):

    pattern = r'^\(?\d{3}\)?[- ]?\d{3}[- ]?\d{4}$'

    if re.match(pattern, phone):
        return True
    else:
        return False


# Validate Social Security Number
def validate_ssn(ssn):

    pattern = r'^\d{3}-\d{2}-\d{4}$'

    if re.match(pattern, ssn):
        return True
    else:
        return False


# Validate ZIP code
def validate_zip(zip_code):

    pattern = r'^\d{5}(-\d{4})?$'

    if re.match(pattern, zip_code):
        return True
    else:
        return False


# Main function
def main():

    phone = input("Enter a phone number: ")
    ssn = input("Enter a Social Security Number (XXX-XX-XXXX): ")
    zip_code = input("Enter a ZIP code: ")

    print("\nResults:")

    if validate_phone(phone):
        print("Phone number is valid")
    else:
        print("Phone number is invalid")

    if validate_ssn(ssn):
        print("SSN is valid")
    else:
        print("SSN is invalid")

    if validate_zip(zip_code):
        print("ZIP code is valid")
    else:
        print("ZIP code is invalid")


# Run program
if __name__ == "__main__":
    main()
