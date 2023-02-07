#(694)544-2366, (420)   647-3944, ( 321) 1526278, (776) 949-8387, 351588-8871
import re

numbers = ["(694)544-2366", "(420)   647-3944", "( 321) 1526278", "(776) 949-8387", "351588-8871"]
for x in numbers:
    new_number = re.sub(r"[\([{})\]]", "", x)
    new_number2 = new_number.replace("-", "")
    new_number3 = new_number2.replace(" ", "")
    phone_numbers = new_number3
    print("(" + phone_numbers[0:3] + ")" + " " + phone_numbers[3:6] + "-" + phone_numbers[6:10])


