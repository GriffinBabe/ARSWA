import math, sys

def keyConfigMaker():
	#key loadings
	keyboardconfig = open('keyboardconfig.txt','r')
	configlines = keyboardconfig.read().splitlines()
	keyconfig = {}
	#Player1
	keyconfig['K_q'] = configlines[20]
	keyconfig['K_d'] = configlines[21]
	keyconfig['K_z'] = configlines[22]
	keyconfig['K_SPACE'] = configlines[23]
	keyconfig['K_a'] = configlines[24]
	keyconfig['K_e'] = configlines[25]
	keyconfig['K_r'] = configlines[26]
	#Player2
	keyconfig['K_LEFT'] = configlines[29]
	keyconfig['K_RIGHT'] = configlines[30]
	keyconfig['K_UP'] = configlines[31]
	keyconfig['K_KP0'] = configlines[32]
	keyconfig['K_KP1'] = configlines[33]
	keyconfig['K_KP2'] = configlines[34]
	keyconfig['K_KP3'] = configlines[35]
	
	return keyconfig

