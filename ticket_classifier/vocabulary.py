class Vocabulary:
    def __init__(self):
        self.word_to_index = {}
        self.index_to_word = []
        self.vocabulary_size = 0

    def build_vocabulary(self, tickets):
        unique_words = set()
        for ticket in tickets:
            words = ticket.text.lower().split()
            unique_words.update(words)

        for word in unique_words:
            self.word_to_index[word] = self.vocabulary_size
            self.index_to_word.append(word)
            self.vocabulary_size += 1

    def get_word_index(self, word):
        return self.word_to_index.get(word, -1)

    def get_word(self, index):
        if 0 <= index < len(self.index_to_word):
            return self.index_to_word[index]
        return None
