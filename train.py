import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Sample training pipeline using TfidfVectorizer and LogisticRegression
def train_model():
    # Example dataset structure (Replace or extend with your dataset source)
    data = {
        'text': [
            "Official statement issued by government authorities regarding trade policy.",
            "Shocking secret revealed! Aliens land in city square overnight!",
            "Central bank announces updated interest rate guidelines for Q4.",
            "You won't believe this unbelievable daily miracle trick to double money!"
        ],
        'label': [1, 0, 1, 0] # 1: Real, 0: Fake
    }
    
    df = pd.DataFrame(data)
    
    vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
    X = vectorizer.fit_transform(df['text'])
    y = df['label']
    
    model = LogisticRegression()
    model.fit(X, y)
    
    # Save vectorizer and model
    joblib.dump(vectorizer, 'vectorizer.pkl')
    joblib.dump(model, 'model.pkl')
    print("Model and Vectorizer trained and saved successfully!")

if __name__ == '__main__':
    train_model()
