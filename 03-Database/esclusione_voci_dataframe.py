#ESERCIZIO 10 PAG 47
import pandas as pd

orders = [
(9423517, '2022-02-04', 9001),
(4626232, '2022-02-04', 9003),
(9423534, '2022-02-04', 9001),
(9423679, '2022-02-05', 9002),
(4626377, '2022-02-05', 9003),
(4626412, '2022-02-05', 9004),
(9423783, '2022-02-06', 9002),
(4626490, '2022-02-06', 9004)
]
df_orders = pd.DataFrame(orders, columns =['OrderNo', 'Date', 'Empno'])

details = [
(9423517, 'Jeans', 'Rip Curl', 87.0, 1),
(9423517, 'Jacket', 'The North Face', 112.0, 1),
(4626232, 'Socks', 'Vans', 15.0, 1),
(4626232, 'Jeans', 'Quiksilver', 82.0, 1),
(9423534, 'Socks', 'DC', 10.0, 2),
(9423534, 'Socks', 'Quiksilver', 12.0, 2),
(9423679, 'T-shirt', 'Patagonia', 35.0, 1),
(4626377, 'Hoody', 'Animal', 44.0, 1),
(4626377, 'Cargo Shorts', 'Animal', 38.0, 1),
(4626412, 'Shirt', 'Volcom', 78.0, 1),
(9423783, 'Boxer Shorts', 'Superdry', 30.0, 2),
(9423783, 'Shorts', 'Globe', 26.0, 1),
(4626490, 'Cargo Shorts', 'Billabong', 54.0, 1),
(4626490, 'Sweater', 'Dickies', 56.0, 1)
]
df_details = pd.DataFrame(details, columns =['OrderNo', 'Item', 'Brand', 'Price', 'Quantity'])

emps = [
(9001, 'Jeff Russell', 'LA'),
(9002, 'Jane Boorman', 'San Francisco'),
(9003, 'Tom Heints', 'NYC'),
(9004, 'Maya Silver', 'Philadelphia')
]
df_emps = pd.DataFrame(emps, columns =['Empno', 'Empname', 'Location'])

locations = [
('LA', 'West'),
('San Francisco', 'West'),
('NYC', 'East'),
('Philadelphia', 'East')
]
df_locations = pd.DataFrame(locations, columns =['Location', 'Region'])

#COMBINARE DATAFRAME
df_sales = df_orders.merge(df_details)
#print(df_sales)

df_sales['Total'] = df_sales['Price'] * df_sales['Quantity']
df_sales = df_sales[['Date','Empno','Total']]

df_sales_emps = df_sales.merge(df_emps)
df_result = df_sales_emps.merge(df_locations)


#print("df_result prima del groupby:")
#print(df_result)
#print("\nShape di df_result:", df_result.shape)



df_result = df_result[['Date','Empno','Empname', 'Location', 'Region','Total']]
#print(df_result)

df_date_region = df_result.groupby(['Date','Region'])[['Total']].sum()
print("DataFrame base aggregato:")
print(df_date_region)

ps = df_date_region.sum(axis = 0)
#print(ps)
ps.name=('All','All')
ps_df = ps.to_frame().T  # Trasforma la serie in DataFrame con una riga
df_date_region_total = pd.concat([df_date_region, ps_df])

df_totals = pd.DataFrame()
for date, date_df in df_date_region.groupby(level=0):
    df_totals = pd.concat([df_totals, date_df])

    ps = date_df.sum(axis = 0)
    ps.name=(date,'All')
    # Convertire la serie in DataFrame prima di concatenare
    ps_df = ps.to_frame().T
    df_totals = pd.concat([df_totals, ps_df])

#aggiungere riga del totale al dataframe
total_row = df_date_region_total.loc[('All','All'):('All','All')]
df_totals = pd.concat([df_totals, total_row])
print("\nDataFrame con totali e subtotali:")
print(df_totals)

df_filtered = df_totals[df_totals.index.get_level_values(1) != 'All']

print("\nDataFrame filtrato (senza totali e subtotali):")
print(df_filtered)