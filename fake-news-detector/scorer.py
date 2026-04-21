def calculate_score(caps, sensational, punctuation, clickbait, fear):
    score = 100
    score -= caps * 10
    score -= len(sensational) * 15
    score -= punctuation * 10
    score -= len(clickbait) * 25
    score -= len(fear) * 10
    return max(0, score)

def get_verdict(score):
    if score >= 80:
        return '✅ Likely Credible'
    elif score >= 50:
        return '⚠️  Suspicious'
    else:
        return '🚨 Likely Fake / Clickbait'
