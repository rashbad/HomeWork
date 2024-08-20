my_dict = {'Rashad': 1996, 'Kamil': 1995}
print(my_dict)
my_dict['Ismail'] = 1993
print(my_dict['Rashad'], my_dict['Ismail'])
my_dict.update({'Alex': 1990,
                'Oleg': 1991})
print(my_dict)
my_dict.pop('Rashad')
print(my_dict)
my_set = { 1,2,3,4,5,1,2,3,4, 'ololo', False, (1,2,3,4,5)}
print(my_set)
my_set.update({6,7,8,
               'prizme'})
my_set.discard(1)
print(my_set)
