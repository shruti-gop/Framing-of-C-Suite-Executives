keywords = ["appointed CEO", "named CFO", "joined as Chief", "bio", "background", "education", "with a PhD", "engineer”, “big company”, “manager”, “hired”, “-startup”, “-small business”, “-hiring”, "-nonprofit"]



import numpy as np
import pandas as pd

# Simulated toy dataset
np.random.seed(42)
df = pd.DataFrame({
    "exec_background_score": np.random.uniform(0, 1, 10),  # X
})
df["framing_score"] = 0.6 * df["exec_background_score"] + np.random.normal(0, 0.1, 10)  # Z
df["market_cap"] = 1.2 * df["framing_score"] + 0.4 * df["exec_background_score"] + np.random.normal(0, 0.1, 10) # Y

print("\n=== Toy Dataset Preview ===")
print(df.head())

print("\nThis simulates the structure: background → framing → market cap.")
print("Full mediation + regression logic will be added once real text and embeddings are in.")

for url in urls:
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text(separator=' ')
        
        # Check for keywords
        has_education = bool(education_pattern.search(text))
        has_gender = bool(gender_pattern.search(text))
        
        # Append to list
        data.append({
            "url": url,
            "contains_education": has_education,
            "contains_gender": has_gender
        })
    except Exception as e:
        data.append({
            "url": url,
            "contains_education": None,
            "contains_gender": None
        })

# Create DataFrame
df = pd.DataFrame(data)
print(df)
