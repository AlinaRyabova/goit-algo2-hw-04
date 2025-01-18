from homework import Homework

if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Перевірка кількості слів, що закінчуються на заданий суфікс
    print(trie.count_words_with_suffix("e"))  # Очікується: 1 (apple)
    print(trie.count_words_with_suffix("ion"))  # Очікується: 1 (application)
    print(trie.count_words_with_suffix("a"))  # Очікується: 1 (banana)
    print(trie.count_words_with_suffix("at"))  # Очікується: 1 (cat)

    # Перевірка наявності префікса
    print(trie.has_prefix("app"))  # Очікується: True (apple, application)
    print(trie.has_prefix("bat"))  # Очікується: False
    print(trie.has_prefix("ban"))  # Очікується: True (banana)
    print(trie.has_prefix("ca"))  # Очікується: True (cat)

