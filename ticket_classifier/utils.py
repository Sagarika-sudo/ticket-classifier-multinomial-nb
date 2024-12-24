from .ticket import Ticket


def create_training_data() -> list[Ticket]:
    """Creates sample training data."""
    training_data = [
        Ticket("My computer is slow", "Performance"),
        Ticket("The internet is not working", "Network"),
        Ticket("I cannot access the website", "Network"),
        Ticket("My email is not loading", "Network"),
        Ticket("The system is lagging", "Performance"),
        Ticket("This is running slow", "Performance"),
        Ticket("My screen is frozen", "Performance"),
        Ticket("The wifi is not working", "Network"),
        Ticket("I cannot log in", "Account"),
        Ticket("I forgot my password", "Account"),
        Ticket("I can't print", "Printing"),
        Ticket("The printer is not working", "Printing"),
        Ticket("I need to reset my password", "Account"),
        Ticket("This is very slow", "Performance"),
        Ticket("The web page is not loading", "Network"),
        Ticket("The laptop is crashing", "Performance"),
    
    ]
    return training_data
