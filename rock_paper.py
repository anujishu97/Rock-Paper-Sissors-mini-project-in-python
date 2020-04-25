# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 17:28:13 2020

@author: anujk
"""
import random
result=None
game_list=['rock','paper','scissor']

while(True):
    while(True):
        users_choice=input("Enter your choice-")
        users_choice=users_choice.lower()
        if users_choice not in game_list:
            print("Wrong Input")
        else:
            break
    computer_choice=random.choice(game_list)
    print("User choice-->",users_choice)
    print("Computer Choice-->",computer_choice)
    if((users_choice=="rock" and computer_choice=='paper') or (users_choice=="paper" and computer_choice=='rock')):
        result="paper"
    elif((users_choice=="rock" and computer_choice=='scissor') or (users_choice=="scissor" and computer_choice=='rock')):
        result="rock"
    else:
        result="scissor"
    
    if(users_choice==computer_choice):
        print("Match Draw")
    elif(result==users_choice):
        print("User wins")
    else:
        print("Computer Wins")
        
    ans=input("Do you want to play again?(Y/N)")
    if(ans=='N'):
        break