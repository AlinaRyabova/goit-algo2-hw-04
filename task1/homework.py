from trie import Trie

class Homework(Trie):
    def count_words_with_suffix(self, pattern: str) -> int:
        if not isinstance(pattern, str):
            raise ValueError("Pattern must be a string")

        def collect_suffixes(node, collected_suffix):
            count = 0
            if node.is_end_of_word and collected_suffix.endswith(pattern):
                count += 1
            for char, child_node in node.children.items():
                count += collect_suffixes(child_node, collected_suffix + char)
            return count

        return collect_suffixes(self.root, "")

    def has_prefix(self, prefix: str) -> bool:
        if not isinstance(prefix, str):
            raise ValueError("Prefix must be a string")

        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
