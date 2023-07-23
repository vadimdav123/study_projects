import random
from Art import *

match = 3

class Game:
    def __init__(self, match):
        """Класс для игры 'Камень-ножницы-бумага'."""
        self.match = match
        self.choices = {"к": rock, "н": scissors, "б": paper}
        self.active = True
        self.introduction = "Привет, добро пожаловать в игру 'Камень-ножницы-бумага!'"
        self.leave = "Для выхода из игры напиши q"
        self.score = [0, 0]

    def greeting(self):
        """Приветствие игрока и вывод правил."""
        print(f"{self.introduction}\n{self.leave}")

    def enemy_choice(self):
        """Выбор случайного действия для противника (камень, ножницы или бумага)."""
        en_choice = random.choice(list(self.choices.keys()))
        print(f"Противник выбрал:  \n{self.choices[en_choice]}")
        return en_choice

    def game_total(self, ch1, ch2):
        """Определение результата одной игровой партии (Победа, Поражение или Ничья)."""
        if ch1 == ch2:
            return "Ничья"
        elif (ch1 == "к" and ch2 == "н") or (ch1 == "н" and ch2 == "б") or (ch1 == "б" and ch2 == "к"):
            return "Победа!"
        else:
            return "Поражение"


    def update_score(self, total, score):
        """Обновление счета на основе результата игровой партии."""
        if total == "Поражение":
            score[1] += 1
        elif total == "Победа!":
            score[0] += 1
        return score

    def check_result(self, score, match):
        """Проверка текущего счета и определение победителя."""
        player_score = score[0]
        enemy_score = score[1]
        print(f"{player_score}:{enemy_score}")

        if player_score == match:
            print("Поздравляю, вы победили!")
            return False

        if enemy_score == match:
            print("К сожалению, вы проиграли!")
            return False

        return True

    def get_player_choice(self):
        """Запрос выбора игрока (камень, ножницы или бумага)."""
        choice_player = input("Выберите камень, ножницы или бумагу (к, н, б): ")

        if choice_player == "q":
            print("Выход из игры")
            return None  # Вернуть None, чтобы показать, что пользователь хочет выйти из игры

        elif choice_player in "кнб":
            print(f"\nВаш выбор: {self.choices[choice_player]}")
            return choice_player  # Вернуть выбор игрока (камень, ножницы или бумагу)

        else:
            print("Ошибка! Введите к (камень), н (ножницы) или б (бумагу)")
            return self.get_player_choice()  # Рекурсивно вызвать функцию, чтобы получить корректный выбор

    def game_cycle(self):
        """Основной игровой цикл."""
        self.greeting()
        while self.active:
            choice_player = self.get_player_choice()
            if not(choice_player):
                break
            choice_opponent = self.enemy_choice()
            total = self.game_total(choice_player, choice_opponent)
            print(total)
            self.score = self.update_score(total, self.score)
            self.active = self.check_result(self.score, self.match)


if __name__ == "__main__":
    game = Game(match)
    game.game_cycle()
