"""
Exceptions for the Game
"""


class GameOver(Exception):
    """
    унаслідований від Exception. В класі має бути реалізований метод для збереження фінального рахунку гри по
    її завершенню
    """
    def __init__(self, score, name):
        self.score = score
        self.name = name


class EnemyDown(Exception):
    """
    унаслідований від Exception. Функціонал не потрібен, тільки декларація.
    """
