from views.views import AlphabetView, MainMenuView
from models.models import AlphabetModel


class AlphabetController:

    def __init__(self):
        self.model = AlphabetModel()
        self.view = AlphabetView()
        self.main_menu = MainMenuView()
    
    def run_program(self):
        self.main_menu.display_main_menu(self.model)

    def select_random_letter(self):
        letter = self.model.select_random_letter()
        self.view.display_letter(letter, self.model.remaining_letters)

    def reset_letters(self):
        self.model.reset_letters()
        #print("Les lettres ont été réinitialisées.")
