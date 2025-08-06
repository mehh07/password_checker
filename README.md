# 🔐 Password Strength Checker (Rule-Based)

This is a logic-based password evaluator built in Python that checks password strength using custom rules — not ML. It's based on entropy, structure, dictionary words, patterns, and more.

## Features

- Detects length, digits, specials, casing
- Calculates entropy
- Detects sequences like `1234`, `abcd`
- Checks against common dictionary words
- Classifies as Weak / Moderate / Strong

## Setup

```bash
pip install -r requirements.txt
python main.py