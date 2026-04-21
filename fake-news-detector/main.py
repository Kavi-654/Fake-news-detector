from history import save_to_history
import analyzer
import scorer


def analyze_headline(headline):
    words = analyzer.load_words()

    # Run all detection logic [cite: 6, 102, 103, 104, 105]
    caps = analyzer.check_caps(headline)
    sensational = analyzer.check_sensational(headline, words)
    punctuation = analyzer.check_punctuation(headline)
    clickbait = analyzer.check_clickbait(headline, words)
    fear = analyzer.check_fear(headline, words)  # Added fear check

    # Calculate score [cite: 83, 106]
    score = scorer.calculate_score(caps, sensational, punctuation, clickbait, fear)
    verdict = scorer.get_verdict(score)

    # Visual Output Formatting [cite: 129, 133, 138, 140]
    print("\n" + "-" * 41)
    print(f"📰 Headline: {headline}")
    print("-" * 41)

    print("🔍 Analysis:")
    print(f"  • ALL CAPS words found: {caps}  (-{caps * 10} pts)")
    print(f"  • Sensational words: {sensational}  (-{len(sensational) * 15} pts)")
    print(f"  • Excessive punctuation: {punctuation} instance  (-{punctuation * 10} pts)")
    print(f"  • Fear/conspiracy words: {fear}  (-{len(fear) * 10} pts)")

    print(f"\n📊 Credibility Score: {score} / 100")
    print(f"{verdict}")
    print("-" * 41)

    # Save and Log [cite: 141]
    save_to_history(headline, score, verdict)
    print("💾 Saved to output/history.txt")


if __name__ == '__main__':
    # Initial Header [cite: 124, 125]
    print("=========================================")
    print("🕵️  FAKE NEWS HEADLINE DETECTOR")
    print("=========================================")

    while True:
        user_headline = input("\nPaste a news headline: ")
        analyze_headline(user_headline)

        # Loop for multiple analyses 
        choice = input("\nAnalyze another headline? (y/n): ").lower()
        if choice != 'y':
            print("Goodbye! Stay informed. 🚀")
            break