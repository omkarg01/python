# filename = 'guest.txt'
#
# with open(filename, 'w') as fb:
#     a = input('Enter your name: ')
#     fb.write(a)
#     # fb.write('I love programming.\n')

# file = 'guest_book.txt'
# with open(file, 'w') as gb:
#
file = 'book.txt'
with open(file, 'w') as f:
    name = input("Enter your name : ")
    size = 10
    while size:
        f.write(name)
