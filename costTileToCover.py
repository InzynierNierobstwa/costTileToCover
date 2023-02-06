materialArray = {'plytka lazienkowa': 250, 'plytka dekoracyjna': 400, 'plyta betonowa': 350, 'panel podlogowy': 150, 'podloga winylowa': 90}

def chooseMat():
    print(f'Wybierz material {materialArray.keys()}')
    material = ''

    while material not in materialArray.keys():
        material = input()

    return float(materialArray[material])

def tileArea():
    print('Podaj powierzchnie: ')
    areaX, areaY = input().split()
    return float(areaX), float(areaY)

def calcTileArea(areaX, areaY):
    areaM2 = areaX * areaY
    return areaM2

def calcTilePrice(areaM2, price):
    totalPrice = areaM2 * price
    return totalPrice

x, y = tileArea()
price = chooseMat()
area = calcTileArea(x, y)
totalPrice = calcTilePrice(area, price)

print(f'Powierzchnia pomieszczenia {x} na {y} wynosi {area}. Cena wybranego materialu to {price}.\nCena plytek dla tej powierzchni to {totalPrice}')



