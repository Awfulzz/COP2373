import re


def get_paragraph():
    """Prompt user to enter a paragraph."""
    print("Enter a paragraph:")
    return input()


def extract_sentences(text):
    """
    Extract sentences using regex with look-ahead.
    Handles:
    - Abbreviations (U.S.A.)
    - Decimal numbers (66.5)
    - Sentences starting with numbers
    """
    pattern = r'[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)'

    sentences = re.findall(pattern, text, flags=re.DOTALL | re.MULTILINE)
    return sentences


def display_results(sentences):
    """Display sentences and count."""
    print("\nSentences found:\n")

    for s in sentences:
        print("->", s.strip())

    print(f"\nTotal number of sentences: {len(sentences)}")


def main():
    paragraph = get_paragraph()
    sentences = extract_sentences(paragraph)
    display_results(sentences)


if __name__ == "__main__":
    main()