import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import re
import string

# Load datasets
df_fake = pd.read_csv('https://raw.githubusercontent.com/anmolairi03/Brainwave_Matrix_Intern/refs/heads/main/task%201/Fake.csv')
df_true = pd.read_csv('https://raw.githubusercontent.com/anmolairi03/Brainwave_Matrix_Intern/refs/heads/main/task%201/True.csv')

# Assign class labels
df_fake["class"] = 0
df_true["class"] = 1

# Remove last 10 rows for manual testing
df_fake_manual_testing = df_fake.tail(10)
df_fake = df_fake.iloc[:-10]

df_true_manual_testing = df_true.tail(10)
df_true = df_true.iloc[:-10]

# Combine manual testing datasets
df_manual_testing = pd.concat([df_fake_manual_testing, df_true_manual_testing], axis=0)
df_manual_testing.to_csv("manual_testing.csv")

# Merge and shuffle the datasets
df_merge = pd.concat([df_fake, df_true], axis=0)
df = df_merge.drop(["title", "subject", "date"], axis=1)
df = df.sample(frac=1).reset_index(drop=True)

# Check for null values
print(df.isnull().sum())

# Text preprocessing function
def word_drop(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\\W", " ", text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

# Apply preprocessing
df["text"] = df["text"].apply(word_drop)

# Split the data
x = df["text"]
y = df["class"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)

# Vectorize the text
from sklearn.feature_extraction.text import TfidfVectorizer
vectorization = TfidfVectorizer()
xv_train = vectorization.fit_transform(x_train)
xv_test = vectorization.transform(x_test)

# Logistic Regression
from sklearn.linear_model import LogisticRegression
LR = LogisticRegression()
LR.fit(xv_train, y_train)
pred_LR = LR.predict(xv_test)
print("Logistic Regression Report:\n", classification_report(y_test, pred_LR))

# Decision Tree Classifier
from sklearn.tree import DecisionTreeClassifier
DT = DecisionTreeClassifier()
DT.fit(xv_train, y_train)
pred_DT = DT.predict(xv_test)
print("Decision Tree Report:\n", classification_report(y_test, pred_DT))

# Gradient Boosting Classifier
from sklearn.ensemble import GradientBoostingClassifier
GBC = GradientBoostingClassifier(random_state=0)
GBC.fit(xv_train, y_train)
pred_GBC = GBC.predict(xv_test)
print("Gradient Boosting Report:\n", classification_report(y_test, pred_GBC))

# Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier
RFC = RandomForestClassifier(random_state=0)
RFC.fit(xv_train, y_train)
pred_RFC = RFC.predict(xv_test)
print("Random Forest Report:\n", classification_report(y_test, pred_RFC))


# Manual Testing Function
def output_label(n):
    return "Fake News" if n == 0 else "True News"

def manual_testing(news):
    testing_news = {"text": [news]}
    new_def_test = pd.DataFrame(testing_news)
    new_def_test["text"] = new_def_test["text"].apply(word_drop)
    new_x_test = new_def_test["text"]
    new_xv_test = vectorization.transform(new_x_test)
    
    pred_LR = LR.predict(new_xv_test)[0]
    pred_DT = DT.predict(new_xv_test)[0]
    pred_GBC = GBC.predict(new_xv_test)[0]
    pred_RFC = RFC.predict(new_xv_test)[0]
    
    # Output predictions from all models
    print(f"Logistic Regression Prediction: {output_label(pred_LR)}")
    print(f"Decision Tree Prediction: {output_label(pred_DT)}")
    print(f"Gradient Boosting Prediction: {output_label(pred_GBC)}")
    print(f"Random Forest Prediction: {output_label(pred_RFC)}")


news = input("Enter the news: ")
manual_testing(news)
