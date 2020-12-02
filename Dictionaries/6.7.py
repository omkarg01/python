p1={'first_name':'omkar','last_name':'gujja','location':'mumbai1'}
p2={'first_name':'shourya','last_name':'vannam','location':'mumbai2'}
people=[p1,p2]
for i in people:
    for key,value in i.items():
        print(key.title()+' : '+value.title())
    print()

