import pandas as pd

nomi_prodotti = ['Prodotto A', 'Prodotto B', 'Prodotto C']
codici_prodotti = ['A001', 'B002', 'C003']
quantita_prodotti = [10, 20, 30]

prodotti = pd.Series(nomi_prodotti, index=codici_prodotti)
codici = pd.Series(codici_prodotti, index=codici_prodotti)
quantità = pd.Series(quantita_prodotti, index=codici_prodotti)

inventario_prodotti = pd.concat([prodotti, codici, quantità], axis=1)
print("DataFrame iniziale:")
print(inventario_prodotti)

# accedi e stampa la quantità disponibile del Prodotto A
quantita_prodotto_a = inventario_prodotti.loc['A001', 2]
print(f"\nQuantità disponibile del Prodotto A: {quantita_prodotto_a}")