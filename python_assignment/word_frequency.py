import string
from collections import Counter

def clean_word(word):
    # Remove punctuation and convert to lowercase
    return word.strip(string.punctuation).lower()

def main():
    try:
        with open("text.txt", "r") as file:
            words = []
            for line in file:
                for word in line.split():
                    cleaned = clean_word(word)
                    if cleaned:
                        words.append(cleaned)

            word_count = Counter(words)

        print("Word Frequency:")
        for word, count in word_count.items():
            print(f"{word}: {count}")
    except FileNotFoundError:
        print("Error: Cannot open file 'text.txt'.")

if __name__ == "__main__":
    main()
