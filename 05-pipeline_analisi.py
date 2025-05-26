import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression         #addestriamo classificatore per prevedere il sentiment di una recensione

if __name__ == "__main__":
    df = pd.read_csv('amazon-cells.txt', names = ['review', 'sentiment'], sep='\t')  

    reviews = df['review']
    sentiments = df['sentiment']

    reveiws_train, reviews_test, sentiments_train, sentiments_test = train_test_split(reviews, sentiments, test_size=0.2, random_state=500)

    vectorizer = CountVectorizer()
    vectorizer.fit(reviews)
    X_train = vectorizer.transform(reveiws_train)
    X_test = vectorizer.transform(reviews_test)

    classifier = LogisticRegression()
    classifier.fit(X_train,sentiments_train)

    #valutare l’accuratezza con cui il modello può fare previsioni su nuovi dati
    accuracy = classifier.score(X_test,sentiments_test)
    print("Accuracy:",accuracy)

    new_reviews = ['Old version of python useless', 'Very good effort, but not five stars', 'Clear and concise']
    X_new = vectorizer.transform(new_reviews)
    print(classifier.predict(X_new))