def score_case_ennemi(grid,case,side):
	# calcule le nombre d'ennemis autour d'une case
	s = 0
	for k in [-1, 0, 1]:
        if (case[0] + k) >= 10 or (case[0] + k) < 0:
            continue
        for l in [-1, 0, 1]:
            if (case[1] + l) >= 10 or (case[1] + l) < 0:
                continue
            if grid[case[0]+k][case[1]+l] == side%2 + 1:
            	s += 1
    return s

def ia_ordonnee(game, side0):
	# Cette ia a pour but de jouer là où elle pourra manger le plus
	# d'ennemis. Si plusieurs cases sont à égalité, elle choisira la
	# première qui est dans son ORDRE (liste des cases ordonnée d'une 
	# manière que je vous laisse deviner). L'ordre est changeable en
	# début de programme (c'est la variable ordre0).
	side = int(side0[-1]) # pour obtenir juste le 1 ou le 2
	if game["player_"+str(side)]["misc"] == {}:
		# on crée l'ordre utilisé
		ordre0 = []
		for i in range(10):
			ordre0.append([i,i])
		for i in range(4):
			for j in range(4-i):
				ordre0 += [[4-i,3-i-j], [5+i,6+i+j], [3-i-j,4-i], [6+i+j,5+i]]
		for i in range(50):
			ordre0.append([ordre0[i][0], 9-ordre0[i][1]])
		# on conserve cet ordre dans misc
		game["player_"+str(side)]["misc"] = ordre0
	ordre = game["player_"+str(side)]["misc"] # pour alléger l'écriture
	s_max, choix = -1, [0,0]
	for i in range(100):
		if game["grid"] [ordre[i][0]] [ordre[i][1]] != 0:
		#s'il y a déjà un pion
			continue
		s_temps = score_case_ennemi(game["grid"],ordre[i],side)
		if s_temps > s_max:
			#regarde les cases autour et s'il y a un pion allié alors valide le coup
			for k in [-1,0,1]:
		    	for l in [-1,0,1]:
		    		if (ordre[i][0] + k) >= 10 or (ordre[i][0] + k) < 0:
            			continue
                	if (ordre[i][1] + l) >= 10 or (ordre[i][1] + l) < 0:
            			continue
                	if game["grid"][ordre[i][0]+k][ordre[i][1]+l] == side:
                		s_max, choix = s_temps, [ordre[i][0],ordre[i][1]]
    if choix == [0,0]:
    	return False
    else:
    	return choix
