"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('../data/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('../data/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
def find_telephone_number(calls):
    telephone_numbers = []

    for record in calls:
        if record[0] not in telephone_numbers:
            telephone_numbers.append(record[0])
        if record[1] not in telephone_numbers:
            telephone_numbers.append(record[1])

    return telephone_numbers

def calc_busiest_telephone_number(calls):
    telephone_numbers = find_telephone_number(calls)
    telephone_number_time = {}

    for telephone_number in telephone_numbers:
        telephone_number_time[telephone_number] = 0

    for record in calls:
        telephone_number_time[record[0]] += int(record[3])
        telephone_number_time[record[1]] += int(record[3])

    busiest_telephone_number = str()
    busiest_telephone_number_time = 0

    for telephone_number, time in telephone_number_time.items():
        if busiest_telephone_number_time < time:
            busiest_telephone_number = telephone_number
            busiest_telephone_number_time = time

    return busiest_telephone_number, busiest_telephone_number_time


busiest_telephone_number, busiest_telephone_number_time = calc_busiest_telephone_number(calls)
print("{} spent the longest time, {} seconds, on the phone during September 2016."
      .format(busiest_telephone_number, busiest_telephone_number_time))
