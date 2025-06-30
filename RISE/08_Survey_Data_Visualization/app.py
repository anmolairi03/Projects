# Save this as app.py and run with: streamlit run app.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("survey_data.csv")

st.title("Survey Data Dashboard")

# Summary metrics
st.subheader("📊 Summary Metrics")
st.write(f"Average Satisfaction Level: {df['Satisfaction_Level'].mean():.2f}")
st.write(f"Average Ease of Use: {df['Ease_of_Use'].mean():.2f}")
st.write(f"Average Recommendation Likelihood: {df['Recommendation_Likelihood'].mean():.2f}")

st.subheader("Satisfaction Level Distribution")
sns.set_theme()
fig1, ax1 = plt.subplots()
sns.countplot(data=df, x='Satisfaction_Level', palette='Blues', ax=ax1)
st.pyplot(fig1)

st.subheader("Recommendation Likelihood")
fig2, ax2 = plt.subplots()
df['Recommendation_Likelihood'].value_counts().sort_index().plot.pie(autopct='%1.1f%%', ax=ax2, colors=sns.color_palette("pastel"))
ax2.set_ylabel("")
st.pyplot(fig2)

st.subheader("Correlation Heatmap")
fig3, ax3 = plt.subplots()
sns.heatmap(df.drop("Respondent_ID", axis=1).corr(), annot=True, cmap="YlOrRd", ax=ax3)
st.pyplot(fig3)
