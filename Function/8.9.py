def print_models(unprinted_desings, completed_models):
    while unprinted_desings:
        current_design = unprinted_desings.pop()

        print('Printing models: ' +current_design.title())

        completed_models.append(current_design)

def show_completed_models(completed_models):
    print('\nFollowing models are printed: ')
    for i in completed_models:
        print(i.title())


unprinted_desings = ['iphone case','robot pendant','dodecahedron']
completed_models = []

print_models(unprinted_desings,completed_models)
show_completed_models(completed_models)

#unprinted_desings=completed_models[:]
print(unprinted_desings)



magician_names = ['bash','nknsjs','bjbjs']
def show_magician(magician_names):
    print('\n')
    for i in magician_names:
        print(i.title())
show_magician(magician_names)


