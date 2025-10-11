# Framing-of-C-Suite-Executives
# Web Parser + Model Evaluation

This repo demonstrates:
1. Manually select and fetch a website (or pages).
2. Parse the HTML to structured JSON using a parser.
3. Run multiple models on the parsed / extracted text.
4. Score model outputs (BLEU, ROUGE, embedding similarity, BERTScore).
5. Compare models to determine which best suits the task.

## Quickstart
0. Create a Python 3.10+ virtualenv and install:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
