import csv
import random
from collections import Counter

#where we'll store the inputs.
class Games:
	week = ''	
	visiting_team = ''
	home_team = ''
	home_we = 0
	sim_result = ''

games_dict = {}

#lists to store results.
div_winner_list = []
div_count_list = []

#read the CSV with the games and probabilities.
r = csv.reader(open('nfc_east.csv'))
gamelines = [l for l in r]

#set up the game class with the CSV data.
for x in range(1,len(gamelines)):
	games_dict[x] = Games()
	games_dict[x].week = gamelines[x][0]
	games_dict[x].visiting_team = gamelines[x][1]
	games_dict[x].home_team = gamelines[x][2]
	games_dict[x].home_we = float(gamelines[x][3])
	games_dict[x].sim_result = ''

#iterate 100,000 times.
for i in range(0,100000):
	#set up the starting wins totals.
	was_wins = 6
	dal_wins = 5
	phi_wins = 4
	nyg_wins = 3 
	
	#run the sim for each game.
	for x in games_dict:
		if random.random() >= games_dict[x].home_we:
			games_dict[x].sim_result = games_dict[x].visiting_team
		else:
			games_dict[x].sim_result = games_dict[x].home_team

		#add the results to the win totals
		if games_dict[x].sim_result == 'Redskins':
			was_wins += 1
		elif games_dict[x].sim_result == 'Cowboys':
			dal_wins += 1
		elif games_dict[x].sim_result == 'Eagles':
			phi_wins += 1
		elif games_dict[x].sim_result == "Giants":
			nyg_wins += 1

	#figure out the highest value
	highest_score = 0
	highest_score = max(int(was_wins), int(dal_wins), int(phi_wins), int(nyg_wins))
	
	#initialize variable.
	div_winner = ''
	
	#add the winners
	if nyg_wins == highest_score:
		div_winner = div_winner + "Giants "
	if was_wins == highest_score:
		div_winner = div_winner + "Redskins "
	if phi_wins == highest_score:
		div_winner = div_winner + "Cowboys "
	if dal_wins == highest_score:
		div_winner = div_winner + "Eagles "

	#append the winner and win totals to the list.
	div_winner_list.append(div_winner)
	div_count_list.append(highest_score)

#print results
print dict(Counter(div_winner_list))
print dict(Counter(div_count_list))
