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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
def count_telephone_number(texts, calls):
    telephone_numbers = []
    count = 0

    for record in texts:
        if record[0] not in telephone_numbers:
            telephone_numbers.append(record[0])
            count += 1
        if record[1] not in telephone_numbers:
            telephone_numbers.append(record[1])
            count += 1

    for record in calls:
        if record[0] not in telephone_numbers:
            telephone_numbers.append(record[0])
            count += 1
        if record[1] not in telephone_numbers:
            telephone_numbers.append(record[1])
            count += 1

    return count


print("There are {} different telephone numbers in the records.".format(count_telephone_number(texts, calls)))
