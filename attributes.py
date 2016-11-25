import pygame, sys, math
from pygame.locals import *

def map_1():
	#grav, p1startX, p1startY, p2startX, p2startY
	mapAttributes = [0.25,200,750,1000,750]
	return mapAttributes

def map_1_obstacles():
	#is a list, in the second where [[obstacle],[another obstacle]] and in each 'obstacle' [oX,oY],[oL,oH]
	collisionalRectanglesList = [[[575,685],[50,105]],[[0,675],[350,25]],[[850,675],[350,25]],[[350,550],[500,25]],[[0,450],[250,25]],[[950,450],[250,25]],[[200,350],[800,25]],[[0,250],[100,25]],[[1100,250],[100,25]]]
#[420,710],[400,15]],[[800,610],[450,15]],[[0,610],[450,15]],
	collisionalRectanglesTuple = [(420,710,400,15),(800,610,450,15),(0,610,450,15),(600,700,200,200)]
	mapGroundImg = pygame.image.load('32x32/ground.png')


	return collisionalRectanglesList, collisionalRectanglesTuple, mapGroundImg

def class_attributes(pclass):

	if pclass == 'Warrior':
		classImgFront = pygame.image.load('64x64/warriorFront.png')
		classImgRight = pygame.image.load('64x64/warriorRight.png')
		classImgLeft = pygame.image.load('64x64/warriorLeft.png')
		classImgBasicAttackRight = pygame.image.load('64x64/warriorAttackRight.png')
		classImgBasicAttackLeft = pygame.image.load('64x64/warriorAttackLeft.png')
		classImgDmg = pygame.image.load('64x64/warriorDmg.png')
		classSpell1Img = pygame.image.load('64x64/bubulle.png')
		classSpell2Img = pygame.image.load('64x64/warriorFront.png')
		classBasicAttackIcon = pygame.image.load('32x32/warriorBasicAttackIcon.png')
		classSpell1Icon = pygame.image.load('32x32/warriorSpell1Icon.png')
		classSpell2Icon = pygame.image.load('32x32/warriorSpell2Icon.png')
		#acceleration, max_speed, jump speed, jumps available, HP
		classAttributes = [0.30,5,10,1,150]

	if pclass == 'Box':
		classImgFront = pygame.image.load('64x64/BoxFront.png')
		classImgRight = pygame.image.load('64x64/BoxRight.png')
		classImgLeft = pygame.image.load('64x64/BoxLeft.png')
		classImgBasicAttackRight = pygame.image.load('64x64/BoxFront.png')
		classImgBasicAttackLeft = pygame.image.load('64x64/BoxFront.png')
		classImgDmg = pygame.image.load('64x64/BoxFront.png')
		classSpell1Img = pygame.image.load('64x64/BoxFront.png')
		classSpell2Img = pygame.image.load('64x64/BoxFront.png')
		classBasicAttackIcon = pygame.image.load('32x32/warriorBasicAttackIcon.png')
		classSpell1Icon = pygame.image.load('32x32/warriorBasicAttackIcon.png')
		classSpell2Icon = pygame.image.load('32x32/warriorBasicAttackIcon.png')
		classAttributes = [0.50,8,10,1,100]

	if pclass == 'Mage':
		classImgFront = pygame.image.load('64x64/mageFront.png')
		classImgRight = pygame.image.load('64x64/mageRight.png')
		classImgLeft = pygame.image.load('64x64/mageLeft.png')
		classImgBasicAttackRight = pygame.image.load('64x64/mageLeft.png')
		classImgBasicAttackLeft = pygame.image.load('64x64/mageRight.png')
		classImgDmg = pygame.image.load('64x64/mageDmg.png')
		classSpell1Img = pygame.image.load('64x64/bubulle.png')
		classSpell2ImgRight = '32x32/blueFireballRight.png'
		classSpell2ImgLeft = '32x32/blueFireballLeft.png'
		classSpell2Img = [classSpell2ImgRight, classSpell2ImgLeft]
		classBasicAttackIcon = pygame.image.load('32x32/mageBasicAttackIcon.png')
		classSpell1Icon = pygame.image.load('32x32/mageSpell1Icon.png')
		classSpell2Icon = pygame.image.load('32x32/mageSpell2Icon.png')
		classAttributes = [0.25,7,10,1,100]

	if pclass == 'Ninja':
		classImgFront = pygame.image.load('64x64/ninjaFront.png')
		classImgRight = pygame.image.load('64x64/ninjaRight.png')
		classImgLeft = pygame.image.load('64x64/ninjaLeft.png')
		classImgBasicAttackRight = pygame.image.load('64x64/ninjaRight.png')
		classImgBasicAttackLeft = pygame.image.load('64x64/ninjaLeft.png')
		classImgDmg = pygame.image.load('64x64/ninjaFront.png')
		classSpell1Img = pygame.image.load('64x64/ninjaFront.png')
		classSpell2Img = pygame.image.load('64x64/ninjaFront.png')
		classBasicAttackIcon = pygame.image.load('32x32/warriorBasicAttackIcon.png')
		classSpell1Icon = pygame.image.load('32x32/warriorBasicAttackIcon.png')
		classSpell2Icon = pygame.image.load('32x32/warriorBasicAttackIcon.png')
		classAttributes = [0.40,8,10,2,80]

	if pclass == 'Archer':
		classImgFront = pygame.image.load('64x64/archerFront.png')
		classImgRight = pygame.image.load('64x64/archerRight.png')
		classImgLeft = pygame.image.load('64x64/archerLeft.png')
		classImgBasicAttackRight = pygame.image.load('64x64/archerAttackRight.png')
		classImgBasicAttackLeft = pygame.image.load('64x64/archerAttackLeft.png')
		classImgDmg = pygame.image.load('64x64/archerDmg.png')
		classSpell1ImgRight = '32x32/slowArrow1Right.png'
		classSpell1ImgLeft = '32x32/slowArrow1Left.png'
		classSpell1Img = [classSpell1ImgRight,classSpell1ImgLeft]
		classSpell2ImgRight = '32x32/trap.png'
		classSpell2ImgLeft = '32x32/trap.png'
		classSpell2Img = [classSpell2ImgRight,classSpell2ImgLeft]
		classBasicAttackIcon = pygame.image.load('32x32/archerBasicAttackIcon.png')
		classSpell1Icon = pygame.image.load('32x32/archerSpell1Icon.png')
		classSpell2Icon = pygame.image.load('32x32/archerSpell2Icon.png')
		classAttributes = [0.35,8,10,1,120]

	return (classAttributes,classImgFront,classImgRight,classImgLeft, classImgBasicAttackRight, classImgBasicAttackLeft, classImgDmg, classSpell1Img, classSpell2Img, classBasicAttackIcon, classSpell1Icon, classSpell2Icon)

def basic_attack(pclass):
	if pclass == 'Warrior':
		#Exists,Dmg,Cooldown, HitBox Lenght, Hitbox Height, ranged or not, speed, Right Frame Name, Left Frame Name
		attackAttributes = ['yes',35,60,64,32,'no',0,15]

	if pclass == 'Box':
		attackAttributes = ['no']

	if pclass == 'Mage':
		attackAttributes = ['yes',30,75,64,32,'yes',12,0,'32x32/fireball1right.png','32x32/fireball1left.png']

	if pclass == 'Ninja':
		attackAttributes = ['yes',15,45,64,32,'yes',15,0,'32x32/ninjaShuriken.png','32x32/ninjaShuriken.png']

	if pclass == 'Archer':
		attackAttributes = ['yes',15,45,64,32,'yes',15,0,'32x32/arrow1Right.png','32x32/arrow1Left.png']

	return attackAttributes

def spell_1(pclass):
	
	if pclass == 'Warrior':
		#DmgDealer?,Dmg,Cooldown,Hitbox lenght, Hitbox Height,Aura,Duration,Name, mooving frame?, frame X, frame Y,X speed,Y speed
		spell1Attributes = ['no',0,360,0,0,'yes',60,'Immunity','no',-32,-32,0,0]
	if pclass == 'Box':
		spell1Attributes = ['no',25,0,0,0,'no',0,'none','no',0,0,0,0]

	if pclass == 'Mage':
		spell1Attributes = ['no',0,900,0,0,'no',0,'none','Recall',0,0,0,0]

	if pclass == 'Ninja':
		spell1Attributes = ['no',0,0,0,0,'no',0,'none','no',0,0,0,0]

	if pclass == 'Archer':
		spell1Attributes = ['yes',30,360,64,32,'yes',90,'Slow Arrow','no',0,0,12,0]

	return spell1Attributes

def spell_2(pclass):
	
	if pclass == 'Warrior':
		spell2Attributes = ['no',25,180,0,0,'yes',30,'Dash','no',0,0,0,0]
	if pclass == 'Box':
		spell2Attributes = ['no',0,0,0,0,'no',0,'none','no',0,0,0,0]
	if pclass == 'Mage':
		spell2Attributes = ['yes',20,600,64,32,'no',90,'Freezer','no',0,0,10,0]
	if pclass == 'Ninja':
		spell2Attributes = ['no',0,0,0,0,'no',0,'none','no',0,0,0,0]
	if pclass == 'Archer':
		spell2Attributes = ['no',0,1200,64,32,'yes',120,'Root','no',0,0,0,0]

	return spell2Attributes

def buffs_frames():
	buff1Frame = '64x64/bubulle.png'
	buff2Frame = '64x64/warriorFront.png'
	buff3Frame = '64x64/root.png'
	buff4Frame = '64x64/iceBlock.png'
	buffsFrames = [buff1Frame,buff2Frame,buff3Frame,buff4Frame]
	return buffsFrames

