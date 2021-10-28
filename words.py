def print_upper_words(words, must_start_with):
    """For a list of words, print out each word on a separate line, but in all uppercase."""

    for word in words:
        for letter in must_start_with:
            if word[0] == letter:
                print(word.upper(), '\n')
