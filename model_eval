from transformers import pipeline

# Load text
with open("page.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Make it shorter if it's too long
text = text[:1000]

# Load models
models = {
    "bart": pipeline("summarization", model="facebook/bart-large-cnn"),
    "t5": pipeline("summarization", model="t5-small"),
}

# Run models
for name, model in models.items():
    print(f"\n=== {name.upper()} MODEL ===")
    summary = model(text, max_length=100, min_length=25, do_sample=False)
    print(summary[0]["summary_text"])
