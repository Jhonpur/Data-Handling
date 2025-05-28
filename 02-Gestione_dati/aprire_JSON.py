import json
path = "02-Gestione_dati/cars.json"
with open(path,'r') as f:
    data = json.load(f)
    for row in data['cars']:
        print(row)