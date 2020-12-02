cities={
    'mumbai':{
        'country':'inida',
        'population':'2 crore',

    },
    'tokyo':{
        'country':'japan',
        'population':'92 lakh'
    },

    'new york':{
        'country':'usa',
        'population':'84 lakh'
    }
}

for key,value in cities.items():
    print('City Name : '+key.upper())
    if key =='new york':
        print('\t' + key.title() + ' city is from ' + value['country'].upper() + ', it has a population over ' + value[
            'population'].title() + '\n')
    else:
        print('\t'+key.title()+' city is from '+value['country'].title()+', it has a over '+value['population'].title()+'\n')
