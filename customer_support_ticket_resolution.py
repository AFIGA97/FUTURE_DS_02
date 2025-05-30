# -*- coding: utf-8 -*-
"""customer_support_ticket resolution

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1I_mFEIdvN4B6w029sys4PeWXv15BSXij
"""

# Install required libraries
!pip install pandas nltk matplotlib seaborn wordcloud

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from wordcloud import WordCloud
import nltk
nltk.download('punkt')
nltk.download('stopwords')

# Load data
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("customer_support_tickets.csv")

# Data Cleaning
# Handle missing values
df.fillna({'Resolution': 'Unresolved', 'Customer Satisfaction Rating': 0}, inplace=True)

# Convert dates to datetime
df['First Response Time'] = pd.to_datetime(df['First Response Time'])
df['Time to Resolution'] = pd.to_datetime(df['Time to Resolution'])

# Calculate response times in hours
df['First Response Hours'] = (df['First Response Time'] - pd.to_datetime(df['Date of Purchase'])).dt.total_seconds() / 3600
df['Resolution Hours'] = (df['Time to Resolution'] - df['First Response Time']).dt.total_seconds() / 3600

import nltk
nltk.download('punkt_tab') # Download the punkt_tab data package

# Text Analysis for Common Issues
stop_words = set(stopwords.words('english'))
ticket_text = " ".join(df['Ticket Description'].dropna().astype(str))
words = word_tokenize(ticket_text.lower())
filtered_words = [word for word in words if word.isalpha() and word not in stop_words]
common_words = FreqDist(filtered_words).most_common(20)

# Generate Word Cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(" ".join(filtered_words))
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Most Frequent Words in Support Tickets")
plt.show()

# Summary Statistics
print("Average First Response Time (Hours):", df['First Response Hours'].mean())
print("Average Resolution Time (Hours):", df['Resolution Hours'].mean())
print("\nTicket Type Distribution:")
print(df['Ticket Type'].value_counts(normalize=True) * 100)

# Export Cleaned Data for Tableau
df.to_csv('cleaned_support_tickets.csv', index=False)
files.download('cleaned_support_tickets.csv')