magician_names = ['bash','nknsjs','bjbjs']


def show_magician():
    for i in magician_names:
        print(i.title())

(show_magician())

def make_great():
    a = magician_names[:]
    for i in a:
        print('The Great '+i.title())


make_great()






