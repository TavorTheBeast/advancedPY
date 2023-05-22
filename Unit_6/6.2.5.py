class GreetingCard:
    def __init__(self, recipient="Dana Ev", sender="Eyal Ch"):
        self._recipient = recipient
        self._sender = sender

    def greeting_msg(self):
        print(f"Sender: {self._sender}")
        print(f"Recipient: {self._recipient}")



from file1 import GreetingCard


class BirthdayCard(GreetingCard):
    def __init__(self, sender_age=0, recipient="Dana Ev", sender="Eyal Ch"):
        super().__init__(recipient, sender)
        self._sender_age = sender_age

    def greeting_msg(self):
        print(f"Sender: {self._sender}")
        print(f"Recipient: {self._recipient}")
        print(f"Happy birthday! Sender's age: {self._sender_age}")



from file1 import GreetingCard
from file2 import BirthdayCard

birthday_card = BirthdayCard(sender_age=30)
birthday_card.greeting_msg()

greeting_card = GreetingCard()
greeting_card.greeting_msg()
