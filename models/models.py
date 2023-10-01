import random


class AlphabetModel:

    def __init__(self):
        self.alphabet = list("abcdefghijklmnopqrstuvwxyz")
        self.remaining_letters = len(self.alphabet)

    def select_random_letter(self):
        if self.remaining_letters == 0:
            return None
        indice = random.randint(0, self.remaining_letters - 1)
        lettre = self.alphabet[indice]
        self.remaining_letters -= 1
        return lettre

    def reset_letters(self):
        self.remaining_letters = len(self.alphabet)
        print()
        print("Les lettres ont été réinitialisées.")
