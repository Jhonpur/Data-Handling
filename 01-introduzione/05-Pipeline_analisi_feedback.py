import pandas as pd
import numpy as np
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn import svm

def feedback():
    print("Acquisizione feedback in corso...")
    feedback = ["  AWESOME Event ! Very satisfying :)  ", 
                "I don't like this event very much... The WORST event Organization ever!", 
                "  Nothing out of ordinary.  ",
                " I love this content SO much!",
                "I don't want to partecipate anymore to this event! "]
    return pd.DataFrame(feedback, columns=['Feedback'])

def pulizia_feedback(df):
    # Rimuovere caratteri speciali, punteggiatura extra o spazi bianchi all'inizio/fine dei commenti
    # Convertire tutti i commenti in minuscolo per garantire uniformità
    print("Pulizia del testo")
    def clean(testo):
        testo = testo.strip().lower()   # strip rimuove gli spazi e lower mette tutto in minuscolo
        # espressioni regolari come nel modulo 4
        testo = re.sub(r'[^\w\s]', '', testo) # sostituisce la punteggiatura con '', quindi rimuovendolo
                                # prende solo le parole che hanno spazi e hanno caratteri letterari con \w
        return testo
    df['Clean'] = df['Feedback'].apply(clean)
    return df

def estrazione_parole_chiave(df):
    # Estrazione delle parole chiave (in questo caso, le parole più frequenti) versione semplice
    # parole_chiave = df['Clean'].str.split(expand=True).stack().value_counts()
    # return parole_chiave.head(5)  # Restituisco le prime 5 parole più frequenti
    

    #VERSIONE TFIDFVECTORIZER
    vectorizer = TfidfVectorizer(max_features = 5,
                                stop_words = ['this', 'to', 'dont', 'want', 'very', 'much', 'like', 'anymore'],
                                token_pattern = r'\b[a-zA-Z]{3,}\b',  # Almeno 3 lettere
                                )
    x = vectorizer.fit_transform(df['Clean'])
    parole_chiave = vectorizer.get_feature_names_out()

    # Calcola il conteggio delle parole selezionate da TF-IDF
    conteggi = {}
    for parola in parole_chiave:
        conteggi[parola] = df['Clean'].str.count(parola).sum()
    
    # Crea Series con parole e conteggi
    parole_con_conteggio = pd.Series(conteggi, name='conteggio')
    return parole_con_conteggio

#Preso da esempio modulo 5
def analisi_sentiment_generale(df):
    df_amazon = pd.read_csv('amazon-cells.txt', names = ['review', 'sentiment'], sep='\t')  

    reviews = df_amazon['review']
    sentiments = df_amazon['sentiment']

    reviews_train, reviews_test, sentiments_train, sentiments_test = train_test_split(reviews, sentiments, test_size=0.2, random_state=500)

    vectorizer = CountVectorizer()
    vectorizer.fit(reviews)
    X_train = vectorizer.transform(reviews_train)
    X_test = vectorizer.transform(reviews_test)

    classifier = LogisticRegression()
    #linear_classifier = LinearRegression()
    classifier.fit(X_train,sentiments_train)
    #linear_classifier.fit(X_train, sentiments_train)
    svm_classifier = svm.SVC()
    svm_classifier.fit(X_train,sentiments_train)


    #valutare l’accuratezza con cui il modello può fare previsioni su nuovi dati
    accuracy = classifier.score(X_test,sentiments_test)
    #linear_accuracy = linear_classifier.score(X_test, sentiments_test)
    svm_accuracy = svm_classifier.score(X_test,sentiments_test)
    print("Accuracy:",accuracy)
    #print("Linear accuracy:", linear_accuracy)
    print("Svm Accuracy:",svm_accuracy)

    X_new = vectorizer.transform(df['Clean'])
    predizione = classifier.predict(X_new)
    df['sentiment'] = predizione
    return df

def analisi_sentiment_medio(df):
    # Calcolo del sentiment medio
    sentiment_medio = df['sentiment'].mean()
    return sentiment_medio

def salvataggio_risultati(df, parole_chiave, sentiment_generale, sentiment_medio):
    print("Salvataggio dei risultati in corso...")
    # Salvo i risultati in un file CSV
    df.to_csv('feedback_pulito.csv', index=False)
    parole_chiave.to_csv('parole_chiave.csv')
    with open('analisi_sentiment.txt', 'w') as f:
        f.write(f"Sentiment Generale: {sentiment_generale}\n")
        f.write(f"Sentiment Medio: {sentiment_medio}\n")
    print("Risultati salvati con successo!")

# per eseguire il tutto
if __name__ == "__main__":
    df = feedback()
    df = pulizia_feedback(df)
    parole = estrazione_parole_chiave(df)
    sent_gen = analisi_sentiment_generale(df)
    sent_med = analisi_sentiment_medio(df)
    salvataggio_risultati(df, parole, sent_gen, sent_med)
    
    print(f"\nRisultati:")
    print(f"Sentiment Generale: {sent_gen}\n")
    print("Analisi del sentiment medio in corso...")
    print(f"Sentiment Medio: {sent_med}\n")
    print("Estrazione parole chiave in corso...")
    print(f"Parole più frequenti:\n{parole}")
