import math, sys

def Hp_percentage(pHp, pClass):

	if pClass == "Warrior":
		maxHp = 150
	if pClass == "Box":
		maxHp = 100
	if pClass == "Mage":
		maxHp = 100
	if pClass == "Ninja":
		maxHp = 80

	if pClass == "Archer":
		maxHp = 120

	tweny_percentage = math.ceil((pHp / float(maxHp))*20)
	tweny_spaces = 20 - tweny_percentage
	text = "HP: [" + "=" * int(tweny_percentage) + "  " * int(tweny_spaces) + "] " + str(pHp)
	return text

def wich_cooldown_frame(pCooldown,pCooldownAttribute):
	
	cooldownFrame = 'nocooldown'

	cooldownPercentage = (pCooldown/float(pCooldownAttribute)) * 100

	if cooldownPercentage >= 87.5:
		cooldownFrame = 'cooldown1of8'

	elif cooldownPercentage >=  75:
		cooldownFrame = 'cooldown2of8'

	elif cooldownPercentage >= 62.5:
		cooldownFrame = 'cooldown3of8'

	elif cooldownPercentage >= 50:
		cooldownFrame = 'cooldown4of8'

	elif cooldownPercentage >= 37.5:
		cooldownFrame = 'cooldown5of8'

	elif cooldownPercentage >= 25:
		cooldownFrame = 'cooldown6of8'

	elif cooldownPercentage >= 12.5:
		cooldownFrame = 'cooldown7of8'

	elif cooldownPercentage > 0:
		cooldownFrame = 'cooldown8of8'

	return cooldownFrame

def players_inter_collision(p1X,p1Y,p2X,p2Y):
	#Player 1
	if ((p2X - (p1X + 64)) <= 0 and p2X + 64 - p1X >= 0) and ((p2Y - (p1Y + 64) <= 0) and (p2Y + 64 - p1Y >= 0)):
		return True
	else:
		return False

def ranged_attack_hit(pX,pY,pRangedAttackFrame):
	aX = pRangedAttackFrame[2]
	aY = pRangedAttackFrame[3]
	aL = pRangedAttackFrame[8]
	aH = pRangedAttackFrame[9]
	if ((pX - (aX + aL) <= 0) and (pX + 64 - aX >= 0)) and ((pY - (aY + aH) <= 0) and (pY + 64 - aY >= 0)):
		return True

def ranged_attack_collision(aX,aY,aL,aH,collisionalRectangles):
	for obstacle in collisionalRectangles:
		if ((obstacle[0][0] - (aX + aL)) <= 0	and	(obstacle[0][0] + obstacle[1][0] - aX >= 0)) and ((obstacle[0][1] - (aY + aH) <= 0) and (obstacle[0][1] + obstacle[1][1] - aY >= 0)):
			return True

	
	
def order_list(still_playing_players, players_wins):
	players_wins_lenght = len(players_wins)
	for i in range(players_wins_lenght - 1):
		min = i
		for j in range(i+1,n):
			if players_wins[j] > players_wins[min]:
				min = j

			players_wins[min],players_wins[j] = players_wins[j],players_wins[min]
			still_playing_players[min],still_playing_players[i] = still_playing_players[i],still_playing_players[min]

	
		
