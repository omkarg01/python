# import json
#
# filename = 'numbers.json'
#
# with open(filename) as f_obj:
#     num = json.load(f_obj)

# print(num)
#
# import json
# filename = 'username.json'
#
# with open(filename) as f_obj:
#     username

import json

filename = 'fav_num.json'

with open(filename) as f:
    a = json.load(f)

print(a)