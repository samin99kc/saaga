import pandas as pd
import numpy as np
import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score, classification_report

# Expanded dataset with 100 different text samples
news_sources = {
    "Politics": [
        "The president announced a new economic policy today",
        "Senators debated the new healthcare bill in Congress",
        "A new law has been passed to regulate election funding",
        "The opposition party criticized the government's tax reforms",
        "World leaders met at the UN summit to discuss global trade",
        "A new immigration policy was introduced by the administration",
        "The government is planning to increase defense budget",
        "The prime minister visited flood-hit areas to assess damage",
        "A new treaty was signed between neighboring countries",
        "Protests erupted over the recent government decision"
    ],
    "Business": [
        "Apple launched its latest iPhone model this week",
        "Stock market experiences sharp decline due to economic slowdown",
        "A startup raised $10 million in funding to expand globally",
        "The Federal Reserve announced a hike in interest rates",
        "Retail stores report increased sales during holiday season",
        "Amazon and Walmart compete for dominance in the e-commerce market",
        "The automotive industry is facing supply chain disruptions",
        "Oil prices have surged due to global conflicts",
        "A major airline filed for bankruptcy amid economic downturn",
        "Cryptocurrency markets are experiencing extreme volatility"
    ],
    "Health": [
        "New research suggests a link between diet and mental health",
        "Doctors recommend regular exercise to prevent heart disease",
        "The latest flu strain has led to an increase in hospitalizations",
        "A new vaccine for malaria has been approved for distribution",
        "Mental health awareness campaigns are gaining traction worldwide",
        "Experts warn against the overuse of antibiotics and resistance risks",
        "Obesity rates are increasing due to unhealthy diets",
        "Researchers discover a potential cure for Alzheimer's disease",
        "Hospitals are facing staff shortages amid rising cases",
        "Government launches a new initiative to promote healthy eating"
    ]
}

# Expanding the dataset to 100 unique entries
data = [(text, category) for category, texts in news_sources.items() for text in texts] * 10

df = pd.DataFrame(data[:100], columns=["text", "category"])

# Splitting dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df["text"], df["category"], test_size=0.2, random_state=42)

# Setting up text processing and classification pipeline
print("Setting up the text classification model...")
model = make_pipeline(TfidfVectorizer(stop_words='english'), MultinomialNB())

# Train the model
print("Training the model...")
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Function to predict category of new text
def predict_category(text):
    """Predicts the category of the given text input."""
    category = model.predict([text])[0]
    return category

# Test the model with new user input
new_text = "The central bank reduced interest rates to boost the economy"
predicted_category = predict_category(new_text)
print(f"Predicted Category: {predicted_category}")
