qereal_estate = dict()
slot = 1
while slot > 0:
    house = dict()
    name = input("name of the house:")
    category = input("category:")
    price = float(input("price:"))
    locatoin = input("locatoin:")
    color = input("color painting:")
    owner = input("landlord:")
    broker = input(" broker:")


    house['name'] = name
    house['category'] = category
    house['price'] = price
    house['locatoin'] = locatoin
    house['color'] = color
    house['owner'] = owner
    house['broker'] = broker 
    slot = slot-1
    real_estate[f'{name}']= house.items()
for key, value in real_estate.items():
    for k,v in value: 
        print({key:{k:v}})
    
