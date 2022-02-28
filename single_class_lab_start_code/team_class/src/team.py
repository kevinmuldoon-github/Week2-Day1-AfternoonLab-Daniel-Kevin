# Team.py

class Team:
    def __init__(self, input_name, input_players, input_coach):
        self.name = input_name
        self.players = input_players
        self.coach = input_coach
        self.points = 0

    def add_player(self, player):
        self.players.append(player)

    def has_player(self, player_name):
        if player_name in self.players:
            return True
        else:
            return False
    
    def play_game(self, win):
        if win == True:
            self.points += 3