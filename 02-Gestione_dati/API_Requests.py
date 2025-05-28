'''Come urllib3, la libreria Requests può interagire con le API HTTP. Provate a riscrivere il
codice che invia una richiesta GET all’API News in modo che utilizzi la libreria Requests al
posto di urllib3. Si noti che con Requests non è necessario aggiungere manualmente i parametri
di query all’URL passato. Si possono invece passare i parametri come un dizionario
di stringhe.'''

import requests
PARAMS = {'news':'', 'format':'json'}
r = requests.get('https://newsapi.org/v2/everything? q=Python programming language& apiKey=your_api_key_here& pageSize=5', params=PARAMS)
for article in r['articles']:
    print(article['title'])
    print(article['publishedAt'])
    print(article['url'])
    print()