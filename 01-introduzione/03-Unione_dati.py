import pandas as pd
import numpy as np

# 1. Creazione DataFrame CLIENTI
print("=== CREAZIONE DATAFRAMES ===")

clienti_data = {
    'ID Cliente': [1, 2, 3, 4],
    'Nome': ['Mario Rossi', 'Anna Verdi', 'Luca Bianchi', 'Sara Neri'],
    'Città': ['Roma', 'Milano', 'Napoli', 'Torino']
}

clienti = pd.DataFrame(clienti_data)
clienti = clienti.set_index('ID Cliente')  # ID Cliente come indice

print("DataFrame CLIENTI:")
print(clienti)
print()

# 2. Creazione DataFrame ORDINI
ordini_data = {
    'ID Ordine': [101, 102, 103, 104, 105],
    'ID Cliente': [1, 1, 2, 3, 999],  # Nota: 999 non esiste in clienti, 4 non ha ordini
    'Importo': [150.50, 89.20, 220.00, 67.80, 340.00]
}

ordini = pd.DataFrame(ordini_data)

print("DataFrame ORDINI:")
print(ordini)
print()

# INNER JOIN - Solo record che esistono in entrambe le tabelle
inner_join = pd.merge(clienti, ordini, left_index=True, right_on='ID Cliente', how='inner')
print(inner_join)
print(f"Risultato: {len(inner_join)} record (ordini con cliente valido)")
print()

# LEFT JOIN - Tutti i clienti + loro ordini (se esistono)
left_join = pd.merge(clienti, ordini, left_index=True, right_on='ID Cliente', how='left')
print(left_join)
print(f"Risultato: {len(left_join)} record (tutti i clienti)")
print("Nota: Sara Neri ha valori NaN perché non ha ordini")
print()

# RIGHT JOIN - Tutti gli ordini + dati cliente (se esistono)
right_join = pd.merge(clienti, ordini, left_index=True, right_on='ID Cliente', how='right')
print(right_join)
print(f"Risultato: {len(right_join)} record (tutti gli ordini)")
print("Nota: Ordine 105 (ID Cliente 999) ha valori NaN perché il cliente non esiste")
print()