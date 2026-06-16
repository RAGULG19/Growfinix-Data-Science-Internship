import numpy as np
import pandas as pd
from scipy import stats

# 1. Simulate A/B Testing Data
# Group A: Standard Table Layout | Group B: Card Layout
np.random.seed(42)

# Simulating 1000 users for each group (1 = Converted/Bought, 0 = Not Converted)
# Table Layout conversion rate ~ 12% | Card Layout conversion rate ~ 16%
group_A = np.random.choice([0, 1], size=1000, p=[0.88, 0.12])
group_B = np.random.choice([0, 1], size=1000, p=[0.84, 0.16])

# 2. Calculate Conversions and Totals
conversions_A = np.sum(group_A)
conversions_B = np.sum(group_B)

print(f"--- A/B TEST RAW SUMMARY ---")
print(f"Group A (Table Layout): {conversions_A} conversions out of 1000 users")
print(f"Group B (Card Layout) : {conversions_B} conversions out of 1000 users\n")

# 3. Perform Two-Sample Z-Test / Chi-Square Test using SciPy
# Creating a contingency table for statistical test
contingency_table = [
    [conversions_A, 1000 - conversions_A],
    [conversions_B, 1000 - conversions_B]
]

# Calculate Chi-Square statistic and P-Value
chi2, p_value, dof, expected = stats.chi2_contingency(contingency_table)

print(f"--- STATISTICAL ANALYSIS ---")
print(f"Chi-Square Statistic: {chi2:.4f}")
print(f"P-Value: {p_value:.5f}")

# 4. Determine Statistical Significance (Alpha = 0.05)
alpha = 0.05
if p_value < alpha:
    print("\nResult: STATISTICALLY SIGNIFICANT! 🚀")
    print("Reject the Null Hypothesis. The Card Layout significantly improves user conversion rates.")
else:
    print("\nResult: NOT STATISTICALLY SIGNIFICANT! ❌")
    print("Fail to reject the Null Hypothesis. No significant difference between the layouts.")