import time
from datetime import datetime
from controllers.tournament import create_next_round
from models.player import Player
from models.tournament import Tournament
from views.game import winner_game_is
from views.player import PlayerView
from views.table import myScoreTable


def show_all_games(trn: Tournament):
    for rnd in trn.tournament_rounds:
        print(rnd)
        for i, game in enumerate(rnd.games):
            print(f"{i + 1}-{game}")


def show_scores_table(trn: Tournament):
    myScoreTable.clear_rows()
    trn.tournament_players.sort(key=lambda player: player.rank, reverse=True)
    trn.tournament_players.sort(key=lambda player: trn.tournament_participants[player.number], reverse=True)

    for p in trn.tournament_players:
        myScoreTable.add_row([p.number, trn.tournament_participants[p.number], p.rank])
    print(myScoreTable)


def show_round_menu(trn: Tournament):
    """The round menu with the different options depending on whether the round is completed or not."""
    print("")
    print("################")
    print("Show Round Menu")
    print("################")
    while True:
        time.sleep(1)
        print("")
        print("What do you want to do?")
        print("1- End round")
        print("2- Next round")
        print("3- Change players ranking")
        print("4- Show current scores")
        print("0- Return to previous menu ")
        choice = input("Choose option: ")
        if choice == "0":
            trn.save_tournaments()
            print("Returning to previous menu")
            break
        elif choice == "1":
            for rnd in trn.tournament_rounds:
                if rnd.start_date_time == "" and rnd.end_date_time == "" and rnd.games == []:
                    print("Choose Next round to generate games.")
                    break
                elif rnd.start_date_time != "" and rnd.end_date_time == "" and rnd.games != []:
                    for game in rnd.games:
                        winner_game_is(game, trn.tournament_participants)
                        print("")
                        print(game)
                        print("/Game completed/")
                    time.sleep(2)
                    rnd.end_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    print(f"{rnd} : //completed//")
                    show_scores_table(trn)
                    if rnd == trn.tournament_rounds[-1]:
                        trn.tournament_end_date = rnd.end_date_time
                        print("The tournament is completed")
                    trn.save_tournaments()
                elif rnd.start_date_time != "" and rnd.end_date_time != "":
                    print(f"{rnd} : //completed//")
                else:
                    time.sleep(1)
                    print(f"{rnd} : not started yet")
            show_all_games(trn)
        elif choice == "2":
            if trn.tournament_rounds[-1].start_date_time != "" and trn.tournament_rounds[-1].end_date_time != "":
                print("All rounds are completed.")
            else:
                not_started_rounds = []
                for rnd in trn.tournament_rounds:
                    if rnd.start_date_time == "" and rnd.end_date_time == "" and rnd.games == []:
                        not_started_rounds.append(rnd)
                        next_round = not_started_rounds[0]
                        print(next_round.round_name)
                        create_next_round(next_round, trn)
                        trn.save_tournaments()
                        for game in next_round.games:
                            print(game)
                        print("Ready to start the new round !")
                        break
                    elif rnd.start_date_time != "" and rnd.end_date_time == "":
                        print(f"You have to end {rnd.round_name} first.")
                        break
                    elif rnd.start_date_time != "" and rnd.end_date_time == "" and rnd == trn.tournament_rounds[-1]:
                        print("It's the last round.")
                        break
        elif choice == "3":
            last_round = trn.tournament_rounds[-1]
            if last_round.end_date_time != "":
                PlayerView.change_rank_players()
                Player.serialize_players()
            else:
                print("The tournament is not completed yet")
        elif choice == "4":
            show_scores_table(trn)
        else:
            print("Wrong choice. Try again")
