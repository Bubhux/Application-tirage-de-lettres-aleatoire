from models.models import AlphabetModel


class AlphabetView:

    def display_letter(self, letter, remaining):
        if letter:
            uppercase_letter = letter.upper()
            print()
            print(f"Lettre tirée aléatoirement : {uppercase_letter}")
            print(f"Nombre de lettres restantes : {str(remaining)}")
        else:
            print("Toutes les lettres ont été tirées !")


class MainMenuView:

    def display_main_menu(self, model):
        alphabet_view = AlphabetView()
        while True:
            print("\nMenu principal :")
            print("1. Choisir une lettre aléatoire")
            print("2. Quitter le programme")
            print()
            choice = input("Votre choix : \n> ")

            if choice == "1":
                while True:
                    print("\nSous-menu - Choisir une lettre aléatoire :")
                    print(f"1. Tirer une lettre ({model.remaining_letters} lettres disponibles)")
                    print("2. Réinitialiser les lettres")
                    print("3. Retour au menu principal")
                    print()
                    under_choice = input("Votre choix : \n> ")

                    if under_choice == "1":
                        letter = model.select_random_letter()
                        alphabet_view.display_letter(letter, model.remaining_letters)
                    elif under_choice == "2":
                        model.reset_letters()
                    elif under_choice == "3":
                        break
                    else:
                        print("Choix invalide. Veuillez réessayer.")

            elif choice == "2":
                print("Au revoir !")
                break
            else:
                print("Choix invalide. Veuillez réessayer.")
