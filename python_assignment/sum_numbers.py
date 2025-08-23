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
