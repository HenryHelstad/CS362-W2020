# -*- coding: utf-8 -*-

"""
Created on Sat Jan 18 17:55:42 2020

@author: henry.helstad
"""



import Dominion
import random
from collections import defaultdict


def get_box(nV):
    box = {}
    box["Woodcutter"]=[Dominion.Woodcutter()]*10
    box["Smithy"]=[Dominion.Smithy()]*10
    box["Laboratory"]=[Dominion.Laboratory()]*10
    box["Village"]=[Dominion.Village()]*10
    box["Festival"]=[Dominion.Festival()]*10
    box["Market"]=[Dominion.Market()]*10
    box["Chancellor"]=[Dominion.Chancellor()]*10
    box["Workshop"]=[Dominion.Workshop()]*10
    box["Moneylender"]=[Dominion.Moneylender()]*10
    box["Chapel"]=[Dominion.Chapel()]*10
    box["Cellar"]=[Dominion.Cellar()]*10
    box["Remodel"]=[Dominion.Remodel()]*10
    box["Adventurer"]=[Dominion.Adventurer()]*10
    box["Feast"]=[Dominion.Feast()]*10
    box["Mine"]=[Dominion.Mine()]*10
    box["Library"]=[Dominion.Library()]*10
    box["Gardens"]=[Dominion.Gardens()]*nV
    box["Moat"]=[Dominion.Moat()]*10
    box["Council Room"]=[Dominion.Council_Room()]*10
    box["Witch"]=[Dominion.Witch()]*10
    box["Bureaucrat"]=[Dominion.Bureaucrat()]*10
    box["Militia"]=[Dominion.Militia()]*10
    box["Spy"]=[Dominion.Spy()]*10
    box["Thief"]=[Dominion.Thief()]*10
    box["Throne Room"]=[Dominion.Throne_Room()]*10
    return box

def get_supply_order():
    supply_order = {0:['Curse','Copper'],2:['Estate','Cellar','Chapel','Moat'],
                    3:['Silver','Chancellor','Village','Woodcutter','Workshop'],
                    4:['Gardens','Bureaucrat','Feast','Militia','Moneylender','Remodel','Smithy','Spy','Thief','Throne Room'],
                    5:['Duchy','Market','Council Room','Festival','Laboratory','Library','Mine','Witch'],
                    6:['Gold','Adventurer'],8:['Province']}
    return supply_order

#TEST SCENARIO, removed silver from supply_order
def get_supply_order_bug2():
    supply_order = {0:['Curse','Copper'],2:['Estate','Cellar','Chapel','Moat'],
                    3:['Chancellor','Village','Woodcutter','Workshop'],
                    4:['Gardens','Bureaucrat','Feast','Militia','Moneylender','Remodel','Smithy','Spy','Thief','Throne Room'],
                    5:['Duchy','Market','Council Room','Festival','Laboratory','Library','Mine','Witch'],
                    6:['Gold','Adventurer'],8:['Province']}
    return supply_order


def init_supply(box, nV, nC, random10, player_names):
    supply = defaultdict(list,[(k,box[k]) for k in random10])
    
    #The supply always has these cards
    supply["Copper"]=[Dominion.Copper()]*(60-len(player_names)*7)
    supply["Silver"]=[Dominion.Silver()]*40
    supply["Gold"]=[Dominion.Gold()]*30
    supply["Estate"]=[Dominion.Estate()]*nV
    supply["Duchy"]=[Dominion.Duchy()]*nV
    supply["Province"]=[Dominion.Province()]*nV
    supply["Curse"]=[Dominion.Curse()]*nC
    return supply

        
def init_players(player_names):
    players = []
    for name in player_names:
        if name[0]=="*":
            players.append(Dominion.ComputerPlayer(name[1:]))
        elif name[0]=="^":
            players.append(Dominion.TablePlayer(name[1:]))
        else:
            players.append(Dominion.Player(name))
    return players

def print_supply(supply_order,supply):
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))

def print_points(players):    
    for player in players:
        print (player.name,player.calcpoints())
 

def calc_nC(player_names):
    return -10 + 10 * len(player_names)

def calc_nV(player_names):
    if len(player_names)>2:
        return 12
    return 8
    

#TEST SCENARIO, changed the the value of number of victory cards for more than 8 players to zero 
def calc_nV_bug1(player_names):
    if len(player_names)>2:
        return 0
    return 8
 







