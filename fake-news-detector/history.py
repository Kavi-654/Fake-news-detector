import os
from datetime import datetime


def save_to_history(headline, score, verdict):
    # Ensure the output directory exists [cite: 47]
    if not os.path.exists('output'):
        os.makedirs('output')

    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Format the log entry
    log_entry = (
        f"[{timestamp}]\n"
        f"Headline: {headline}\n"
        f"Score: {score}/100 | Verdict: {verdict}\n"
        f"{'-' * 40}\n"
    )

    # Append the entry to history.txt [cite: 40, 118]
    with open('output/history.txt', 'a', encoding='utf-8') as f:
        f.write(log_entry)