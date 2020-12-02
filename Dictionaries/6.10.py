ppl_fav_num={
    'omkar':[15,24,86],
    'shourya':[9,68,17],
    'manan':[52,36,79],
    'vaya':[60,47,29]
}
for key, value in ppl_fav_num.items():
    print("\n"+key.title()+"'s fav number are:")
    for i in value:
        print('\t'+str(i))

