import math
from collections import defaultdict
from .vocabulary import Vocabulary
from .ticket import Ticket


class TicketClassifier:
    def __init__(self, vocabulary: Vocabulary):
        self.vocabulary = vocabulary
        self.category_probabilities = defaultdict(
            lambda: [0.0] * vocabulary.vocabulary_size
        )
        self.category_counts = defaultdict(int)
        self.total_tickets = 0
        self.categories = set()

    def train(self, training_data: list[Ticket]):
        self.total_tickets = len(training_data)
        for ticket in training_data:
            self.categories.add(ticket.category)
            self.category_counts[ticket.category] += 1

        for ticket in training_data:
            words = ticket.text.lower().split()
            for word in words:
                word_index = self.vocabulary.get_word_index(word)
                if word_index != -1:
                    self.category_probabilities[ticket.category][word_index] += 1.0

        for category in self.categories:
            category_probs = self.category_probabilities[category]
            category_word_count = sum(category_probs)
            for i in range(len(category_probs)):
                category_probs[i] = (category_probs[i] + 1) / (
                    category_word_count + self.vocabulary.vocabulary_size
                )

    def classify(self, text: str) -> str:
        best_prob = -float("inf")
        best_category = None

        for category in self.categories:
            category_prob = math.log(
                self.category_counts[category] / self.total_tickets
            )
            words = text.lower().split()
            for word in words:
                word_index = self.vocabulary.get_word_index(word)
                if word_index != -1:
                    category_prob += math.log(
                        self.category_probabilities[category][word_index]
                    )

            if category_prob > best_prob:
                best_prob = category_prob
                best_category = category

        return best_category
