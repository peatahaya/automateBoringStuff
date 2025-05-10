myCat = {'size': 'fat', 
         'color': 'gray', 
         'disposition': 'loud'}

print(myCat['size'])

for v in myCat.values():
    print(v)

for v, k in myCat.items():
    print(f'{v}, {k}')