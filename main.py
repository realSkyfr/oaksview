# oaks crim code viewer
import json

with open('header.json', 'r') as crimcode: 
    data = crimcode.read()
    code = json.loads(data)

print("All caps, format like I-A-1, press [CTRL]+[C] to quit.")

while True:
    toLook = input("What code would you like to view?\n")
    try:
        print(code[toLook]['Discription'])

    except:
        print("Invalid code! Make sure it is all capital and formatted like this: I-A-1")
        continue
