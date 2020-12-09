def sandwich(*items):
    print('List of the items that you want on sandwich: ')
    for item in items:
        print('\t-'+item)
#a = ('bhab','dbf')
sandwich('bhab','dbf')

def build_profile(first,last,**user_info):
    profile={}
    profile['first_name: ']=first
    profile['last_name: ']=last
    for key, value in user_info.items():
        profile[key]=value
    return profile
a = build_profile('omkar','gujja',location='mumbai',clg='VP')
print(a)
