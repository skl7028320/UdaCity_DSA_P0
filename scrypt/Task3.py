"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('../data/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('../data/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

"""
Part A
"""
def is_number_from_bangalore(number):
    area_code = "(080)"
    if area_code in number:
        return True
    else:
        return False

def is_number_mobile(number):
    if " " in number:
        return True
    else:
        return False

def is_number_fixed(number):
    if "(" in number:
        return True
    else:
        return False

def find_codes_and_prefixes_called_from_bangalore(calls):
    codes = []
    prefixes = []
    for record in calls:
        if is_number_from_bangalore(record[0]):
            if is_number_mobile(record[1]) and record[1][0:4] not in prefixes:
                prefixes.append(record[1][0:4])
            elif is_number_fixed(record[1]) and record[1][record[1].find("("):record[1].find(")") + 1] not in codes:
                codes.append(record[1][record[1].find("("):record[1].find(")") + 1])

    return codes, prefixes


codes, prefixes = find_codes_and_prefixes_called_from_bangalore(calls)
sorted_codes = sorted(codes)
sorted_prefixes = sorted(prefixes)

print("The numbers called by people in Bangalore have codes:")
print(sorted_codes)
print("The numbers called by people in Bangalore have prefixes:")
print(sorted_prefixes)

"""
Part B
"""
def is_call_from_bangalore(call):
    if "(080)" in call[0]:
        return True
    else:
        return False

def is_call_to_bangalore(call):
    if "(080)" in call[1]:
        return True
    else:
        return False

def calc_percentage(calls):
    from_bangalore_call_number = 0
    from_bangalore_to_bangalore_call_number = 0

    for call in calls:
        if is_call_from_bangalore(call):
            from_bangalore_call_number += 1
            if is_call_to_bangalore(call):
                from_bangalore_to_bangalore_call_number += 1

    return float(from_bangalore_to_bangalore_call_number) / from_bangalore_call_number


print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines "
      "in Bangalore.".format(round(calc_percentage(calls) * 100)))
