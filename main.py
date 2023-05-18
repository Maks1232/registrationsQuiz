import random
import colorama as colorama
import pickle


class Voivodeship:
    def __init__(self, voivodeship_dict):
        self.voivodeship_dict = voivodeship_dict
        self.merged_dicts = {}

        with open('dicts.pickle', 'rb') as file:
            loaded_dicts = pickle.load(file)
        for dict in loaded_dicts:
            self.merged_dicts.update(dict)

    def get_random_question(self):
        # wybieramy losowy klucz i wartość ze słownika
        question, answer = random.choice(list(self.voivodeship_dict.items()))
        return question, answer

    def generate_answers(self, correct_answer):

        # generujemy listę odpowiedzi, w tym poprawnej odpowiedzi
        answers = [correct_answer]

        while len(answers) < 4:
            # wybieramy losową wartość ze słownika, ale tylko jeśli nie jest już na liście
            random_answer = random.choice(list(self.merged_dicts.values()))

            if random_answer[0].lower() == correct_answer[0].lower() and random_answer not in answers:
                answers.append(random_answer)

        # losowo przemieszczamy poprawną odpowiedź
        random.shuffle(answers)
        return answers

    def ask_question(self):

        question, correct_answer = self.get_random_question()
        answers = self.generate_answers(correct_answer)

        print(f"\nCo to za rejestracja?: {question}")
        for i, answer in enumerate(answers, start=1):
            print(f"{i}. {answer}")
        while True:
            guess = input("Odpowiedź: ")
            if guess == "0":
                return False
            try:
                guess = int(guess)
                if 1 <= guess <= 4:
                    if guess - 1 == answers.index(correct_answer):
                        print(colorama.Fore.GREEN + "Poprawna odpowiedź!")
                        return True
                    else:
                        print(colorama.Fore.RED + "\nNiepoprawna odpowiedź!")
                        return False
            except ValueError:
                pass


def menu():

    # list_of_dicts = [podlaskie, kujawsko_pomorskie, dolnoslaskie, lodzkie, lubuskie, pomorskie, malopolskie, lubelskie,
    #                  warminsko_mazurskie, opolskie, wielkopolskie, podkarpackie, slaskie, swietokrzyskie, mazowieckie,
    #                  zachodniopomorskie]
    #
    # with open('dicts.pickle', 'wb') as file:
    #     pickle.dump(list_of_dicts, file)


    print("\nWciśnij [j], aby wyjść\n\n1. Podlaskie\n2. Kujawsko-Pomorskie\n3. Dolnośląskie\n4. Łódzkie\n5. Lubuskie\n6. Pomorskie\n"
          "7. Małopolskie\n8. Lubelskie\n9. Warmińsko-Mazurskie\n10. Opolskie\n11. Wielkopolskie\n12. Podkarpackie\n"
          "13. Śląskie\n14. Świętokrzyskie\n15. Mazowieckie\n16. Zachodnipomorskie\n")

    with open('dicts.pickle', 'rb') as file:
        loaded_dicts = pickle.load(file)

    choice = int(input("Wybierz numer województwa do nauki lub j aby wyjść: "))

    for voivode_id, voivode in enumerate(loaded_dicts, start=1):
        if choice == voivode_id and choice in range(1, 17):
            return voivode
        elif choice == 0:
            break

# inicjalizujemy moduł colorama
colorama.init(autoreset=True)
# tworzymy obiekt klasy Voivodeship

while True:
    try:
        quiz = Voivodeship(menu())
        # pytamy użytkownika, czy chce zagrać w quiz
        while True:
            play = int(input("Czy chcesz zagrać ponownie? [1 - Tak ][ 0 - Nie]: "))
            if play == 0:
                break
            elif play == 1:
                # uruchamiamy quiz
                correct = 0
                total = 1
                while True:
                    result = quiz.ask_question()
                    if not result:
                        break
                    elif result:
                        correct += 1
                    total += 1

                # podsumowanie wyników
                print(f"Twój wynik to: {correct}/{total}\n")

        # kończymy program
        print("Dziękujemy za grę!")
    except UnboundLocalError:
        print()
        print("Do zobaczenia!")
        break
    except ValueError:
        print()
        print("Do zobaczenia!")
        break
