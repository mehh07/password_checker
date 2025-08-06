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

Example

Enter your password: Welcome123!

Password Strength: 🔐 Strong
Details:
• ✅ Long password (12+ characters)
• ✅ Contains digits
• ✅ Contains special characters
• ✅ Contains both uppercase and lowercase letters
• ✅ High entropy (48.2 bits)

---

## 🚀 Final Steps

1. ✅ Put this in a folder: `password-strength-checker`
2. ✅ Run `python main.py` to test
3. ✅ Add to GitHub (if needed)
4. ✅ Mention on your resume as:
   > Built a rule-based password strength evaluator using entropy, dictionary, and structural analysis. Used custom scoring logic with real-world password patterns.

Made with 🧠 by mehhh07


