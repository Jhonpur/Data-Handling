'''Esercizio: Combinare intervalli in una fetta “Other”
Osservando il grafico della Figura 8-7, si può notare che alcuni intervalli sono rappresentati
da una fetta molto sottile della torta. Questi sono gli intervalli con un numero di dipendenti
pari a uno o due. Modificate il grafico in modo che questi intervalli siano uniti in un’unica
fetta etichettata Other. A tal fine, è necessario modificare l’array count e la lista labels.
Quindi, si deve ricreare il grafico.'''
import numpy as  np
from matplotlib import pyplot as plt
import pandas as pd
salaries = [1215, 1221, 1263, 1267, 1271, 1274, 1275, 1318, 1320, 1324, 1324, 1326, 1337, 1346, 1354, 1355, 1364, 1367,
            1372, 1375, 1376, 1378, 1378, 1410, 1415, 1415, 1418, 1420, 1422, 1426, 1430, 1434, 1437, 1451, 1454, 1467,
            1470, 1473, 1477, 1479,1480, 1514, 1516, 1522, 1529, 1544, 1547, 1554, 1562, 1584, 1595, 1616, 1626, 1717]

count, labels = np.histogram(salaries, bins=np.arange(1100, 1900, 50))

labels = ['$'+str(labels[i])+'-'+str(labels[i+1]) for i, _ in enumerate(labels[1:])]
non_zero_pos = [i for i, x in enumerate(count) if x != 0]

labels = [e for i, e in enumerate(labels) if i in non_zero_pos]
count = [e for i, e in enumerate(count) if i in non_zero_pos]

df = pd.DataFrame({'Label': labels, 'Count': count})

df_free = df.copy()
df_free.loc[df_free['Count'] < 3, 'Label'] = 'Other'
df_free = df_free.groupby('Label')['Count'].sum().reset_index()

#TORTA CON UNIFICAZIONE CON SALARIO SIMILE DI MAX 3 PERSONE 
plt.pie(df_free['Count'], labels=df_free['Label'], autopct='%1.1f%%')
plt.title('Monthly Salaries in the Sales Department')
plt.show()

'''TORTA SENZA UNIFICAZIONE
plt.pie(count, labels=labels, autopct='%1.1f%%')
plt.title('Monthly Salaries in the Sales Department')
plt.show()
'''