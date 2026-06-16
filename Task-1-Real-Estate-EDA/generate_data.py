import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# 1. Generate fake clean data
n_samples = 200
data = {
    'Property_ID': [f'PROP_{i}' for i in range(1, n_samples + 1)],
    'Location': np.random.choice(['Adyar', 'Velachery', 'Omr', 'Tambaram'], size=n_samples),
    'BHK': np.random.choice([1, 2, 3, 4], size=n_samples, p=[0.2, 0.4, 0.3, 0.1]),
    'Price_Lakhs': np.random.randint(40, 250, size=n_samples).astype(float),
    'Area_SqFt': np.random.randint(500, 2500, size=n_samples)
}

df = pd.DataFrame(data)

# 2. Make it MESSY intentionally (as required by your task)
# Inject missing values
df.loc[df.sample(frac=0.08).index, 'Price_Lakhs'] = np.nan
df.loc[df.sample(frac=0.05).index, 'Area_SqFt'] = np.nan

# Inject outliers (Extremely wrong values)
df.at[15, 'Price_Lakhs'] = 9999.0  # Impossible price for a normal flat
df.at[85, 'Price_Lakhs'] = -50.0   # Negative price is impossible

# Inject duplicates
df = pd.concat([df, df.iloc[[10, 20, 30]]], ignore_index=True)

# Save to CSV
df.to_csv('messy_real_estate.csv', index=False)
print("Super! 'messy_real_estate.csv' successfully created inside your folder.")