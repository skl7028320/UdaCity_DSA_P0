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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
def find_telemarketers(texts, calls):
    telemarketers = []
    for call in calls:
        if call[0] not in telemarketers:
            telemarketers.append(call[0])

    for call in calls:
        if call[1] in telemarketers:
            del telemarketers[telemarketers.index(call[1])]

    for text in texts:
        if text[0] in telemarketers:
            del telemarketers[telemarketers.index(text[0])]
        if text[1] in telemarketers:
            del telemarketers[telemarketers.index(text[1])]

    return telemarketers


print("These numbers could be telemarketers: ")
telemarketers = find_telemarketers(texts, calls)
telemarketers.sort()
print(telemarketers)
