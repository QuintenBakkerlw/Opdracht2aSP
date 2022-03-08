from pprint import pprint
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false')
db = client.spDatabase



"Wat is de naam en prijs van het eerste product in de database?"
eerste_product = db.product.find()[0]
name = eerste_product['name']
selling_price = (eerste_product['price']['selling_price'])
pprint(f"{name}\n{selling_price}")


"Geef de naam van het eerste product waarvan de naam begint met een 'R'?"

R = False
x = 0
### while loop zodat het herhaalt totdat die de juist antwoordt heeft gevonden ###
while R == False:

    ### kijkt naar elke product naam ###
    check = db.product.find()[x]
    name = check["name"]

    ### kijkt of de eerste letter een R is ###
    if name[0] == "R":
        R = True
        print(f'found it\n {name}')
    else:
        x += 1


"Wat is de gemiddelde prijs van de producten in de database?"
lst = []
### pakt van elke product de prijs ###
for x in range(0, 1000):
    product = db.product.find()[x]
    price = (product['price']['selling_price'])

    ### voegt de prijs toe aan lst, berekent daarna de gemiddelde van het lst ###
    lst.append(price)

gemiddelde = int(sum(lst)/(len(lst)))
print(f"het gemiddelde prijs = {gemiddelde}")






