import re

def find_phone_number(text):
    phone_pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'

    match = re.search(phone_pattern, text)

    if match:
        return match.group()
    else:
        return None


input_text1 = "Please call me at 555-555-5555"
input_text2 = "Please call me at (555)-124-5563"
input_text3 = "Please call me at 91-1294-22131"

found_number = find_phone_number(input_text1)

if found_number:
    print("Found phone number:", found_number)
else:
    print("No valid phone number found.")

found_number = find_phone_number(input_text2)

if found_number:
    print("Found phone number:", found_number)
else:
    print("No valid phone number found.")

found_number = find_phone_number(input_text3)

if found_number:
    print("Found phone number:", found_number)
else:
    print("No valid phone number found.")


