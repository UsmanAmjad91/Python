class Player:
    max_hp = 5000

player1 = Player()
print(player1.max_hp)
player2 = Player()
print(player2.max_hp)


class Players:
    max_hp = 5000

    def __init__(self, name ,max_hp):
        self.name = name
        self.max_hp = Players.max_hp
        self.score = 0
        player1 = Players("Usman", 7000)
        player2 = Players("Amjad", 8000)
        print(f"Player {player1.name} created with max HP: {player1.max_hp}")
        print(f"Player {player2.name} created with max HP: {player2.max_hp}")
        