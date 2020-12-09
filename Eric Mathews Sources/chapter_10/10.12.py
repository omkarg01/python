import json

def ask_fav_num():
    # filename = 'favorite_num'
    ask = input('What is your favorite number: ')
    filename = 'favorite.json'

    with open(filename, 'w') as fn:
        json.dump(ask, fn)
    return ask

def show_fav_num():

    filename = 'favorite.json'
    try:
        with open(filename) as fn:
            json.load(fn)
    except FileNotFoundError:
        return None
    else:
        return filename

def fav_num():
    filename = show_fav_num()
    if filename:
        print(f'Your fav num is: {filename}.')
    else:
        filename = ask_fav_num()
        print(f"We'll remember your fav num, {filename}")

fav_num()
