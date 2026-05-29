import pandas as pd
import matplotlib.pyplot as plt
# Load dataset
df = pd.read_csv("quotes.csv")
# Display first 5 rows
print("FIRST 5 ROWS")
print(df.head())
# Display dataset information
print("\nDATASET INFO")
print(df.info())
# Total number of quotes
print("\nTOTAL QUOTES")
print(len(df))
# Count unique authors
print("\nUNIQUE AUTHORS")
print(df['Author'].nunique())
# Count quotes by each author
author_counts = df['Author'].value_counts()
# Display top authors
print("\nTOP AUTHORS")
print(author_counts.head())
# Create bar chart
author_counts.head(5).plot(kind='bar')
plt.title("Top 5 Authors")
plt.xlabel("Authors")
plt.ylabel("Number of Quotes")
plt.show()
