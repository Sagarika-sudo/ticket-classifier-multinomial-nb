# from ticket_classifier.classifier import TicketClassifier
    # from ticket_classifier.vocabulary import Vocabulary
    # from ticket_classifier.utils import create_training_data
    # from ticket_classifier.ticket import Ticket
    import sys
    sys.path.append(r"C:\Users\velupula.sagarika\Documents\ticket-classifier-multinomial-nb")
    from ticket_classifier.classifier import TicketClassifier
    from ticket_classifier.vocabulary import Vocabulary
    from ticket_classifier.utils import create_training_data
    from ticket_classifier.ticket import Ticket


def main():
    # Create training data
    training_data = create_training_data()

    # Build Vocabulary
    vocabulary = Vocabulary()
    vocabulary.build_vocabulary(training_data)

    # Train the classifier
    classifier = TicketClassifier(vocabulary)
    classifier.train(training_data)

    # Sample tickets to classify
    tickets_to_classify = [
        "I can not remember my login details.",
        "My laptop is very slow.",
        "The internet connection is down.",
        "I need a new account",
    ]

    # Classify the tickets
    for ticket_text in tickets_to_classify:
        category = classifier.classify(ticket_text)
        print(f"Ticket: {ticket_text} -> Category: {category}")


if __name__ == "__main__":
    main()
