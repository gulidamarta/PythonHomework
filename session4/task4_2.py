from collections import Counter


def most_common_words(filepath, number_of_words):
    """Function, that search for most common words in the file."""
    with open(filepath, 'r') as input_file:
        words = input_file.read()
    words = words.lower()
    words.replace(',', ' ').replace('.', ' ')
    words = words.split(' ')

    word_counter = {}
    for word in words:
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1

    popular_words = sorted(word_counter, key=word_counter.get, reverse=True)
    return popular_words[:number_of_words]


def most_common_words_with_counter(filepath, number_of_words):
    """Function, that search for most common words with use of Counter"""
    with open(filepath, 'r') as input_file:
        words = input_file.read()
    words = words.lower()
    words.replace(',', ' ').replace('.', ' ')
    words = words.split(' ')
    counter = Counter(words)
    most_occur = counter.most_common(number_of_words)
    return most_occur


def main():
    print(most_common_words(filepath='data/lorem_ipsum.txt', number_of_words=3))


if __name__ == '__main__':
    main()