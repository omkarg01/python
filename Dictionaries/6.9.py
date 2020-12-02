fav_places={'omkar':
    ['mumbai','japan','new york'],
            'shourya':
    ['america','australia','kashmir']
    }
for key,value in fav_places.items():
    print('\n'+key.title()+', your fav places are : ')
    for i in value:
        print('\t'+i.title())