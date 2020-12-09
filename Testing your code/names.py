from name_function import get_formatted_name
print("Enter 'q' at any time to quit.")
while True:
    first = input('\nplease give me a first name: ')
    if first == 'q':
        break

    last = input('give your last name: ')
    if last == 'q':
        break

    middle = input('middle name if any: ')
    if middle == 'q'

    formatted_name = get_formatted_name(first, last, middle = '')
    print('\tNeatly formatted name: ' + formatted_name + '.')
