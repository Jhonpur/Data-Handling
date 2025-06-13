import pandas as pd
from geopy.distance import distance
from shapely.geometry import Point, Polygon

# Definizione dei due poligoni
coord_ovest = [(45.087431138440785, 7.651760766753362), (45.09623071049582, 7.657831250276273), (45.09514616189083, 7.671158204013811), (45.09056193206845, 7.669907888054073), (45.08251193328369, 7.666569904869294)]
coord_est = [(45.08283069707979, 7.667157139596527), (45.08983957943029, 7.677303546985579), (45.0952602245639, 7.672257766011785), (45.09196917994888, 7.693592644259675), (45.07699804808852, 7.683695783413152)]


poly_ovest = Polygon(coord_ovest)
poly_est = Polygon(coord_est)

# Definizione dei taxi
taxi1 = Point(45.088178826955584, 7.657606107328147)
taxi2 = Point(45.0891585599824, 7.669495328334604)
taxi3 = Point(45.08824519760572, 7.654126449604319)
taxi4 = Point(45.08473670758764, 7.66745310391404)
taxi5 = Point(45.087431138440785, 7.651760766753362)
taxi6 = Point(45.08726177890536, 7.67754221059107)
taxi7 = Point(45.08263682634163, 7.675584622952353)
taxi8 = Point(45.0933214948493, 7.678031607214152)

# Creazione del dizionario dei taxi
taxi = {
    'taxi1': taxi1,
    'taxi2': taxi2,
    'taxi3': taxi3,
    'taxi4': taxi4,
    'taxi5': taxi5,
    'taxi6': taxi6,
    'taxi7': taxi7,
    'taxi8': taxi8
}

# Punto di prelievo
pick_up = Point(45.09183288080605, 7.662181769671327)

# Associazione taxi ai poligoni
taxi_dict = {
    'ovest': [],
    'est': []
}


for name, point in taxi.items():
    if point.within(poly_ovest):
        taxi_dict['ovest'].append((name, point))
    elif point.within(poly_est):
        taxi_dict['est'].append((name, point))

# Verifica in quale poligono si trova il punto di prelievo
if pick_up.within(poly_ovest):
    zona = 'ovest'
elif pick_up.within(poly_est):
    zona = 'est'
else:
    zona = None

# Calcolo distanza solo se il punto è in un poligono valido
if zona:
    print(f"\nIl punto di prelievo si trova nella zona: {zona}")
    min_dist = float('inf')
    closest_taxi = None

    for name, point in taxi_dict[zona]:
        dist = distance((pick_up.y, pick_up.x), (point.y, point.x)).m
        print(f"{name} distanza: {round(dist)} m")
        if dist < min_dist:
            min_dist = dist
            closest_taxi = name

    print(f"\nIl taxi più vicino è: {closest_taxi} a {round(min_dist)} metri")

else:
    print("Il punto di prelievo non si trova in nessun poligono definito.")
