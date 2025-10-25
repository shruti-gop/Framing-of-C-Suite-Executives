keywords = ["appointed CEO", "named CFO", "joined as Chief", "bio", "background", "education", "with a PhD", "engineer”, “big company”, “manager”, “hired”, “-startup”, “-small business”, “-hiring”, "-nonprofit"]



import numpy as np
import pandas as pd

# Simulated toy dataset
np.random.seed(42)
df = pd.DataFrame({
    "exec_background_score": np.random.uniform(0, 1, 10),  # X
})
df["framing_score"] = 0.6 * df["exec_background_score"] + np.random.normal(0, 0.1, 10)  # M
df["market_cap"] = 1.2 * df["framing_score"] + 0.4 * df["exec_background_score"] + np.random.normal(0, 0.1, 10) # Y

print("\n=== Toy Dataset Preview ===")
print(df.head())

print("\nThis simulates the structure: background → framing → market cap.")
print("Full mediation + regression logic will be added once real text and embeddings are in.")
