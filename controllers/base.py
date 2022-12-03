"""Define the main controller."""
import random
from datetime import datetime
from typing import List
from models.player import Player
from models.game import Game
from models.round import Round
from models.tournament import Tournament
from views.base import View

NUMBERS_PLAYERS = 4

class Controller:
    """Main controller."""
    def __init__(self, tournament: Tournament, view: View):
        """Has a Tournament, a list of players and a view."""
        # models
        self.tournament = tournament
        self.players = self.tournament.tournament_players

        # views
        self.view = view

    def get_players(self):
        """Get some players."""
        while len(self.players) < NUMBERS_PLAYERS:
            info = self.view.prompt_for_player()
            if not info:
                return
            player = Player(info)
            self.players.append(player)

    def create_round(self):
        """"""
        info = self.view.round_info()
        if not info:
            return
        round = Round(info)
        self.tournament.tournament_rounds.append(round)

    def generate_pairs_first_round(self):
        """Create pairs for the first round (swiss rules)."""
        self.tournament.tournament_rounds[0] = []
        self.players = sorted(self.players, key=lambda player: player.rank)
        half = len(self.players) // 2
        upper_list = self.players[:half]
        lower_list = self.players[half:]
        for i, j in zip(range(len(upper_list)), range(len(lower_list))):
            self.tournament.tournament_rounds[0].append(Game(upper_list[i], lower_list[j]))
        return self.tournament.tournament_rounds[0]

    def players_for_next_round(self):
        """Create list of the winners."""
        winners_list = []
        for round in self.tournament.tournament_rounds:
            for game in round.games:
                if self.view.winner_game_is(game) == 1:
                    winners_list.append(game.player_1)
                elif self.view.winner_game_is(game) == 2:
                    winners_list.append(game.player_2)
                else:
                    print("Choisir 1 ou 2.")
        return winners_list

    def generate_pairs_next_rounds(self):
        """Create pairs for the others rounds (swiss rules)."""
        pairs_next_rounds = []
        winners = self.players_for_next_round()
        list_scores = [player.score for player in winners]
        for score in list_scores:
            if list_scores.count(score) > 1:
                winners = sorted(winners, key=lambda player: player.rank)
            else:
                winners = sorted(winners, key=lambda player: player.score, reverse=True)
        for i in range(len(winners)-1):
            if (winners.index(winners[i]) % 2) == 0:
                pairs_next_rounds.append((winners[i], winners[i+1]))
        return pairs_next_rounds

    def set_scores(self, list_games):
        """Set the players scores at the end of the games."""
        for game in list_games:
            if self.view.winner_game_is(game) == 1:
                game.player_1.score += 1
                game.player_2.score += 0
            elif self.view.winner_game_is(game) == 2:
                game.player_1.score += 0
                game.player_2.score += 1
            else:
                game.player_1.score += 0.5
                game.player_2.score += 0.5

    def run(self):
        """Run the tournament."""
        running = True
        while running:
            if self.view.main_menu() == 1:
                self.tournament.tournament_start_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.view.tournament_info()
                self.get_players()
                self.create_round()
                self.tournament.tournament_rounds[0].end_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.generate_pairs_first_round()
                print(self.tournament.tournament_rounds[0])
                if self.view.main_menu() == 2:
                    #self.tournament.tournament_rounds[0].end_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    for game in self.tournament.tournament_rounds[0]:
                        self.view.winner_game_is(game)
                    self.set_scores(self.tournament.tournament_rounds[0])
                    if self.view.main_menu() == 3:
                        self.players_for_next_round()
                        self.generate_pairs_next_rounds()
                        if self.view.main_menu() == 4:
                            self.tournament.tournament_end_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            self.view.show_winner_tournament(self.players_for_next_round()[0])
                            running = False
            else:
                print("Aucun tournoi n'a été commencé.")
                self.view.main_menu()


























