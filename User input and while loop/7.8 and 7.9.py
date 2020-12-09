sandwich_order = ['noodle sandwich','pastrami sandwich','tomato sandwich','toast sandwich','pastrami sandwich','pastrami sandwich']
finished_sandwiches = []
print('We are run out of pastrami sandwich.\n')
while 'pastrami sandwich' in sandwich_order:
    sandwich_order.remove('pastrami sandwich')
while sandwich_order:
    a = sandwich_order.pop()
    print('Your '+a.title()+' is ready.')
    finished_sandwiches.append(a)
print('\nFollowing are the list of sandwiches you have ate: ')
for finished_sandwich in finished_sandwiches:
    print('\t'+ finished_sandwich.title())

