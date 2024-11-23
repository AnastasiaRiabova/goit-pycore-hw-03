import re


def normalize_phone(phone_number):
    clean_number = re.sub(r'[^\d+]', '', phone_number.strip())

    if clean_number.startswith('+380'):
        return clean_number

    if clean_number.startswith('380'):
        return f'+{clean_number}'

    if clean_number.startswith('0') or clean_number.isdigit():
        return f'+38{clean_number}'

    if clean_number.startswith('+'):
        return clean_number

    return ''


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Normalized phone numbers are:", sanitized_numbers)
