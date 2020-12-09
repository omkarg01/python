import json

num = input('Enter your favorite number: ')
filename = 'fav_num.json'

with open(filename, 'w') as f:
    json.dump(num, f)

# import json
#
# filename = 'fav_num'
#
# with open(filename) as f:
#     a = json.load(f)
#
# print(a)