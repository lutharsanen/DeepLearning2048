import gym 
import numpy as np
import matplotlib as plt
import gym_2048
import random
import functions as f
import ast

if __name__ == '__main__':
    env = gym.make('2048-v0')

    #model hyperparameters
    ALPHA = 0.1
    GAMMA = 0.9
    EPSILON = 1.0
    #this variable counts how many times we have won.
    won = 0
    #value we want to reach due to memory restrictions.
    GOAL = 256
    max_value = 0

    #construct state space
    '''
    f1 = open('states.txt', 'r')
    #we created the whole state_space externally to avoid a MemoryError. Though it was still hard for our machines.
    states = ast.literal_eval(f1.read())
    print("states created")
    '''

    states = []
    Q = {}
    '''
    for s in states:
        for a in range(4):
            #we changed the state to a to avoid a TypeError, because lists aren't hashable.
            Q[tuple(s),a] = 0
            '''

    numGames = 30
    totalRewards = []
    for i in range(numGames):
        game_won = False
        observation = f.numpy_transformer_light(env.reset())
        s = tuple(observation)
        #check if observation isn't already in states
        if observation not in states:
            states.append(observation)
            for a in range(4):
                #we changed the state to a to avoid a TypeError,
                #because lists aren't hashable.
                Q[tuple(s),a] = 0
        rand = np.random.random()
        if rand < (1-EPSILON):
            a = f.maxAction(Q,s) 
        else:
            a = np.random.randint(0,4)
        done = False
        epRewards = 0
        while not done:
            new_state, reward, done, _ = env.step(a)
            observation_ = f.numpy_transformer_light(new_state)
            s_ = tuple(observation_)
            if observation_ not in states:
                states.append(observation_)
                for a in range(4):
                    #we changed the state to a to avoid a TypeError,
                    #because lists aren't hashable.
                    Q[tuple(s_),a] = 0

            rand = np.random.random()
            if rand < (1-EPSILON):
                a_ = f.maxAction(Q,s_)
            else: 
                a_ = np.random.randint(0,4)
            epRewards += reward
            Q[s,a] = Q[s,a] + ALPHA*(reward + GAMMA*Q[s_,a_] - Q[s,a])
            s,a = s_,a_

            #checks if the GOAL is reached. Sets the done to True to avoid KeyError (a higher state can be reached
            # but we don't want to reach it, because we don't have in in our state_space.)
            if f.get_max(observation_)==GOAL:
                game_won = True
            
            if f.get_max(observation_)>max_value:
                max_value = f.get_max(observation_)
        
        if game_won == True:
            won+= 1

        if EPSILON > 0:
            EPSILON -= 2/(numGames)  
        else:
            EPSILON = 0
        totalRewards.append(epRewards)
        if i%5 == 0:
            print("you won " + str(won) + " from " + str(i) + " episodes.")
            print("MAX is:" + str(max_value))
            