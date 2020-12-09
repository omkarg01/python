pizza='\nWhat toppings you want to add? '
pizza+="\nEnter 'quit' when done "
active = True
while active:
    a = input(pizza)
    if a == 'quit':
        break
    else:
        print(a.title() + ' is added.')

