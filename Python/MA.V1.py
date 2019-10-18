# MA: own retry to understand code...
# #MA: needed imports/environments
import gym
import gym_2048
import random
import numpy as np

env = gym.make('2048-v0')

#MA: for random generator
i = random.randint(0,100)
# MA: print not needed, but maybe save/log the generated seed for each episode? 
print(i)
env.seed(i)
env.reset()
#MA: note, not always same start 
# (sometimes only 1x "2", sometimes 2x "2", sometimes 1x"2" & 1x"4")
print("The environment is\n")
done = False
moves = 0

