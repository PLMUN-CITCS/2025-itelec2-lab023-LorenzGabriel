def get_sentence_input():
    return input("Enter a sentence: ")

def count_words(sentence):
    # Handling case where the sentence might be empty
    if sentence.strip() == "":
        return 0
    return len(sentence.split())

def main():
    sentence = get_sentence_input()
    word_count = count_words(sentence)
    print(f"The sentence has {word_count} words.")

main()


