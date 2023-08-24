import random

class ChoiceList(list):
    def choice(self):
        try:
            return random.choice(self)
        except IndexError:
            print("Cannot select from an empty list! ")

