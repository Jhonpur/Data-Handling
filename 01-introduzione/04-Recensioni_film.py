import pandas as pd

# 1. Creazione del DataFrame con le recensioni
print("=== CREAZIONE DATASET RECENSIONI ===")

# Simulo un dataset realistico con multiple recensioni per film
recensioni_data = {
    'ID Film': [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5],
    'Titolo Film': ['Titanic', 'Titanic', 'Titanic', 'Titanic', 
                    'Avatar', 'Avatar', 'Avatar',
                    'Inception', 'Inception', 'Inception', 'Inception', 'Inception',
                    'Interstellar', 'Interstellar',
                    'The Matrix', 'The Matrix', 'The Matrix', 'The Matrix', 'The Matrix'],
    'Punteggio': [5, 4, 5, 3, 4, 5, 4, 5, 5, 4, 5, 3, 4, 5, 5, 4, 5, 4, 3]
}

recensioni_film = pd.DataFrame(recensioni_data)

print("DataFrame RECENSIONI ORIGINALE:")
print(recensioni_film)
print(f"\nTotale recensioni nel dataset: {len(recensioni_film)}")
print()

# 3. AGGREGAZIONE CON GROUPBY
print("=== AGGREGAZIONI CON GROUPBY ===")

# Raggruppa per Titolo Film (o usare ID Film)
gruppi_film = recensioni_film.groupby('Titolo Film')

# a) Punteggio medio per ciascun film
print("1. PUNTEGGIO MEDIO per film:")
punteggio_medio = gruppi_film['Punteggio'].mean()
print(punteggio_medio.round(2))  # Arrotondato a 2 decimali
print()

# b) Numero totale di recensioni per ciascun film
print("2. NUMERO RECENSIONI per film:")
numero_recensioni = gruppi_film['Punteggio'].count()  # o .size()
print(numero_recensioni)
print()

# c) Punteggio massimo e minimo per ciascun film
print("3. PUNTEGGIO MASSIMO per film:")
punteggio_max = gruppi_film['Punteggio'].max()
print(punteggio_max)
print()

print("4. PUNTEGGIO MINIMO per film:")
punteggio_min = gruppi_film['Punteggio'].min()
print(punteggio_min)
print()

# 7. ESEMPIO CON GROUPBY SU ID FILM
print("=== GROUPBY SU ID FILM ===")
gruppi_per_id = recensioni_film.groupby('ID Film')
statistiche_per_id = gruppi_per_id.agg({
    'Titolo Film': 'first',  # Prendi il primo titolo (sono tutti uguali per ID)
    'Punteggio': ['mean', 'count', 'max', 'min']
})

print("Statistiche raggruppate per ID Film:")
print(statistiche_per_id)