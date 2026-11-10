"""Example rubric scorer for AI-generated responses.

Usage:
    python3 evaluate.py examples/sample_responses.json

This is an example / learning script. It scores a response against a
simple rubric (accuracy, relevance, clarity, completeness) using
keyword checks and length checks only. It does not verify facts
against an external source, and its scores are only a starting
point for human review.
"""

import json
import sys


RUBRIC = ["accuracy", "relevance", "clarity", "completeness"]


def score_item(item):
    """Score one prompt/response pair on a 0-5 scale per rubric item."""
    prompt = item.get("prompt", "")
    response = item.get("response", "")
    expected = item.get("expected_keywords", [])
    words = response.split()
    scores = {}

    # Accuracy (example only): how many expected keywords appear.
    found = sum(1 for kw in expected if kw.lower() in response.lower())
    scores["accuracy"] = round(5 * found / max(len(expected), 1), 1) if expected else 0.0

    # Relevance (example only): overlap between prompt words and response words.
    prompt_words = {w.strip("?,.").lower() for w in prompt.split() if len(w) > 3}
    response_words = {w.strip("?,.").lower() for w in words}
    overlap = len(prompt_words & response_words)
    scores["relevance"] = round(min(5.0, overlap), 1)

    # Clarity (example only): penalise very long sentences.
    sentences = [s for s in response.replace("?", ".").split(".") if s.strip()]
    avg_len = len(words) / max(len(sentences), 1)
    scores["clarity"] = 5.0 if avg_len <= 20 else 3.0 if avg_len <= 30 else 1.0

    # Completeness (example only): response length vs a simple target.
    scores["completeness"] = 5.0 if len(words) >= 20 else round(5 * len(words) / 20, 1)

    scores["overall"] = round(sum(scores[k] for k in RUBRIC) / len(RUBRIC), 1)
    return scores


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "examples/sample_responses.json"
    with open(path, encoding="utf-8") as f:
        items = json.load(f)
    for i, item in enumerate(items, 1):
        print(f"\n#{i}  {item.get('prompt', '')}")
        print(f"Response: {item.get('response', '')}")
        print(f"Scores: {score_item(item)}")


if __name__ == "__main__":
    main()