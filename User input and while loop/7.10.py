responses = {}
active = True
while active:
    name = input('\nWhat is your name? ').title()
    place = input('Which is your dream vacation place? ').title()

    responses[name] = place

    repeat = input('Would you like to let another person respond? (yes/no)')

    if repeat == 'no':
        active = False

print('\n'+'-'*3 +' Poll Result '+'-'*3)
for name, place in responses.items():
    print(name + ' would like to go to '+place+".")