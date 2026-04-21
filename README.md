# 🕵️ Fake News Headline Detector

A command-line Python tool that analyzes news headlines
and assigns a **credibility score** based on rule-based
text analysis — no machine learning, just smart logic!

## 🚀 Features
- Detects sensational and emotionally charged words
- Flags excessive capitalization (SHOUTING)
- Identifies clickbait phrases
- Checks for excessive punctuation (!!!)
- Saves analysis history with timestamps
- Clean credibility score: 0-100

## 🛠️ Tech Stack
- Python 3.x (no external libraries!)
- Built-in: re, json, string, datetime

## 📦 Installation
```bash
git clone https://github.com/yourusername/Fake-news-detector
cd fake-news-detector
python main.py
```

## 🎯 How It Works
The detector checks 5 red flags:
1. Sensational words  → -15 pts each
2. ALL CAPS words     → -10 pts each
3. Clickbait phrases  → -25 pts each
4. Excessive !! / ??  → -10 pts each
5. Fear/conspiracy    → -10 pts each

Score 80-100 = ✅ Credible
Score 50-79  = ⚠️  Suspicious
Score 0-49   = 🚨 Likely Fake

## 📁 Project Structure
```
fake-news-detector/
├── main.py        # Entry point
├── analyzer.py    # Detection logic
├── scorer.py      # Score calculator
├── data/
│   └── bad_words.json
└── output/
    └── history.txt
```

## 🌱 Future Improvements
- Add Flask web API
- Connect to real news APIs
- Add source credibility checking
- Build a simple web UI

## 👨💻 Author
Built by [Kavinayasri -M] — a Python learner
exploring real-world applications.

