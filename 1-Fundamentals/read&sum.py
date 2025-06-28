# Exercise 1: Reading and Summing Numbers
def sum_numbers_from_file(filename):
    try:
        with open(filename, 'r') as file:
            total = 0
            for line in file:
                line = line.strip()
                if line.isdigit():
                    total += int(line)
        print(f"Sum of numbers in '{filename}': {total}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Exercise 2: Word Frequency Counter
def count_word_frequencies(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
        # Remove punctuation and make all lowercase
        import re
        words = re.findall(r'\b\w+\b', text.lower())
        word_freq = {}

        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1

        print(f"\nWord frequencies in '{filename}':")
        for word, freq in sorted(word_freq.items()):
            print(f"{word}: {freq}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main program
if __name__ == "__main__":
    # Change filenames as needed
    number_file = "numbers.txt"
    text_file = "text.txt"

    print("== Exercise 1: Sum Numbers ==")
    sum_numbers_from_file(number_file)

    print("\n== Exercise 2: Word Frequency ==")
    count_word_frequencies(text_file)
