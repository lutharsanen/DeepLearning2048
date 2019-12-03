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
    won = 0

    #construct state space
    f1 = open('states.txt', 'r')
    states = ast.literal_eval(f1.read())
    print("states created")

    
    Q = {}
    for s in states:
        for a in range(4):
            Q[tuple(s),a] = 0

    numGames = 50
    totalRewards = np.zeros(numGames)
    for i in range(numGames):
        if i%5 == 0:
            print('starting game', i)
            game_won = False
            observation = env.reset()
            s = f.numpy_transformer(observation)
            rand = np.random.random()
            if rand < (1-EPSILON):
                a = f.maxAction(Q,s) 
            else:
                a = np.random.randint(0,4)
            done = False
            epRewards = 0
            while not done:
                observation_, reward, done, _ = env.step(a)
                s_ = f.numpy_transformer(observation_)
                rand = np.random.random()
                if rand < (1-EPSILON):
                    a_ = f.maxAction(Q,s_)
                else: 
                    a_ = np.random.randint(0,4)
                epRewards += reward
                Q[s,a] = Q[s,a] + ALPHA*(reward + GAMMA*Q[s_,a_] - Q[s,a])
                s,a = s_,a_
                if f.get_max(s)>2048:
                    game_won = True
            
            if game_won == True:
                won+= 1

            if EPSILON > 0:
                EPSILON -= 2/(numGames)  
            else:
                EPSILON = 0
            totalRewards[i] = epRewards

            print("you won " + str(won) + " from " + str(i) + " episodes.")