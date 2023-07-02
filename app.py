from constants import TEAMS, PLAYERS;
import copy;
import random; 

def get_data(players: list):
    myplayers = copy.copy(players);
    return myplayers;

def process_data(players: list):   
    for player in players:
        # Height: This should be saved as an integer. Ex 39 inches to 39
        player['height'] = int(player['height'].split(' ')[0]);
        # This should be saved as a boolean value (True or False)
        player['experience'] = True if (player['experience'] == 'YES') else False
        # Guardian: split up the guardian string into a List
        player['guardians'] = list(player['guardians'].split(' and '));
    return players;
def balance_teams(players: list, teams: list):
    total_players = len(players);
    total_teams = len(teams);
    while((total_players % total_teams) != 0 ):
        print(f"We can not divide the players into {total_teams} teams equally!");
        print("We are gonna remove one player");
        total_players -= 1;
    maximum_player = total_players / total_teams;
    teams_dictionary = { team : 0 for team in teams };
    print(teams_dictionary);
    for player in players:
        player['team'] = "";
        while(player['team'] == ""):
            number = random.randint(0,total_teams-1); # Get a random number
            if(teams_dictionary[teams[number]] < maximum_player):
                player['team'] = teams[number]; # Assign a team for player
                teams_dictionary[teams[number]] += 1; # Update the number of players in a team
    print(teams_dictionary);
    return players, teams_dictionary;

def display(players: list, teams_dictionary: dict):
    for team in teams_dictionary.keys():
        for player in players:
            if player['team'] == team:
                print(f"{team} picked {player['name']}");
        print("****************************");
if __name__ == "__main__":
    players, teams_dictionary = balance_teams(process_data(get_data(PLAYERS)),TEAMS);
    display(players, teams_dictionary);


