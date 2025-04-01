def count_words_and_characters():
    text = input("Enter text:\n")

    word_count = len(text.split())
    char_count = len(text)

    print(f"\n Word count: {word_count}")
    print(f" character count: {char_count}")
count_words_and_characters()
