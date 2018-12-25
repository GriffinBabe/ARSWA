from main import main

import pygame, math



DISPLAYSURF = pygame.display.set_mode((1200, 800),0,32)
pygame.display.set_caption('Project ARSWA')

def start_menu():
    #Loadings
    menuImage = pygame.image.load('menu.png')
    DISPLAYSURF.blit(menuImage,(0,0))
    pygame.display.update()

    #Existances
    existing_class = ['Warrior','Mage','Archer']
    existing_layouts = ['AZERTY','QWERTY']
    existing_os = ['Windows','Unix']
    existing_gamemodes = ['q']
    existing_best_of = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39]

    max_player_number = 16

    #Memes
    """
    antoine_names = ['antoine','Antoine','Griffon','griffon','poulpy','Poulpy','patapoulpe','Patapoulpe','pata','Pata']
    simon_names = ['simon','Simon','sim0n','Sim0n']
    alexandre_names = ['deadamer','Deadamer','alexandre','Alexandre','deadamer07','Deadamer07','frouze','Frouze']
    igor_names = ['igor','Igor','igigor','Igigor','grosPD']
    antoni_names = ['polak','Polak','Antoni','antoni','Antik','antik','Antik554','antik554','antek','Antek','Anal Rupture','anal rupture','olow','Olow','cetteListeEstLonguePutainJeVaisPasTeLouper']
    darius_names = ['Darius','darius','DarkQ','darkQ','GriffinBabe','BeautifulGriffin']
    """

    p1 = True
    p2 = True
    winner = ''

    keyboardconfig = open('keyboardconfig.txt','r')
    configlines = keyboardconfig.readlines()

    #First use keyboard configuration
    if configlines[0] == 'none\n':

        print('---------------------------')
        print('-----CONFIGURING ARSWA-----')
        print('---------------------------')

        print('Wich OS are you using ? Windows or Unix (MAC OS, Linux): ')

        while True:
            os = input()
            if os in existing_os:
                break
            else:
                print('Unknown OS, just type "Windows" or "Unix"')

        print('Keyboard isn\'t configured yet, are you using QWERTY or AZERTY ? ')
        while True:
            keyboardLayout = input()
            if keyboardLayout in existing_layouts:
                break
            else:
                print('Unknown keyboard layout, please type correctly QWERTY or AZERTY : ')

        if keyboardLayout == 'AZERTY' and os == 'Unix':
            configlines[0] = 'AZERTY\n'
            configlines[20] = 'K_q\n'
            configlines[21] = 'K_d\n'
            configlines[22] = 'K_z\n'
            configlines[23] = 'K_SPACE\n'
            configlines[24] = 'K_a\n'
            configlines[25] = 'K_e\n'
            configlines[26] = 'K_r\n'
            configlines[29] = 'K_LEFT\n'
            configlines[30] = 'K_RIGHT\n'
            configlines[31] = 'K_UP\n'
            configlines[32] = 'K_KP0\n'
            configlines[33] = 'K_KP1\n'
            configlines[34] = 'K_KP2\n'
            configlines[35] = 'K_KP3\n'

        elif keyboardLayout == 'QWERTY' and os == 'Unix':
            configlines[0] = 'QWERTY\n'
            configlines[20] = 'K_a\n'
            configlines[21] = 'K_d\n'
            configlines[22] = 'K_w\n'
            configlines[23] = 'K_SPACE\n'
            configlines[24] = 'K_q\n'
            configlines[25] = 'K_e\n'
            configlines[26] = 'K_r\n'
            configlines[29] = 'K_LEFT\n'
            configlines[30] = 'K_RIGHT\n'
            configlines[31] = 'K_UP\n'
            configlines[32] = 'K_KP0\n'
            configlines[33] = 'K_KP1\n'
            configlines[34] = 'K_KP2\n'
            configlines[35] = 'K_KP3\n'

        elif keyboardLayout == 'AZERTY' and os == 'Windows':
            configlines[0] = 'AZERTY\n'
            configlines[20] = 'K_a\n'
            configlines[21] = 'K_d\n'
            configlines[22] = 'K_w\n'
            configlines[23] = 'K_SPACE\n'
            configlines[24] = 'K_q\n'
            configlines[25] = 'K_e\n'
            configlines[26] = 'K_r\n'
            configlines[29] = 'K_LEFT\n'
            configlines[30] = 'K_RIGHT\n'
            configlines[31] = 'K_UP\n'
            configlines[32] = 'K_KP0\n'
            configlines[33] = 'K_KP1\n'
            configlines[34] = 'K_KP2\n'
            configlines[35] = 'K_KP3\n'

        else:
            configlines[0] = 'QWERTY\n'
            configlines[20] = 'K_q\n'
            configlines[21] = 'K_d\n'
            configlines[22] = 'K_z\n'
            configlines[23] = 'K_SPACE\n'
            configlines[24] = 'K_a\n'
            configlines[25] = 'K_e\n'
            configlines[26] = 'K_r\n'
            configlines[29] = 'K_LEFT\n'
            configlines[30] = 'K_RIGHT\n'
            configlines[31] = 'K_UP\n'
            configlines[32] = 'K_KP0\n'
            configlines[33] = 'K_KP1\n'
            configlines[34] = 'K_KP2\n'
            configlines[35] = 'K_KP3\n'


        keyboardconfig = open('keyboardconfig.txt','w')
        keyboardconfig.writelines(configlines)
        print('Basic '+configlines[0]+' settings are done, you also can change them manually in keyboardconfig.txt')
        print('Game is closing, just restart it')
        return

    #Gamemode selection
    print("------------------------")
    print("-----PROJECT ARSWA------")
    print("------------------------")

    print("Select your gamemode (q for Quick Game): ")


    while True:

        gamemode = input()

        if gamemode in existing_gamemodes:
            break

        else:
            print('Unknown gamemode, please type q :')

    #Simple game
    if gamemode == 'q':

        p1Wins = 0
        p2Wins = 0
        p1Name = ''
        p2Name = ''

        print('Best of ? (odd number)')

        while True:

            best_of = int(input())

            if best_of in existing_best_of:
                break
            if best_of > existing_best_of[19]:
                print('I don\'t think that you are going to play that much rounds... T\'ESSAYES DE ME TEST MATHIEU?? MOI ?? Please type a valid best of (odd number) ')
            else:
                print('Please type a valid best of (odd number): ')

        rounds_to_win = int(math.ceil(best_of/float(2)))
        print('Game finishes at '+str(rounds_to_win)+' wins')

        #Names  + Memes
        p1Name = input('Player 1 Name ? ')

        p2Name = input('Player 2 Name ? ')

        while True:

            while p1 == True:
                p1class = input('\nPlayer 1 Class ? Disponible: Warrior, Mage, Archer: ')
                if p1class in existing_class:
                    p1 = False
                else:
                    print("Class doesn't exists...")

            while p2 == True:
                p2class = input('\nPlayer 2 Class ? Disponible: Warrior, Mage, Archer:  ')
                if p2class in existing_class:
                    p2 = False
                else:
                    print("Class doesn't exists...")

            print('Launching game...')

            #Game starts
            winner, p1, p2 = main(p1class,p2class,p1Name,p2Name,1,p1Wins,p2Wins)
            DISPLAYSURF.blit(menuImage,(0,0))

            if winner == p1Name:
                p1Wins += 1
            if winner == p2Name:
                p2Wins += 1

            print(str(p1Name)+' '+str(p1Wins)+'-'+str(p2Wins)+' '+str(p2Name))

            if p1Wins == rounds_to_win:
                print(p1Name+' winned the best off, '+p2Name+' sucks')
                return
            if p2Wins == rounds_to_win:
                print(p2Name+' winned the best off, '+p1Name+' sucks')
                return


start_menu()
#main('Archer','Archer','Darius','Alexandre',1,0,0)
