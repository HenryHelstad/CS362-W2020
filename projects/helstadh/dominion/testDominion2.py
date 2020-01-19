# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 17:55:42 2020

@author: henry.helstad
"""

import Dominion
import random
from collections import defaultdict
import testUtility
#Get player names
player_names = ["Annie","*Ben","*Carla"]

#number of curses and victory cards
nV = testUtility.calc_nV(player_names)
nC = testUtility.calc_nC(player_names)

#Define box
box = testUtility.get_box(nV)


supply_order = testUtility.get_supply_order_bug2()


#Pick 10 cards from box to be in the supply.
boxlist = [k for k in box]
random.shuffle(boxlist)
random10 = boxlist[:10]
supply = testUtility.init_supply(box, nV, nC, random10,player_names)
#initialize the trash
trash = []

#Costruct the Player objects
players = testUtility.init_players(player_names)

#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1    
    print("\r")
    #print supply
    testUtility.print_supply(supply_order,supply) 
    print("\r")
    #print points
    testUtility.print_points(players)
    print ("\rStart of turn " + str(turn))    
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)
            

#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)
