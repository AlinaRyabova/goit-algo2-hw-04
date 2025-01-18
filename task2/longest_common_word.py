from trie import Trie

class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        # Перевірка на некоректні вхідні дані
        if not strings or not all(isinstance(word, str) for word in strings):
            return ""
        
        # Вставляємо всі слова у Trie
        for word in strings:
            self.insert(word)
        
        # Знаходимо найдовший спільний префікс
        prefix = ""
        node = self.root
        while node and len(node.children) == 1 and not node.is_end_of_word:
            char, next_node = list(node.children.items())[0]
            prefix += char
            node = next_node

        return prefix
