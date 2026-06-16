import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the messy dataset
df = pd.read_csv('messy_real_estate.csv')
print("--- RAW DATA OVERVIEW ---")
print(df.head(), "\n")
print("Missing Values Count:\n", df.isnull().sum(), "\n")

# 2. DATA CLEANING (Wrangling)

print(f"Initial row count: {len(df)}")
df = df.drop_duplicates()
print(f"Row count after removing duplicates: {len(df)}\n")

df.loc[df['Price_Lakhs'] < 0, 'Price_Lakhs'] = np.nan

df['Price_Lakhs'] = df.groupby('BHK')['Price_Lakhs'].transform(lambda x: x.fillna(x.median()))
df['Area_SqFt'] = df.groupby('BHK')['Area_SqFt'].transform(lambda x: x.fillna(x.median()))
df = df[df['Price_Lakhs'] < 2000]

print("--- CLEANED DATA OVERVIEW ---")
print(df.isnull().sum())
print("Data fully cleaned without missing values and weird outliers!\n")

# 3. STATISTICAL VISUALIZATION (EDA)
sns.set_theme(style="whitegrid")

# Figure 1: Price distribution across different Locations (Boxplot)
plt.figure(figsize=(10, 6))
sns.boxplot(x='Location', y='Price_Lakhs', data=df, palette='Set2')
plt.title('Property Price Distribution Across Locations', fontsize=14)
plt.xlabel('Location (Chennai Zones)', fontsize=12)
plt.ylabel('Price (in Lakhs)', fontsize=12)
plt.savefig('location_price_distribution.png')
print("Saved Chart 1: location_price_distribution.png")

# Figure 2: Area vs Price Correlation (Scatter Plot)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Area_SqFt', y='Price_Lakhs', hue='BHK', size='BHK', data=df, palette='viridis', sizes=(50, 200))
plt.title('Property Area vs Price Analysis', fontsize=14)
plt.xlabel('Area (SqFt)', fontsize=12)
plt.ylabel('Price (in Lakhs)', fontsize=12)
plt.savefig('area_price_scatter.png')
print("Saved Chart 2: area_price_scatter.png")

plt.show()