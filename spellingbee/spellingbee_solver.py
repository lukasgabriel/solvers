#speelingbee_solver.py

from re import match

MIN_LENGTH = 4


def get_input():
    while True:
        input_string = input("Enter the letters, starting with the central letter: ").upper()
        if match("^[a-zA-Z]{7}$", input_string) and (
            len(set(input_string)) == len(input_string)
        ):
            return input_string
        print("Invalid input. Input must be 7 unique letters. Please try again.")

def prepare_wordlist(letters):
    central_letter = letters[0]

    # Load wordlist
    with open("data/wordlist_spellingbee.txt", "r", encoding="latin-1") as f:
        wordlist = {line.strip() for line in f}

    # Reduce to possible words
    wordlist = {word for word in wordlist if len(word) >= MIN_LENGTH and central_letter in word and all(letter in letters for letter in word)}

    # Sort by unique letters and length
    wordlist = sorted(
        wordlist, key=lambda word: (len(set(word)), 1 / len(word)), reverse=True
    )

    return wordlist


print(prepare_wordlist(get_input()))
