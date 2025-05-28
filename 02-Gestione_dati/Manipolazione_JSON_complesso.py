'''MANIPOLARE STRUTTURE JSON COMPLESSE'''
import pandas as pd
import json

data = [{"Emp":"Jeff Russell",
         "Emp_email":"jeff.russell",
         "POs":[{"Pono":2608,"Total":35},
                {"Pono":2617,"Total":35},
                {"Pono":2620,"Total":139}
                ]},
        {"Emp":"Jane Boorman",
         "Emp_email":"jane.boorman",
         "POs":[{"Pono":2621,"Total":95},
                {"Pono":2626,"Total":218}
                ]
            }]

df = pd.json_normalize(data, "POs", ["Emp", "Emp_email"]).set_index(["Emp","Emp_email","Pono"])

df = df.reset_index() #ELIMINIAMO INDICE A 2 COLONNE, COSì RENDIAMO EMP E PONO COLONNE
json_doc = ( df.groupby(['Emp','Emp_email'], as_index=True) #RAGGRUPPIAMO LE RIGHE IN BASE ALLA COLONNA EMP
.apply(lambda x: x[['Pono','Total']].to_dict('records'), include_groups=False) #apply APPLICA FUNZIONE LAMBDA A OGNI RECORD, CHE SPECIFICA QUALI QUALI CAMPI VISUALIZZARE IN UNA RIGA
.reset_index() #CONVERTIAMO LA Series IN UN DataFrame, e converte pure EMP DA INDICE A COLONNA REGOLARE
.rename(columns={0:'POs'}) #IMPOSTIAMO NOME COLONNA
.to_json(orient='records')) #TRASFORMIAMO IL DataFrame in JSON

#Per migliorare la leggibilità, è possibile stamparla con il seguente comando:
print(json.dumps(json.loads(json_doc), indent=2))
#print(df)
