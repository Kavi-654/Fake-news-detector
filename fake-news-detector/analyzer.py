import re,json,string

def load_words():
    with open('data/bad_words.json','r') as f:
        return json.load(f)


def check_caps(headline):
    words=headline.split()
    caps_count=sum(1 for w in words if w.isupper() and len(w)>2)
    return caps_count

def check_sensational(headline,words):
    headline_lower=headline.lower()
    found=[w for w in words['sensational'] if w in headline_lower]
    return found

def check_punctuation(headline):
    return len(re.findall(r'[!?]{2,}',headline))

def check_clickbait(headline,words):
    headline_lower=headline.lower()
    found=[p for p in words ['clickbait'] if p in headline_lower]
    return found

# Add this to analyzer.py
def check_fear(headline, words):
    headline_lower = headline.lower()
    found = [w for w in words['fear_words'] if w in headline_lower]
    return found