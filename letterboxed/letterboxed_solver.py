# letterboxed_solver.py

from re import match


def same_group(letter1, letter2, letter_groups):
    for group in letter_groups:
        if letter1 in group and letter2 in group:
            return True
    return False


def get_input():
    while True:
        input_string = input("Enter the letters: ").upper()
        if match("^[a-zA-Z]{12}$", input_string) and (
            len(set(input_string)) == len(input_string)
        ):
            return input_string
        print("Invalid input. Input must be 12 unique letters. Please try again.")


def prepare_wordlist(letters):
    groups = [letters[0:3], letters[3:6], letters[6:9], letters[9:12]]

    # Load wordlist
    with open("data/wordlist_letterboxed.txt", "r", encoding="latin-1") as f:
        wordlist = {line.strip() for line in f}

    # Reduce to possible words
    wordlist = {word for word in wordlist if all(letter in letters for letter in word)}
    for word in wordlist.copy():
        for i in range(len(word) - 1):
            if same_group(word[i], word[i + 1], groups):
                wordlist.remove(word)
                break

    # Sort by unique letters and length
    wordlist = sorted(
        wordlist, key=lambda word: (len(set(word)), 1 / len(word)), reverse=True
    )

    return wordlist


def solve(letters, wordlist):
    # First, check if wordlist contains a word that uses all letters
    for word in wordlist:
        if len(set(word)) == len(letters):
            return [word]


    # Split wordlist by first letter
    first_letter_dict = {}
    for word in wordlist:
        first_letter = word[0]
        if first_letter not in first_letter_dict:
            first_letter_dict[first_letter] = [word]
        else:
            first_letter_dict[first_letter].append(word)

    # Simple loop-based approach; it's unlikely that any solution ever requires a depth of more than 2
    candidates = []
    for first_word in wordlist:
        for second_word in first_letter_dict[first_word[-1]]:
            if len(set(first_word + second_word)) == len(letters):
                candidates.append(first_word + "-" + second_word)
                
    # Depth-three search; very slow. This can be improved to only go deeper when depth 2 fails to find a solution
    # candidates = []
    # for first_word in wordlist:
    #     for second_word in first_letter_dict.get(first_word[-1], []):
    #         for third_word in first_letter_dict.get(second_word[-1], []):
    #             combined = first_word + second_word + third_word
    #             if len(set(combined)) == len(letters):
    #                 candidates.append(first_word + "-" + second_word + "-" + third_word)

    if len(candidates) > 0:
        return sorted(candidates, key=len)
    return None
        


letters = get_input()
wordlist = prepare_wordlist(letters)
print(solve(letters, wordlist))
