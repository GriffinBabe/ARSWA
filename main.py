import pygame, sys, math
from pygame.locals import *
import pygame.key
from attributes import map_1, map_1_obstacles, class_attributes, basic_attack, spell_1, spell_2, buffs_frames
from maths import Hp_percentage, wich_cooldown_frame, players_inter_collision, ranged_attack_hit, ranged_attack_collision
from configmaker import keyConfigMaker

pygame.init()

#frames per second setting
FPS = 60
fpsClock = pygame.time.Clock()

#Colors setup
gray = pygame.Color(128,128,128)
black = pygame.Color(0,0,0)
olive = pygame.Color(128,128,0)
white = pygame.Color(255,255,255)
alpha = pygame.Color(0,0,0,0)
red = pygame.Color(255,0,0)
blue = pygame.Color(50,150,230)
brown = pygame.Color(100,30,30)

#Memes
antoine_names = ['antoine','Antoine','Griffon','griffon','poulpy','Poulpy','patapoulpe','Patapoulpe','pata','Pata']
simon_names = ['simon','Simon','sim0n','Sim0n']
alexandre_names = ['deadamer','Deadamer','alexandre','Alexandre','deadamer07','Deadamer07','frouze','Frouze']
igor_names = ['igor','Igor','igigor','Igigor','grosPD']
antoni_names = ['polak','Polak','Antoni','antoni','Antik','antik','Antik554','antik554','antek','Antek','Anal Rupture','anal rupture','olow','Olow','cetteListeEstLonguePutainJeVaisPasTeLouper']
darius_names = ['Darius','darius','DarkQ','darkQ','GriffinBabe','BeautifulGriffin']


#Window setup
DISPLAYSURF = pygame.display.set_mode((1200, 800),0,32)
pygame.display.set_caption('Project ARSWA')

#font
fontObj = pygame.font.SysFont('freesansbold.tff',32) #creates a pygame.font.Font object
#textSurfaceObj = fontObj.render('Projet ARSWA',True,olive,alpha) #renders it
#textRectObj = textSurfaceObj.get_rect()
#textRectObj.center = (600,100)



def main(p1class,p2class,p1Name,p2Name,mapNumber,p1Wins,p2Wins):


    #General loadings

    framecount = 0
    seconds = 0

    player1ClassChange = False
    player2ClassChange = False

    keyconfig = keyConfigMaker()

    grav, p1X, p1Y, p2X, p2Y = map_1()

    psWinsSurfaceObj = fontObj.render(str(p1Wins)+' - '+str(p2Wins),True,olive,black)
    psWinsRectObj = psWinsSurfaceObj.get_rect()
    psWinsRectObj.center = (600,100)

    buffsFrames = buffs_frames()


    #players attributes loadings
    p1Attributes, p1ImgFront, p1ImgRight, p1ImgLeft, p1BasicAttackRight, p1BasicAttackLeft, p1ImgDmg, p1Spell1Img, p1Spell2Img, p1BasicAttackIcon, p1Spell1Icon, p1Spell2Icon = class_attributes(p1class)
    p2Attributes, p2ImgFront, p2ImgRight, p2ImgLeft, p2BasicAttackRight, p2BasicAttackLeft, p2ImgDmg, p2Spell1Img, p2Spell2Img, p2BasicAttackIcon, p2Spell1Icon, p2Spell2Icon = class_attributes(p2class)

    p1AttackAttributes = basic_attack(p1class)
    p2AttackAttributes = basic_attack(p2class)

    p1Spell1Attributes = spell_1(p1class)
    p2Spell1Attributes = spell_1(p2class)

    p1Spell2Attributes = spell_2(p1class)
    p2Spell2Attributes = spell_2(p2class)


    collisionalRectangles,collisionalRectanglesTuple, groundImg = map_1_obstacles()

    p1Positions = []
    p2Positions = []

    p1XS = 0
    p1fXS = 0
    p1YS = 0
    p1fYS = 0
    p2XS = 0
    p2fXS = 0
    p2YS = 0
    p2fYS = 0

    grav = 0.50

    p1BasicAttackCooldown = 0
    p2BasicAttackCooldown = 0

    p1Spell1Cooldown = 0
    p2Spell1Cooldown = 0

    p1Spell2Cooldown = 0
    p2Spell2Cooldown = 0

    p1Cooldowns = [p1BasicAttackCooldown,p1Spell1Cooldown,p1Spell2Cooldown]
    p2Cooldowns = [p2BasicAttackCooldown,p2Spell1Cooldown,p2Spell2Cooldown]

    p1BasicAttackFrameDuration = 0
    p2BasicAttackFrameDuration = 0

    p1Spell1FrameDuration = 0
    p2Spell1FrameDuration = 0

    p1Spell2FrameDuration = 0
    p2Spell2FrameDuration = 0

    p1DmgFrameDuration = 0
    p2DmgFrameDuration = 0

    p1FramesDurations = [p1DmgFrameDuration,p1BasicAttackFrameDuration,p1Spell1FrameDuration,p1Spell2FrameDuration]
    p2FramesDurations = [p2DmgFrameDuration,p2BasicAttackFrameDuration,p2Spell1FrameDuration,p2Spell2FrameDuration]

    p1jumps = p1Attributes[3]
    p2jumps = p2Attributes[3]

    p1direction = 'none'
    p2direction = 'none'

    p1lastdirection = 'none'
    p2lastdirection = 'none'

    p1action = 'none'
    p2action = 'none'

    fontp1Name = pygame.font.SysFont('freesansbold.tff',25)
    fontPercentage = pygame.font.SysFont('freesansbold.tff',32)

    textSurfacep1Name = fontp1Name.render(p1Name,True,blue,black)
    textRectp1Name = textSurfacep1Name.get_rect()

    textSurfacep2Name = fontp1Name.render(p2Name,True,red,black)
    textRectp2Name = textSurfacep2Name.get_rect()

    #players ranged attacks

    #Exists,dmg,startx,starty,speed,right image name, left image name,left or right, hitbox lenght, hithox Height, special reference name, buff duration
    p1RangedAttack1 = [False,0,0,0,0,'noImage.png','noImage.png','none',0,0,'none',0]
    p1RangedAttack2 = [False,0,0,0,0,'noImage.png','noImage.png','none',0,0,'none',0]
    p1RangedAttack3 = [False,0,0,0,0,'noImage.png','noImage.png','none',0,0,'none',0]
    p1RangedAttack4 = [False,0,0,0,0,'noImage.png','noImage.png','none',0,0,'none',0]
    p1RangedAttack5 = [False,0,0,0,0,'noImage.png','noImage.png','none',0,0,'none',0]
    p1RangedAttack6 = [False,0,0,0,0,'noImage.png','noImage.png','none',0,0,'none',0]
    p1RangedAttack7 = [False,0,0,0,0,'noImage.png','noImage.png','none',0,0,'none',0]
    p1RangedAttack8 = [False,0,0,0,0,'noImage.png','noImage.png','none',0,0,'none',0]
    p1RangedAttack9 = [False,0,0,0,0,'noImage.png','noImage.png','none',0,0,'none',0]
    p1RangedAttack10 = [False,0,0,0,0,'noImage.png','noImage.png','none',0,0,'none',0]


    p2RangedAttack1 = [False,0,0,0,0,'noImage.png','noImage.png','none',0,0,'none',0]
    p2RangedAttack2 = [False,0,0,0,0,'noImage.png','noImage.png','none',0,0,'none',0]
    p2RangedAttack3 = [False,0,0,0,0,'noImage.png','noImage.png','none',0,0,'none',0]
    p2RangedAttack4 = [False,0,0,0,0,'noImage.png','noImage.png','none',0,0,'none',0]
    p2RangedAttack5 = [False,0,0,0,0,'noImage.png','noImage.png','none',0,0,'none',0]
    p2RangedAttack6 = [False,0,0,0,0,'noImage.png','noImage.png','none',0,0,'none',0]
    p2RangedAttack7 = [False,0,0,0,0,'noImage.png','noImage.png','none',0,0,'none',0]
    p2RangedAttack8 = [False,0,0,0,0,'noImage.png','noImage.png','none',0,0,'none',0]
    p2RangedAttack9 = [False,0,0,0,0,'noImage.png','noImage.png','none',0,0,'none',0]
    p2RangedAttack10 = [False,0,0,0,0,'noImage.png','noImage.png','none',0,0,'none',0]


    p1RangedAttacks = [p1RangedAttack1,p1RangedAttack2,p1RangedAttack3,p1RangedAttack4,p1RangedAttack5,p1RangedAttack6,p1RangedAttack7,p1RangedAttack8,p1RangedAttack9,p1RangedAttack10]
    p2RangedAttacks = [p2RangedAttack1,p2RangedAttack2,p2RangedAttack3,p2RangedAttack4,p2RangedAttack5,p2RangedAttack6,p2RangedAttack7,p2RangedAttack8,p2RangedAttack9,p2RangedAttack10]


    #players additional frames

    #players buffs

    p1ImmunityDuration = 0

    p2ImmunityDuration = 0

    p1DashingDuration = 0

    p2DashingDuration = 0

    p1RootedDuration = 0

    p2RootedDuration = 0

    p1FreezedDuration = 0

    p2FreezedDuration = 0

    p1Slowed50Duration = 0

    p2Slowed50Duration = 0


    p1BuffsDurations = [p1ImmunityDuration,p1DashingDuration,p1RootedDuration,p1FreezedDuration,p1Slowed50Duration]
    p2BuffsDurations = [p2ImmunityDuration,p2DashingDuration,p2RootedDuration,p2FreezedDuration,p2Slowed50Duration]

    #Exception

    p1Traps = 0
    p2Traps = 0


    while True: # main game loop

        #Key entrances
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                ys.exit()

            keys = pygame.key.get_pressed()

            #Player 1 Keys
            if keys[K_c]:
                player1ClassChange = True
            if keys[getattr(pygame, keyconfig['K_q'])]:
                p1direction = 'left'
                p1lastdirection = 'left'
            if keys[getattr(pygame, keyconfig['K_d'])]:
                p1direction = 'right'
                p1lastdirection = 'right'
            if keys[getattr(pygame, keyconfig['K_z'])]:
                p1action = 'up'
            if keys[getattr(pygame, keyconfig['K_SPACE'])]:
                p1action = 'basic attack'
            if keys[getattr(pygame, keyconfig['K_a'])]:
                p1action = 'spell1'
            if keys[getattr(pygame, keyconfig['K_e'])]:
                p1action = 'spell2'

            if not keys[getattr(pygame, keyconfig['K_SPACE'])] and not keys[getattr(pygame, keyconfig['K_a'])] and not keys[getattr(pygame, keyconfig['K_z'])] and not keys[getattr(pygame, keyconfig['K_e'])]:
                p1action = 'none'
            if not keys[getattr(pygame, keyconfig['K_q'])] and not keys[getattr(pygame, keyconfig['K_d'])]:
                p1direction = 'none'
            if keys[getattr(pygame, keyconfig['K_q'])] and keys[getattr(pygame, keyconfig['K_d'])]:
                p1direction = 'none'

            if p1BuffsDurations[2] > 0:
                p1direction = 'none'
                p1lastdirection = 'none'

            if p1BuffsDurations[1] > 0:
                p1lastdirection = 'none'

            if p1BuffsDurations[3] > 0:
                p1direction = 'none'
                p1action = 'none'
                p1lastdirection = 'none'

            #Player 2 Keys
            if keys[K_KP8]:
                player2ClassChange = True
            if keys[getattr(pygame, keyconfig['K_LEFT'])]:
                p2direction = 'left'
                p2lastdirection = 'left'
            if keys[getattr(pygame, keyconfig['K_RIGHT'])]:
                p2direction = 'right'
                p2lastdirection = 'right'
            if keys[getattr(pygame, keyconfig['K_UP'])]:
                p2action = 'up'
            if keys[getattr(pygame, keyconfig['K_KP0'])]:
                p2action = 'basic attack'
            if keys[getattr(pygame, keyconfig['K_KP1'])]:
                p2action = 'spell1'
            if keys[getattr(pygame, keyconfig['K_KP2'])]:
                p2action = 'spell2'

            if not keys[getattr(pygame, keyconfig['K_KP0'])] and not keys[getattr(pygame, keyconfig['K_KP1'])] and not keys[getattr(pygame, keyconfig['K_UP'])] and not keys[getattr(pygame,keyconfig['K_KP2'])]:
                p2action = 'none'
            if not keys[getattr(pygame, keyconfig['K_LEFT'])] and not keys[getattr(pygame, keyconfig['K_RIGHT'])]:
                p2direction = 'none'
            if keys[getattr(pygame, keyconfig['K_RIGHT'])] and keys[getattr(pygame, keyconfig['K_LEFT'])]:
                p2direction = 'none'

            if p2BuffsDurations[2] > 0:
                p2direction = 'none'
                p2lastdirection = 'none'

            if p2BuffsDurations[1] > 0:
                p2lastdirection = 'none'

            if p2BuffsDurations[3] > 0:
                p2direction = 'none'
                p2action = 'none'
                p2lastdirection = 'none'


        #Death Certificate
        if p1Attributes[4] <= 0 and p2Attributes[4] > 0:
            print('\n'+p2Name+' wins!')
            return p2Name, player1ClassChange, player2ClassChange

        if p2Attributes[4] <= 0 and p1Attributes[4] > 0:
            print('\n'+p1Name+' wins!')
            return p1Name, player1ClassChange, player2ClassChange

        if p1Attributes[4] <= 0 and p2Attributes[4] <= 0:
            print('No one wins :( ')
            return 'none', player1ClassChange, player2ClassChange

        #Cooldwon resetting

        for i in range(0,len(p1Cooldowns)):
            if p1Cooldowns[i] > 0:
                p1Cooldowns[i] -= 1

        for i in range(0,len(p2Cooldowns)):
            if p2Cooldowns[i] > 0:
                p2Cooldowns[i] -= 1

        #Frame durations

        for i in range(0,len(p1FramesDurations)):
            if p1FramesDurations[i] > 0:
                p1FramesDurations[i] -= 1

        for i in range(0,len(p2FramesDurations)):
            if p2FramesDurations[i] > 0:
                p2FramesDurations[i] -= 1

        #Buff Durations

        for i in range(0,len(p1BuffsDurations)):
            if p1BuffsDurations[i] > 0:
                p1BuffsDurations[i] -= 1

        for i in range(0,len(p2BuffsDurations)):
            if p2BuffsDurations[i] > 0:
                p2BuffsDurations[i] -= 1



        #Actions player 1
        #Jump

        if p1action == 'up' and p1jumps >= 1:
            p1jumps -= 1
            p1YS = -10

        #Spell 1
        if p1action == 'spell1':
            if p1Cooldowns[1] == 0:
                if p1class == 'Warrior':
                    p1Cooldowns[1] = p1Spell1Attributes[2]
                    p1BuffsDurations[0] += p1Spell1Attributes[6]
                    p1FramesDurations[2] += p1Spell1Attributes[6]

                if p1class == 'Mage':
                    if framecount > 301:
                        p1Cooldowns[1] = p1Spell1Attributes[2]
                        p1X = p1Positions[framecount-300][0]
                        p1Y = p1Positions[framecount-300][1]
                        p1XS = 0
                        p1YS = 0

                if p1class == 'Archer':
                    if p1lastdirection == 'right' or p1lastdirection == 'left':
                        for p1RangedAttack in p1RangedAttacks:
                            if p1RangedAttack[0] == False:
                                p1Cooldowns[1] = p1Spell1Attributes[2]
                                p1RangedAttack[0] = True
                                p1RangedAttack[1] = p1Spell1Attributes[1]
                                p1RangedAttack[2] = p1X
                                p1RangedAttack[3] = p1Y + 16
                                p1RangedAttack[4] = p1Spell1Attributes[11]
                                p1RangedAttack[5] = p1Spell1Img[0]
                                p1RangedAttack[6] = p1Spell1Img[1]
                                p1RangedAttack[7] = p1lastdirection
                                p1RangedAttack[8] = p1Spell1Attributes[3]
                                p1RangedAttack[9] = p1Spell1Attributes[4]
                                p1RangedAttack[10] = p1Spell1Attributes[7]
                                p1RangedAttack[11] = p1Spell1Attributes[6]
                                break



        #Spell 2
        if p1action == 'spell2':
            if p1Cooldowns[2] == 0:
                if p1class == 'Warrior' and p1BuffsDurations[2] == 0:
                    p1Cooldowns[2] = p1Spell2Attributes[2]
                    p1BuffsDurations[1] += p1Spell2Attributes[6]
                    p1FramesDurations[3] += p1Spell2Attributes[6]

                if p1class == 'Mage':
                    if p1lastdirection == 'right' or p1lastdirection == 'left':
                        for p1RangedAttack in p1RangedAttacks:
                            if p1RangedAttack[0] == False:
                                p1Cooldowns[2] = p1Spell2Attributes[2]
                                p1RangedAttack[0] = True
                                p1RangedAttack[1] = p1Spell2Attributes[1]
                                p1RangedAttack[2] = p1X
                                p1RangedAttack[3] = p1Y + 16
                                p1RangedAttack[4] = p1Spell2Attributes[11]
                                p1RangedAttack[5] = p1Spell2Img[0]
                                p1RangedAttack[6] = p1Spell2Img[1]
                                p1RangedAttack[7] = p1lastdirection
                                p1RangedAttack[8] = p1Spell2Attributes[3]
                                p1RangedAttack[9] = p1Spell2Attributes[4]
                                p1RangedAttack[10] = p1Spell2Attributes[7]
                                p1RangedAttack[11] = p1Spell2Attributes[6]
                                break

                if p1class == 'Archer':
                    if p1lastdirection == 'right' or p1lastdirection == 'left':
                        if p1Traps < 2:
                            for p1RangedAttack in p1RangedAttacks:
                                if p1RangedAttack[0] == False:
                                    p1Cooldowns[2] = p1Spell2Attributes[2]
                                    p1RangedAttack[0] = True
                                    p1RangedAttack[1] = p1Spell2Attributes[1]
                                    p1RangedAttack[2] = p1X
                                    p1RangedAttack[3] = p1Y + 32
                                    p1RangedAttack[4] = p1Spell2Attributes[11]
                                    p1RangedAttack[5] = p1Spell2Img[0]
                                    p1RangedAttack[6] = p1Spell2Img[1]
                                    p1RangedAttack[7] = p1lastdirection
                                    p1RangedAttack[8] = p1Spell2Attributes[3]
                                    p1RangedAttack[9] = p1Spell2Attributes[4]
                                    p1RangedAttack[10] = p1Spell2Attributes[7]
                                    p1RangedAttack[11] = p1Spell2Attributes[6]
                                    p2Traps += 1
                                    break

        #Basic Attack


        #Melee
        if p1action == 'basic attack':
            if p1AttackAttributes[0] == 'yes':
                if p1AttackAttributes[5] == 'no':
                    if p1Cooldowns[0] == 0:
                        if p1lastdirection == 'right':
                            if (p2X + 32 >= p1X + 32 and p2X + 32 <= p1X + 64 + p1AttackAttributes[3]) and (p2Y + 32 >= p1Y + 32 - (p1AttackAttributes[4]/2) and p2Y + 32 <= p1Y + 32 + (p1AttackAttributes[4]/2)):
                                if p2BuffsDurations[0] == 0:
                                    p2Attributes[4] -= p1AttackAttributes[1]
                                    p2FramesDurations[0] = 30

                            p1AttackFrame = p1BasicAttackRight
                            p1FramesDurations[1] = p1AttackAttributes[7]
                            p1Cooldowns[0] = p1AttackAttributes[2]

                        if p1lastdirection == 'left':
                            if (p2X + 32 >= p1X - p1AttackAttributes[3] and p2X +32 <= p1X + 32) and (p2Y + 32 >= p1Y + 32 - (p1AttackAttributes[4]/2) and p2Y +32 <= p1Y + 32 + (p1AttackAttributes[4]/2)):
                                if p2BuffsDurations[0] == 0:
                                    p2Attributes[4] -= p1AttackAttributes[1]
                                    p2FramesDurations[0] = 30

                            p1AttackFrame = p1BasicAttackLeft
                            p1FramesDurations[1] = p1AttackAttributes[7]
                            p1Cooldowns[0] = p1AttackAttributes[2]
                #Ranged
                if p1AttackAttributes[5] == 'yes':
                    if p1Cooldowns[0] == 0:
                        if p1lastdirection == 'right' or p1lastdirection == 'left':
                            for p1RangedAttack in p1RangedAttacks:
                                if p1RangedAttack[0] == False:
                                    p1Cooldowns[0] = p1AttackAttributes [2]
                                    p1RangedAttack[0] = True
                                    p1RangedAttack[1] =  p1AttackAttributes[1]
                                    p1RangedAttack[2] = p1X
                                    p1RangedAttack[3] = p1Y + 16
                                    p1RangedAttack[4] = p1AttackAttributes[6]
                                    p1RangedAttack[5] = p1AttackAttributes[8]
                                    p1RangedAttack[6] = p1AttackAttributes[9]
                                    p1RangedAttack[7] = p1lastdirection
                                    p1RangedAttack[8] = p1AttackAttributes[3]
                                    p1RangedAttack[9] = p1AttackAttributes[4]
                                    p1RangedAttack[10] = 'none'
                                    break




        #Action player 2

        #Jump
        if p2action == 'up' and p2jumps >= 1:
            p2jumps -= 1
            p2YS = -10


        #Spell 1

        if p2action == 'spell1':
            if p2Cooldowns[1] == 0:
                if p2class == 'Warrior':
                    p2Cooldowns[1] = p2Spell1Attributes[2]
                    p2BuffsDurations[0] += p2Spell1Attributes[6]
                    p2FramesDurations[2] += p2Spell1Attributes[6]

                if p2class == 'Mage':
                    if framecount > 301:
                        p2Cooldowns[1] = p2Spell1Attributes[2]
                        p2X = p2Positions[framecount-300][0]
                        p2Y = p2Positions[framecount-300][1]
                        p2XS = 0
                        p2YS = 0

                if p2class == 'Archer':
                    if p2lastdirection == 'right' or  p2lastdirection == 'left':
                        for p2RangedAttack in p2RangedAttacks:
                            if p2RangedAttack[0] == False:
                                p2Cooldowns[1] = p2Spell1Attributes[2]
                                p2RangedAttack[0] = True
                                p2RangedAttack[1] = p2Spell1Attributes[1]
                                p2RangedAttack[2] = p2X
                                p2RangedAttack[3] = p2Y + 16
                                p2RangedAttack[4] = p2Spell1Attributes[11]
                                p2RangedAttack[5] = p2Spell1Img[0]
                                p2RangedAttack[6] = p2Spell1Img[1]
                                p2RangedAttack[7] = p2lastdirection
                                p2RangedAttack[8] = p2Spell1Attributes[3]
                                p2RangedAttack[9] = p2Spell1Attributes[4]
                                p2RangedAttack[10] = p2Spell1Attributes[7]
                                p2RangedAttack[11] = p2Spell1Attributes[6]
                                break

        #Spell 2
        if p2action == 'spell2':
            if p2Cooldowns[2] == 0:
                if p2class == 'Warrior' and p2BuffsDurations[2] == 0:
                    p2Cooldowns[2] = p2Spell2Attributes[2]
                    p2BuffsDurations[1] += p2Spell2Attributes[6]
                    p2FramesDurations[3] += p2Spell2Attributes[6]

                if p2class == 'Mage':
                    if p2lastdirection == 'right' or p2lastdirection == 'left':
                        for p2RangedAttack in p2RangedAttacks:
                            if p2RangedAttack[0] == False:
                                p2Cooldowns[2] = p2Spell2Attributes[2]
                                p2RangedAttack[0] = True
                                p2RangedAttack[1] = p2Spell2Attributes[1]
                                p2RangedAttack[2] = p2X
                                p2RangedAttack[3] = p2Y + 16
                                p2RangedAttack[4] = p2Spell2Attributes[11]
                                p2RangedAttack[5] = p2Spell2Img[0]
                                p2RangedAttack[6] = p2Spell2Img[1]
                                p2RangedAttack[7] = p2lastdirection
                                p2RangedAttack[8] = p2Spell2Attributes[3]
                                p2RangedAttack[9] = p2Spell2Attributes[4]
                                p2RangedAttack[10] = p2Spell2Attributes[7]
                                p2RangedAttack[11] = p2Spell2Attributes[6]
                                break

                if p2class == 'Archer':
                    if p2lastdirection == 'right' or p2lastdirection == 'left':
                        if p2Traps < 2:
                            for p2RangedAttack in p2RangedAttacks:
                                if p2RangedAttack[0] == False:
                                    p2Cooldowns[2] = p2Spell2Attributes[2]
                                    p2RangedAttack[0] = True
                                    p2RangedAttack[1] = p2Spell2Attributes[1]
                                    p2RangedAttack[2] = p2X
                                    p2RangedAttack[3] = p2Y + 32
                                    p2RangedAttack[4] = p2Spell2Attributes[11]
                                    p2RangedAttack[5] = p2Spell2Img[0]
                                    p2RangedAttack[6] = p2Spell2Img[1]
                                    p2RangedAttack[7] = p2lastdirection
                                    p2RangedAttack[8] = p2Spell2Attributes[3]
                                    p2RangedAttack[9] = p2Spell2Attributes[4]
                                    p2RangedAttack[10] = p2Spell2Attributes[7]
                                    p2RangedAttack[11] = p2Spell2Attributes[6]
                                    p2Traps += 1
                                    break

        #Basic Attack

        #Melee
        if p2action == 'basic attack':
            if p2AttackAttributes[0] == 'yes':
                if p2AttackAttributes[5] == 'no':
                    if p2Cooldowns[0] == 0:
                        if p2lastdirection == 'right':
                            if (p1X + 32 >= p2X + 32 and p1X + 32 <= p2X + 64 + p2AttackAttributes[3]) and (p1Y + 32 >= p2Y + 32 - (p2AttackAttributes[4]/2) and p1Y + 32 <= p2Y + 32 + (p2AttackAttributes[4]/2)):
                                if p1BuffsDurations[0] == 0:
                                    p1Attributes[4] -= p2AttackAttributes[1]
                                    p1FramesDurations[0] = 30

                            p2AttackFrame = p2BasicAttackRight
                            p2FramesDurations[1] = p2AttackAttributes[7]
                            p2Cooldowns[0] = p2AttackAttributes[2]

                        if p2lastdirection == 'left':
                            if (p1X + 32 >= p2X - p2AttackAttributes[3] and p1X + 32 <= p2X + 32) and (p1Y + 32 >= p2Y + 32 - (p2AttackAttributes[4]/2) and p1Y + 32 <= p2Y + 32 + (p2AttackAttributes[4]/2)):
                                if p1BuffsDurations[0] == 0:
                                    p1Attributes[4] -= p2AttackAttributes[1]
                                    p1FramesDurations[0] = 30

                            p2AttackFrame = p2BasicAttackLeft
                            p2FramesDurations[1] = p2AttackAttributes[7]
                            p2Cooldowns[0] = p2AttackAttributes[2]


                #Ranged
                if p2AttackAttributes[5] == 'yes':
                    if p2Cooldowns[0] == 0:
                        if p2lastdirection == 'right' or p2lastdirection == 'left':
                            for p2RangedAttack in p2RangedAttacks:
                                if p2RangedAttack[0] == False:
                                    p2Cooldowns[0] = p2AttackAttributes [2]
                                    p2RangedAttack[0] = True
                                    p2RangedAttack[1] =  p2AttackAttributes[1]
                                    p2RangedAttack[2] = p2X
                                    p2RangedAttack[3] = p2Y + 16
                                    p2RangedAttack[4] = p2AttackAttributes[6]
                                    p2RangedAttack[5] = p2AttackAttributes[8]
                                    p2RangedAttack[6] = p2AttackAttributes[9]
                                    p2RangedAttack[7] = p2lastdirection
                                    p2RangedAttack[8] = p2AttackAttributes[3]
                                    p2RangedAttack[9] = p2AttackAttributes[4]
                                    p2RangedAttack[10] = 'none'
                                    break






        #Movements player 1

        if p1direction == 'right' and p1XS < p1Attributes[1]:
            p1XS += p1Attributes[0]

        elif p1direction == 'left' and p1XS > -p1Attributes[1]:
            p1XS -= p1Attributes[0]

        elif p1direction == 'none':
            if p1XS > 0:
                p1XS -= p1Attributes[0]
                if p1XS - p1Attributes[0] <= 0:
                    p1XS = 0
            if p1XS < 0:
                p1XS += p1Attributes[0]
                if p1XS + p1Attributes[0] >= 0:
                    p1XS = 0


        #Movements player 2

        if p2direction == 'right' and p2XS < p2Attributes[1]:
            p2XS += p2Attributes[0]

        elif p2direction == 'left' and p2XS > -p2Attributes[1]:
            p2XS -= p2Attributes[0]

        elif p2direction == 'none':
            if p2XS > 0:
                p2XS -= p2Attributes[0]
                if p2XS - p2Attributes[0] <= 0:
                    p2XS = 0
            if p2XS < 0:
                p2XS += p2Attributes[0]
                if p2XS + p2Attributes[0] >= 0:
                    p2XS = 0

        #Dashing player 1
        if p1BuffsDurations[1] > 1:
            if p1class == 'Warrior':
                if p1lastdirection == 'right':
                    p1XS = 15
                if p1lastdirection == 'left':
                    p1XS = -15
                if players_inter_collision(p1X,p1Y,p2X,p2Y):
                    p1XS = 0
                    p1BuffsDurations[1] = 0
                    if p2BuffsDurations[0] == 0:
                        p2XS = 0
                        p2YS = 0
                        p2Attributes[4] -= p1Spell2Attributes[1] #Dmg
                        p2BuffsDurations[2] = 60 #root
                        p2FramesDurations[0] = 30


                p1YS = 0

        if p1BuffsDurations[1] == 1:
            p1XS = 0

        #Dashing player 2
        if p2BuffsDurations[1] > 1:
            if p2class == 'Warrior':
                if p2lastdirection == 'right':
                    p2XS = 15

                if p2lastdirection == 'left':
                    p2XS = -15
                if players_inter_collision(p1X,p1Y,p2X,p2Y):
                    p2BuffsDurations[1] = 0
                    p2XS = 0
                    if p1BuffsDurations[0] == 0:
                        p1XS = 0
                        p1YS = 0
                        p1Attributes[4] -= p2Spell2Attributes[1]
                        p1BuffsDurations[2] = 60
                        p1FramesDurations[0] = 30
                p2YS = 0
        if p2BuffsDurations[1] == 1:
            p2XS = 0


        #Ranged Attacks

        #Player1
        for p1RangedAttack in p1RangedAttacks:

            if p1RangedAttack[0] == True:
                if p1RangedAttack[7] == 'right':
                    p1RangedAttack[2] += p1RangedAttack[4]
                if p1RangedAttack[7] == 'left':
                    p1RangedAttack[2] -= p1RangedAttack[4]

                if ranged_attack_hit(p2X,p2Y,p1RangedAttack) and p2BuffsDurations[0] == 0:

                    if p1RangedAttack[10] == 'none':
                        if p2BuffsDurations[3] == 0:
                            p2Attributes[4] -= p1RangedAttack[1]
                        else:
                            p2Attributes[4] -= 2 * p1RangedAttack[1]

                        p1RangedAttack[0] = False
                        p2FramesDurations[0] = 30

                    if p1RangedAttack[10] == 'Freezer':

                        if p2BuffsDurations[3] == 0:
                            p2Attributes[4] -= p1RangedAttack[1]
                        else:
                            p2Attributes[4] -= 2 * p1RangedAttack[1]

                        p1RangedAttack[0] = False
                        p2FramesDurations[0] = 30
                        p2BuffsDurations[3] = p1RangedAttack[11]

                    if p1RangedAttack[10] == 'Slow Arrow':

                        p2Attributes[4] -= p1RangedAttack[1]
                        p1RangedAttack[0] = False
                        p2FramesDurations[0] = 30
                        p2BuffsDurations[4] = p1RangedAttack[11]

                    if p1RangedAttack[10] == 'Root':

                        p2Attributes[4] -= p1RangedAttack[1]
                        p1RangedAttack[0] = False
                        p2BuffsDurations[2] = p1RangedAttack[11]
                        p1Traps -= 1

                if ranged_attack_collision(p1RangedAttack[2],p1RangedAttack[3],p1RangedAttack[8],p1RangedAttack[9],collisionalRectangles):
                    p1RangedAttack[0] = False
                if p1RangedAttack[2] > 1250 or p1RangedAttack[2] < -50:
                    p1RangedAttack[0] = False



        #Player2


        for p2RangedAttack in p2RangedAttacks:
            if p2RangedAttack[0] == True:
                if p2RangedAttack[7] == 'right':
                    p2RangedAttack[2] += p2RangedAttack[4]
                if p2RangedAttack[7] == 'left':
                    p2RangedAttack[2] -= p2RangedAttack[4]

                if ranged_attack_hit(p1X,p1Y,p2RangedAttack) and p1BuffsDurations[0] == 0:

                    if p2RangedAttack[10] == 'none':
                        if p1BuffsDurations[3] == 0:
                            p1Attributes[4] -= p2RangedAttack[1]
                        else:
                            p1Attributes[4] -= 2 * p2RangedAttack[1]

                        p2RangedAttack[0] = False
                        p1FramesDurations[0] = 30

                    if p2RangedAttack[10] == 'Freezer':

                        if p1BuffsDurations[3] == 0:

                            p1Attributes[4] -= p2RangedAttack[1]
                        else:
                            p1Attributes[4] -= 2 * p2RangedAttack[1]

                        p2RangedAttack[0] = False
                        p1FramesDurations[0] = 30
                        p1BuffsDurations[3] = p2RangedAttack[11]

                    if p2RangedAttack[10] == 'Slow Arrow':

                        p1Attributes[4] -= p2RangedAttack[1]
                        p2RangedAttack[0] = False
                        p1FramesDurations[0] = 30
                        p1BuffsDurations[4] = p2RangedAttack[11]

                    if p2RangedAttack[10] == 'Root':

                        p1Attributes[4] -= p2RangedAttack[1]
                        p2RangedAttack[0] = False
                        p1BuffsDurations[2] = p2RangedAttack[11]
                        p2Traps -= 1


                if ranged_attack_collision(p2RangedAttack[2],p2RangedAttack[3],p2RangedAttack[8],p2RangedAttack[9],collisionalRectangles):
                    p2RangedAttack[0] = False
                if p2RangedAttack[2] > 1250 or p2RangedAttack[2] < -50:
                    p2RangedAttack[0] = False



        #Constant speed changes, as gravity
        p1YS += grav
        p2YS += grav

        #Position Adjustements

        if p1BuffsDurations[2] > 0:
            p1XS = 0
        if p1BuffsDurations[3] > 0:
            p1XS = 0

        if p2BuffsDurations[2] > 0:
            p2XS = 0
        if p2BuffsDurations[3] > 0:
            p2XS = 0

        #Slow buff
        if p1BuffsDurations[4] > 0:
            p1fXS = p1XS/float(2)

        if p1BuffsDurations[4] == 0:
            p1fXS = p1XS

        if p2BuffsDurations[4] > 0:
            p2fXS = p2XS/float(2)

        if p2BuffsDurations[4] == 0:
            p2fXS = p2XS

        p1fYS = p1YS
        p2fYS = p2YS

        p1X += p1fXS
        p1Y += p1fYS
        p1Positions.append([p1X,p1Y])

        p2X += p2fXS
        p2Y += p2fYS
        p2Positions.append([p2X,p2Y])


        #Player 1 collision
        for obstacle in collisionalRectangles:
            if ((obstacle[0][0] - (p1X + 64)) <= 0	and	(obstacle[0][0] + obstacle[1][0] - p1X >= 0)) and ((obstacle[0][1] - (p1Y + 64) <= 0) and (obstacle[0][1] + obstacle[1][1] - p1Y >= 0)):

                if p1Y + 64 + p1YS >= obstacle[0][1] and p1Y <= obstacle[0][1] and p1YS > 0:
                    p1Y = obstacle[0][1] - 65
                    p1YS = 0
                    p1jumps = p1Attributes[3]

                elif p1Y + p1YS <= obstacle[0][1] + obstacle[1][1] and p1Y >= obstacle[0][1] and p1YS < 0:
                    p1Y = obstacle[0][1] + obstacle[1][1]
                    p1YS = 0

                else:
                    if p1X+64 <= obstacle[0][0]+obstacle[1][0]:
                        p1X = obstacle[0][0] - 64
                        p1XS = 0
                    if p1X >= obstacle[0][0]:
                        p1X = obstacle[0][0] + obstacle[1][0]
                        p1XS = 0
        #Player 2 collision
        for obstacle in collisionalRectangles:
            if ((obstacle[0][0] - (p2X + 64)) <= 0	and	(obstacle[0][0] + obstacle[1][0] - p2X >= 0)) and ((obstacle[0][1] - (p2Y + 64) <= 0) and (obstacle[0][1] + obstacle[1][1] - p2Y >= 0)):

                if p2Y + 64 + p2YS >= obstacle[0][1] and p2Y <= obstacle[0][1] and p2YS > 0:
                    p2Y = obstacle[0][1] - 65
                    p2YS = 0
                    p2jumps = p1Attributes[3]

                elif p2Y + p2YS <= obstacle[0][1] + obstacle[1][1] and p2Y >= obstacle[0][1] and p2YS < 0:
                    p2Y = obstacle[0][1] + obstacle[1][1]
                    p2YS = 0

                else:
                    if p2X+64 <= obstacle[0][0]+obstacle[1][0]:
                        p2X = obstacle[0][0] - 64
                        p2XS = 0
                    if p2X >= obstacle[0][0]:
                        p2X = obstacle[0][0] + obstacle[1][0]
                        p2XS = 0



        #Map border limiting

        if p1X >= 1136:
            p1X = 1136
            p1XS = 0

        if p1X <= 0:
            p1X = 0
            p1XS = 0

        if p1Y >= 726:
            p1Y = 726
            p1YS = 0
            p1jumps = p1Attributes[3]

        if p2X >= 1136:
            p2X = 1136
            p2XS = 0

        if p2X <= 0:
            p2X = 0
            p2XS = 0

        if p2Y >= 726:
            p2Y = 726
            p2YS = 0
            p2jumps = p2Attributes[3]

        #Player Frames Selection
        if p1direction == 'none':
            p1Img = p1ImgFront
        if p1direction == 'left':
            p1Img = p1ImgLeft
        if p1direction == 'right':
            p1Img = p1ImgRight
        if p1FramesDurations[0] > 0:
            p1Img = p1ImgDmg
        if p1FramesDurations[1] > 0:
            p1Img = p1AttackFrame

        if p2direction == 'none':
            p2Img = p2ImgFront
        if p2direction == 'left':
            p2Img = p2ImgLeft
        if p2direction == 'right':
            p2Img = p2ImgRight
        if p2FramesDurations[0] > 0:
            p2Img = p2ImgDmg
        if p2FramesDurations[1] > 0:
            p2Img = p2AttackFrame

        #HP Percentages text:
        p1HpPercentageText = Hp_percentage(p1Attributes[4],p1class)
        p2HpPercentageText = Hp_percentage(p2Attributes[4],p2class)

        textSurfacep1Percentage = fontPercentage.render(p1HpPercentageText,True,blue,black)
        textRectp1Percentage = textSurfacep1Percentage.get_rect()

        textSurfacep2Percentage = fontPercentage.render(p2HpPercentageText,True,red,black)
        textRectp2Percentage = textSurfacep2Percentage.get_rect()


        #Draw graphics

        #Names
        textRectp1Percentage.center = (200,50)
        textRectp2Percentage.center = (1000,50)
        textRectp1Name.center = (p1X + 32, p1Y - 25)
        textRectp2Name.center = (p2X + 32, p2Y - 25)
        DISPLAYSURF.fill(black)

        #Players
        DISPLAYSURF.blit(p1Img,(p1X,p1Y))
        DISPLAYSURF.blit(p2Img,(p2X,p2Y))
        DISPLAYSURF.blit(groundImg,(0,790))
        for obstacle in collisionalRectangles:
            pygame.draw.rect(DISPLAYSURF,brown,(obstacle[0][0],obstacle[0][1],obstacle[1][0],obstacle[1][1]))

        #Buffs Graphics

        if p1BuffsDurations[0] > 0:
            DISPLAYSURF.blit(pygame.image.load(buffsFrames[0]),(p1X-32,p1Y-32))

        if p1BuffsDurations[2] > 0:
            DISPLAYSURF.blit(pygame.image.load(buffsFrames[2]),(p1X-32,p1Y-32))

        if p1BuffsDurations[3] > 0:
            DISPLAYSURF.blit(pygame.image.load(buffsFrames[3]),(p1X-32,p1Y-32))

        if p2BuffsDurations[0] > 0:
            DISPLAYSURF.blit(pygame.image.load(buffsFrames[0]),(p2X-32,p2Y-32))

        if p2BuffsDurations[2] > 0:
            DISPLAYSURF.blit(pygame.image.load(buffsFrames[2]),(p2X-32,p2Y-32))

        if p2BuffsDurations[3] > 0:
            DISPLAYSURF.blit(pygame.image.load(buffsFrames[3]),(p2X-32,p2Y-32))


        #Ranged attacks
        for p1RangedAttack in p1RangedAttacks:
            if p1RangedAttack[0]:
                if p1RangedAttack[7]=='right':
                    DISPLAYSURF.blit(pygame.image.load(p1RangedAttack[5]),(p1RangedAttack[2],p1RangedAttack[3]))
                if p1RangedAttack[7]=='left':
                    DISPLAYSURF.blit(pygame.image.load(p1RangedAttack[6]),(p1RangedAttack[2],p1RangedAttack[3]))

        for p2RangedAttack in p2RangedAttacks:
            if p2RangedAttack[0]:
                if p2RangedAttack[7]=='right':
                    DISPLAYSURF.blit(pygame.image.load(p2RangedAttack[5]),(p2RangedAttack[2],p2RangedAttack[3]))
                if p2RangedAttack1[7]=='left':
                    DISPLAYSURF.blit(pygame.image.load(p2RangedAttack[6]),(p2RangedAttack[2],p2RangedAttack[3]))


        DISPLAYSURF.blit(textSurfacep2Name,textRectp2Name)
        DISPLAYSURF.blit(textSurfacep1Name,textRectp1Name)
        DISPLAYSURF.blit(textSurfacep1Percentage,textRectp1Percentage)
        DISPLAYSURF.blit(textSurfacep2Percentage,textRectp2Percentage)
        DISPLAYSURF.blit(psWinsSurfaceObj,psWinsRectObj)

        #Cooldown Graphics
        DISPLAYSURF.blit(p1BasicAttackIcon,(100,75))
        if p1Cooldowns[0] > 0:
            DISPLAYSURF.blit(pygame.image.load('32x32/'+wich_cooldown_frame(p1Cooldowns[0],p1AttackAttributes[2])+'.png'),(100,75))

        DISPLAYSURF.blit(p1Spell1Icon,(164,75))
        if p1Cooldowns[1] > 0:
            DISPLAYSURF.blit(pygame.image.load('32x32/'+wich_cooldown_frame(p1Cooldowns[1],p1Spell1Attributes[2])+'.png'),(164,75))

        DISPLAYSURF.blit(p1Spell2Icon,(228,75))
        if p1Cooldowns[2] > 0:
            DISPLAYSURF.blit(pygame.image.load('32x32/'+wich_cooldown_frame(p1Cooldowns[2],p1Spell2Attributes[2])+'.png'),(228,75))

        DISPLAYSURF.blit(p2BasicAttackIcon,(900,75))
        if p2Cooldowns[0] > 0:
            DISPLAYSURF.blit(pygame.image.load('32x32/'+wich_cooldown_frame(p2Cooldowns[0],p2AttackAttributes[2])+'.png'),(900,75))

        DISPLAYSURF.blit(p2Spell1Icon,(964,75))
        if p2Cooldowns[1] > 0:
            DISPLAYSURF.blit(pygame.image.load('32x32/'+wich_cooldown_frame(p2Cooldowns[1],p2Spell1Attributes[2])+'.png'),(964,75))

        DISPLAYSURF.blit(p2Spell2Icon,(1028,75))
        if p2Cooldowns[2] > 0:
            DISPLAYSURF.blit(pygame.image.load('32x32/'+wich_cooldown_frame(p2Cooldowns[2],p2Spell2Attributes[2])+'.png'),(1028,75))


        pygame.display.update()

        framecount += 1

        #Loop per seconds
        fpsClock.tick(FPS)


