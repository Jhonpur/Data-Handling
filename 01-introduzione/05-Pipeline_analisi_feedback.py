import pandas as pd
import re

def feedback():
    print("Acquisizione feedback in corso...")
    feedback = ["  Evento FANTASTICO!!! Molto soddisfatto :)  ", 
                "Non mi è piaciuto per niente... Organizzazione PESSIMA!", 
                "  Nella norma, niente di speciale.  "]
    return pd.DataFrame(feedback, columns=['Feedback'])

def pulizia_feedback(df):
    print("Pulizia feedback in corso...")
    # Rimuovo gli spazi bianchi all'inizio e alla fine, li converto in minuscolo
    df['Feedback'] = df['Feedback'].str.strip().str.lower()
    # Rimuovo i caratteri speciali
    df['Feedback'] = df['Feedback'].apply(lambda x: re.sub(r'[^a-zA-ZÀ-ÿ0-9\s]', '', x))
# da togliere
    print("Feedback dopo pulizia:")
    for i, feedback in enumerate(df['Feedback']):
        print(f"{i+1}: '{feedback}'")
    print()

    return df

def estrazione_parole_chiave(df):
    print("Estrazione parole chiave in corso...")
    # Estrazione delle parole chiave (in questo caso, le parole più frequenti)
    parole_chiave = df['Feedback'].str.split(expand=True).stack().value_counts()
    return parole_chiave.head(5)  # Restituisco le prime 5 parole più frequenti

def analisi_sentiment_generale(df):
    print("Analisi del sentiment generale in corso...")
# da togliere
    for i, feedback in enumerate(df['Feedback']):
        if 'fantastico' in feedback or 'soddisfatto' in feedback:
            print(f"Feedback {i+1} POSITIVO: '{feedback}'")
        elif 'pessima' in feedback or 'non mi e piaciuto' in feedback:
            print(f"Feedback {i+1} NEGATIVO: '{feedback}'")
        else:
            print(f"Feedback {i+1} NEUTRO: '{feedback}'")


    sentiment_generale = df['Feedback'].apply(lambda x: 1 if 'fantastico' in x or 'soddisfatto' in x else 
                                               (-1 if 'pessima' in x or 'non mi e piaciuto' in x else 0)).sum()
    return sentiment_generale

def analisi_sentiment_medio(df):
    print("Analisi del sentiment medio in corso...")
    # Calcolo del sentiment medio
    sentiment_medio = df['Feedback'].apply(lambda x: 1 if 'fantastico' in x or 'soddisfatto' in x else 
                                            (-1 if 'pessimo' in x or 'pessima' in x or 'non mi è piaciuto' in x else 0)).mean()
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
    print(f"Sentiment Generale: {sent_gen}")
    print(f"Sentiment Medio: {sent_med}")
    print(f"Parole più frequenti:\n{parole}")
