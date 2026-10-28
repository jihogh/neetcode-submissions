class PrefixNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = PrefixNode()

    def insert(self, word: str) -> None:
        pointer = self.root

        for char in word:
            if not char in pointer.children:
                pointer.children[char] = PrefixNode()
            pointer = pointer.children[char]

        pointer.endOfWord = True

    def search(self, word: str) -> bool:
        pointer = self.root

        for char in word:
            if not char in pointer.children:
                return False
            pointer = pointer.children[char]
        
        return True if pointer.endOfWord == True else False

    def startsWith(self, prefix: str) -> bool:
        pointer = self.root

        for char in prefix:
            if not char in pointer.children:
                return False
            pointer = pointer.children[char]

        return True