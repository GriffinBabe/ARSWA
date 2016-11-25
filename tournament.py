	#Tournament Mode
	if gamemode == 't':
		#Loadings
		players_number = 0
		players_number_text_count = 1
		players_list = []
		players_classes = []
		players_wins = []
		eliminated = []
		existing_tree_players_number = [2,4,8,16]
		tree_plat
		pools_best_of = 0
		brackets_best_of = 0
		pools_eliminations = 0
		players_to_eliminate_number = 0

		#Options
		while True:
			players_number = raw_input('How many players are there: ')
			if type(players_number) == int:
				if players_number <= max_players:
					break
			else:
				print('Invalid or too big number of players (max 16)...')

		while True:
			pools_best_of = raw_input('Best of for pools (odd number): ')
			if pools_best_of in existing_best_of:
				break
			else:
				print('Invalid or too big number: ')

		while True:
			brackets_best_of = raw_input('Best of for brackets (odd number): ')
			if pools_best_of in existing_best_of:
				break
			else:
				print('Invalid or too big number: ')

		#Choosing Names and Classes
		for i in range(players_number):

			pName = print('Player '+players_number_text_count+' name: ')

			if pName in antoine_names:
				print('\nGRIFFON PUTAIN !')
				print('+ mention: casu\n')
			if pName in simon_names:
				print('\nJ\'ai essaye de mettre des caracteres en chinois mais Python les accepte pas et j\'ai la flemme de chercher')
				print('+ mention: Robot\n')

			if pName in igor_names:
				print('\nO Igorus, deuxiemme createur du jeu')
				print('+ mention: Ce dieux la est special, sur les 7 jours il n\'a travaille que dans 3 parce qu\'il est paresseux\n')

			if pName in alexandre_names:
				print('\nBeta testeur numero 1, attention les gars !')
				print('+ mention: tchiiiip\n')

			if pName in antoni_names:
				print('\nSi il est numero 1 on dit que ca compte pas, ok les gars?')
				print('+ mention: FAP FAP FAP FAP FAP\n')

			if pName in darius_names:
				print('\nO Darius, createur du jeu, qui se suce la bite langoureusement')
				print('+ mention: GRIFFON PUTAIN !!\n')

			while True:
				pClass = raw_input('Player '+players_number_text_count+' class ?')
				if pClass in existing_class:
					break
				else:
					print('Class doesn\'t exists... ')
			

			players_number_text_count += 1
			players_list.append(pName)
			players_classes.append(pClass)

		players_class_dict = {}

		#Creating a name:class dictionary
		for i in range(len(players_list)):
			players_class_dict[players_list[i]] = players_classes[i]

		#Creating the wins list
		for i in range(len(players_list)):
			players_wins.append(0)

		
		#Pool eliminations
		while True:
			for i in range(len(existing_tree_players_number)):
		
				if players_number = existing_tree_players_number:

					players_to_eliminate_number = 0
					break

				if players_number > existing_tree_players_number:

					players_to_eliminate_number = players_number - existing_tree_players_number[i]
					break


			still_playing_players = players_list

			while players_to_eliminate > 0:

				still_playing_players_number = len(still_playing_players)
				not_played_players = still_playing_player

				

				print('Now we have to eliminate '+players_to_eliminate_number+' player(s)')
				print('Crating match pairs...')
				
				while len(not_played_players) > 0:

					not_played_players_number = len(not_played_players)

					p1Name = not_played_players[random.randint(0,not_played_players_number-1)]:
						not_played_players.remove(p1Name)
					p2Name = not_played_players[random.randint(0,not_played_players_number-1)]:
						not_played_players.remove(p2Name)

					rounds_to_win = int(math.ceil(pools_best_of/float(2)))

					print('For this match we have '+p1Name+' against '+p2Name+'.')

					while True:
						localp1Wins = 0
						localp2Wins = 0

						winner = main(players_class_dict[p1Name],players_class_dict[p2Name],p1Name,p2Name,rounds_to_win,localp1Wins,localp2Wins)

						if winner == p1Name:
							players_wins[players_names.index(p1Name)] += 1
							localp1Wins += 1

						if winner == p2Name:
							players_wins[players_names.index(p2Name)] += 1
							localp2Wins += 1

						if localp1Wins == rounds_to_win or localp2Wins == rounds_to_wins:
							break
				
				
				still_playing_players, players_wins = order_list(still_playing_players, players_wins)
				
				print('--------------------Score Board----------------')

				for i in len(still_playing_players):
					print((i+1)+'. '+still_playing_players[i]+' score: 'players_wins[i])

				for i in range(len(still_playing_players)-players_to_eliminate-1,len(still_playing_players)-2):

					if players_wins[i] == players_wins[i+1]:

						print('We have '+still_playing_players[i]+' and '+still_playing_players[i+1]+' having the same amount of wins, let\'s match them')

						while True:
							localp1Wins = 0
							localp2Wins = 0

							p1Name = still_playing_players[i]
							p2Name = still_playing_players[i+1]

							winner = main(players_class_dict[p1Name],players_class_dict[p2Name],p1Name,p2Name,rounds_to_win,localp1Wins,localp2Wins)

							if winner == p1Name:
								localp1Wins += 1
							if winner == p2Name:
								localp2Wins += 1

