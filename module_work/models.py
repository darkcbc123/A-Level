import random
import settings
from exceptions import EnemyDown, GameOver


class Enemy:
    """
    Атрибути класу - level, lives.
    Конструктор приймає тільки аргумент level. Кількість життів = рівень противника.
    """
    def __init__(self, enemy_lives=1, level=1):
        self.level = level
        self.enemy_lives = enemy_lives

    @staticmethod
    def selected_attack():
        """
        повертає випадкове число від 1 до 3
        """
        enemy_random_num = random.randint(1, 3)
        return enemy_random_num

    def enemy_decrease_lives(self):
        """
        зменшує кількість життів на 1. Коли життів стає 0, викликає виняток EnemyDown.
        """
        self.enemy_lives -= 1
        if self.enemy_lives == 0:
            print('Fatality!!!')
            raise EnemyDown


class Player:
    """
    Конструктор приймає ім'я гравця.
    Кількість життів отримується з settings.
    Рахунок дорівнює нулю.
    """
    def __init__(self, name, score=0):
        self.name = name
        self.player_lives = settings.PLAYER_LIVES
        self.score = score

    def player_decrease_lives(self):
        """
        викликає виняток GameOver
        """
        self.player_lives -= 1
        if self.player_lives == 0:
            print('You received damage.')
            print('Game Over!')
            raise GameOver(self.score, self.name)

    @staticmethod
    def selected_attack():
        """
        Player's selected attack
        """
        while True:
            try:
                player_random_num = int(input('Enter a number of char (only 1, 2 or 3): '))
                return player_random_num
            except ValueError:
                print("You can enter only numbers 1-3")
                continue

    @staticmethod
    def fight(attack, defence):
        """
        повертає результат атаки/захисту:
        0 нічия
        -1 aтака/захист невдалі
        1 атака/захист вдалі.
        """
        if attack == defence:
            return 0
        if (attack == 1 and defence == 2) or (attack == 2 and defence == 3) or (attack == 3 and defence == 1):
            return 1
        if (attack == 3 and defence == 2) or (attack == 1 and defence == 3) or (attack == 2 and defence == 1):
            return -1

    def attack(self):
        """
        отримує input (1, 2, 3) від користувача;
        обирає атаку противника з об'екту enemy_obj;
        викликає метод fight();
        Якщо результат 0 - вивести "It's a draw!"
        Якщо 1 = "You attacked successfullyмм!" та зменшує кількість життів противника на 1;
        Якщо -1 = "You missed!"
        """
        print('=====================\nYour turn to attack!\n=====================')
        attack = Player.selected_attack()
        defence = Enemy.selected_attack()
        result_of_attack = self.fight(attack=attack, defence=defence)
        if result_of_attack == 0:
            print('It is draw')
        if result_of_attack == 1:
            Enemy.enemy_decrease_lives(Enemy())
            self.score += 1
            print("You attacked successfully! Enemy lose 1 life!")
        if result_of_attack == -1:
            print("You missed")

    def defence(self):
        """
        такий самий, як метод attack(), тільки в метод fight першим передається атака противника, та
        при вдалій атаці противника викликається метод decrease_lives гравця.
        """
        print('=====================\nEnemy turn to attack!\n=====================')
        attack = Enemy.selected_attack()
        defence = Player.selected_attack()
        result_of_defence = self.fight(attack=attack, defence=defence)
        if result_of_defence == 0:
            print('It is draw')
        if result_of_defence == 1:
            print("You blocked")
        if result_of_defence == -1:
            Player.player_decrease_lives(self)
            print('You received damage.')
