"""
Концепція:**
1. При запуску файлу game.py запропонувати користувачу ввести своє ім'я.
2. Запропонувати користувачу ввести **start** для початку гри.
3. Хід починається з атаки гравця:
-гравець обирає чаклуна(1), воїна(2) чи розбійника(3).
-Вибір противника обирається автоматично.
-Чаклун перемагає воїна. Воїн перемагає розбійника. Розбійник перемагає чаклуна.
-Після атаки вивести результат атаки - влучив, промахнувся, нічия. Нічия у випадку, якщо обрані однакові класи.
-Далі атакує противник, користувач обирає захист - механізм той самий.
4. Після успішної атаки у противника зменшуеться кількість життів. Гравець отримує 1 очко.
5. Після невдалого захисту гравець втрачає одне життя.
6. Коли у гравця закінчуються життя - ігра завершується.
7. Коли у противника закінчуються життя - гравець отримує додатково +5 очків і генерується новий противник.
8. При завершенні гри вивести результат на екран.
"""

import sys
from datetime import date
import settings


from models import Player, Enemy
from exceptions import GameOver, EnemyDown


def play():
    player_name = input('Enter your name ')
    while True:
        game_menu = input(f"Hello, {player_name}. Enter 'start' to begin the game or 'help' to check more options: ")
        if game_menu in settings.main_menu and game_menu == 'start':
            break
        if game_menu in settings.main_menu and game_menu == 'score':
            with open('score.txt', 'r', encoding="utf8") as file_read:
                for line in file_read:
                    print(f"{line}\n")
            continue
        if game_menu in settings.main_menu and game_menu == 'help':
            print(f"You can use these commands: {settings.main_menu}")
            continue
        if game_menu in settings.main_menu and game_menu == 'exit':
            print("Goodbye ")
            sys.exit()
        if game_menu not in settings.main_menu:
            print("Can't find anything! Please enter 'help'.")
            continue
    player = Player(player_name)
    level = 1
    enemy = Enemy()
    print(f"Your enemy has {enemy.enemy_lives} lives and {enemy.level} level!")
    while True:
        try:
            player.attack()
            player.defence()
        except EnemyDown:
            level += 1
            enemy = Enemy(level=level, enemy_lives=level)
            player.score += 5
            print(f"Your score is {player.score}")
            print("Next one will be harder")
            print(f"Now your enemy has {enemy.enemy_lives} lives and level {enemy.level}!")


if __name__ == "__main__":
    while True:
        try:
            play()
        except GameOver as err:
            if err.score > 0:
                with open("score.txt", "a", encoding="utf8") as file:
                    print(f'Your total score is {err.score}. Well done!')
                    file.write(f"Date --- {date.today()}  {err.name}, your score is {err.score} points!!! ")
    