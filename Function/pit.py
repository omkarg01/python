def car_info(manufacturer, model_name, **info):
    make_cae={}
    make_cae['manufacturer']=manufacturer
    make_cae['model_name']=model_name
    for key,value in info.items():
        make_cae[key]=value
    print(make_cae)
#car = car_info('bmw','i series',color='blue',seats='4')
#print(car)
#for i,k in car.items():
 #   print(i+': '+k.title())