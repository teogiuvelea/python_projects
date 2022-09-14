with open('records.csv') as f:
        data = f.readlines()
details = [item.strip("\n").split(',') for item in data]
print(details)
sold_tomatoes = sum([int(q[1]) for q in details if q[5] == 'seller' and q[0].lower() == 'tomatoes'])
sold_cucumbers = sum([int(q[1]) for q in details if q[5] == 'seller' and q[0].lower() == 'cucumbers'])
sold_long_pepers = sum([int(q[1]) for q in details if q[5] == 'seller' and q[0].lower() == 'long peppers'])
sold_red_bell_pepper = sum([int(q[1]) for q in details if q[5] == 'seller' and q[0].lower() == 'red bell peppers'])
print(sold_tomatoes)


