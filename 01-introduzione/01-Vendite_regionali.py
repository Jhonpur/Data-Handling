# Analisi di dati di vendita regionali con NumPy
import numpy as np

vendite_regionali = np.array([
    [100, 120, 110, 130],  # Nord: vendite nei 4 trimestri
    [80, 90, 85, 95],      # Centro: vendite nei 4 trimestri  
    [70, 75, 80, 85]       # Sud: vendite nei 4 trimestri
])

vendite_totali = np.sum(vendite_regionali, axis=1)

trimestre_migliore = np.argmax(vendite_regionali, axis=1)

trimestre_peggiore = np.amin(vendite_regionali, axis=1)

vendite_medie = np.mean(vendite_regionali, axis=0)

print("Vendite totali per regione:", vendite_totali)
print("Trimestre migliore per regione:", trimestre_migliore)
print("Trimestre peggiore per regione:", trimestre_peggiore)
print(f"Vendite medie per regione: {vendite_medie[0]:.1f}")


print("Array vendite regionali:")
print(vendite_regionali)
print()

# 1. Vendite totali per ogni regione nell'anno (somma lungo l'asse 1 - trimestri)
vendite_totali_regione = np.sum(vendite_regionali, axis=1)
print("1. Vendite totali per regione nell'anno:")
print(f"   Nord: {vendite_totali_regione[0]}")
print(f"   Centro: {vendite_totali_regione[1]}")
print(f"   Sud: {vendite_totali_regione[2]}")
print()

# 2. Trimestre con vendite massime per ogni regione (indice del trimestre)
trimestre_max_per_regione = np.argmax(vendite_regionali, axis=1)
valori_max_per_regione = np.amax(vendite_regionali, axis=1)
print("2. Trimestre con vendite massime per regione:")
print(f"   Nord: Trimestre {trimestre_max_per_regione[0]+1} (valore: {valori_max_per_regione[0]})")
print(f"   Centro: Trimestre {trimestre_max_per_regione[1]+1} (valore: {valori_max_per_regione[1]})")
print(f"   Sud: Trimestre {trimestre_max_per_regione[2]+1} (valore: {valori_max_per_regione[2]})")
print()

# 3. Vendite medie per trimestre a livello complessivo (media lungo l'asse 0 - regioni)
vendite_medie_trimestre = np.mean(vendite_regionali, axis=0)
print("3. Vendite medie per trimestre (tutte le regioni):")
print(f"   T1: {vendite_medie_trimestre[0]:.1f}")
print(f"   T2: {vendite_medie_trimestre[1]:.1f}")
print(f"   T3: {vendite_medie_trimestre[2]:.1f}")
print(f"   T4: {vendite_medie_trimestre[3]:.1f}")
print()

# 4. Vendite minime registrate in qualsiasi trimestre e regione
vendite_minime_assolute = np.amin(vendite_regionali)
print("4. Vendite minime assolute:")
print(f"   Valore minimo: {vendite_minime_assolute}")

# Informazioni aggiuntive per completezza
print("\n--- Informazioni aggiuntive ---")
print(f"Vendite massime assolute: {np.amax(vendite_regionali)}")
print(f"Media generale: {np.mean(vendite_regionali):.1f}")
print(f"Deviazione standard: {np.std(vendite_regionali):.1f}")