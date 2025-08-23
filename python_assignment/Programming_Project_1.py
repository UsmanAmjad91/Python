# Some of numbers code 
# numbers.txt create file with some numbers
# 10 25 30 5 -2 12
def main():
    try:
        with open("numbers.txt", "r") as file:
            total = 0
            for line in file:
                line = line.strip()
                if line:
                    try:
                        total += int(line)  
                    except ValueError:
                        print(f"Skipping invalid entry: {line}")
        print("Total sum of numbers:", total)
    except FileNotFoundError:
        print("Error: Cannot open file 'numbers.txt'.")

if __name__ == "__main__":
    main()
# Final result =80

# Word Frequency code
# text.txt create file with some text
# The quick brown fox jumps over the lazy dog.
# The quick dog did not jump over the brown fox.
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

# Final result
# quick: 2
# brown: 2
# fox: 2
# jumps: 1
# over: 2
# lazy: 1
# dog: 2
# did: 1
# not: 1
# jump: 1