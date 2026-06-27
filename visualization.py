import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r"D:\new\books.csv")  # full path

# Set Seaborn style
sns.set(style="whitegrid")

# 1️⃣ Price Distribution
plt.figure(figsize=(10,6))
sns.histplot(df['price'], bins=20, kde=True, color='skyblue')
plt.title("Distribution of Book Prices", fontsize=16)
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.show()

# 2️⃣ Boxplot for Outliers
plt.figure(figsize=(8,4))
sns.boxplot(x=df['price'], color='lightgreen')
plt.title("Boxplot of Book Prices", fontsize=14)
plt.show()

# 3️⃣ Top 10 Most Expensive Books
top_expensive = df.sort_values("price", ascending=False).head(10)
plt.figure(figsize=(12,6))
sns.barplot(x='price', y='title', data=top_expensive, palette='Reds_r')
plt.title("Top 10 Most Expensive Books", fontsize=16)
plt.xlabel("Price (£)")
plt.ylabel("Book Title")
plt.show()

# 4️⃣ Top 10 Cheapest Books
top_cheap = df.sort_values("price", ascending=True).head(10)
plt.figure(figsize=(12,6))
sns.barplot(x='price', y='title', data=top_cheap, palette='Blues')
plt.title("Top 10 Cheapest Books", fontsize=16)
plt.xlabel("Price (£)")
plt.ylabel("Book Title")
plt.show()

# 5️⃣ Optional: Price Scatter Plot
plt.figure(figsize=(12,6))
sns.scatterplot(x=range(len(df)), y='price', data=df, color='purple')
plt.title("Book Prices Scatter Plot", fontsize=16)
plt.xlabel("Book Index")
plt.ylabel("Price (£)")
plt.show()