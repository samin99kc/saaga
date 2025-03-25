from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, accuracy_score, f1_score
import pandas as pd

# ✅ Use raw string to fix Windows path issues
file_path = r"C:\Users\samin\Desktop\ir-assignment\classification\classification.csv"

# Load dataset
df = pd.read_csv(file_path, encoding='ISO-8859-1')

# Step 1: Split data
X = df["Text"]
y = df["label"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 2: Create pipeline with TF-IDF + Naive Bayes
model = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english')),
    ('clf', MultinomialNB())
])

# Step 3: Train the model
model.fit(X_train, y_train)

# Step 4: Evaluate the model
y_pred = model.predict(X_test)

# Show metrics
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average='weighted')  

print(" Classification Report:")
print(classification_report(y_test, y_pred))
print(f"Accuracy: {accuracy * 100:.2f}%")
print(f"F1 Score: {f1:.2f}")

# Step 5: Classify new input
def classify_new_text(text):
    prediction = model.predict([text])[0]
    return prediction

