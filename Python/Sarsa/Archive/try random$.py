import gym 
import numpy as np
import matplotlib as plt
import gym_2048
import random
import functions2 as f
import ast

if __name__ == '__main__':
    env = gym.make('2048-v0')



    #this variable counts how many times we have won.
    won = 0
    #value we want to reach due to memory restrictions.
    GOAL = 256
    max_value = 0


    numGames = 3000
    totalRewards = []
    for i in range(numGames):
        game_won = False
        done = False
        epRewards = 0
        while not done: 
            a = np.random.randint(0,4)
            new_state, reward, done, _ = env.step(a)
            observation_ = new_state
            epRewards += reward

            #checks if the GOAL is reached. Sets the done to True to avoid KeyError (a higher state can be reached
            # but we don't want to reach it, because we don't have in in our state_space.)
            if f.get_max(observation_)==GOAL:
                game_won = True
            
            if f.get_max(observation_)>max_value:
                max_value = f.get_max(observation_)
        
        if game_won == True:
            won+= 1

        
        totalRewards.append(epRewards)
        if i%30 == 0:
            print("you won " + str(won) + " from " + str(i) + " episodes.")
            print("MAX is:" + str(max_value))

