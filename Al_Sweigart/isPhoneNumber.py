import re
phoneNumR = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
message = 'Call me at 943-432-4243 anytime at 3:00'
print(phoneNumR.search(message))
